#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
INPUT_SPEC="${ROOT_DIR}/openapi/public.swagger.json"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

require_command() {
	local command="$1"
	if ! command -v "${command}" >/dev/null 2>&1; then
		echo "${command} is required" >&2
		exit 1
	fi
}

if [[ $# -gt 1 ]]; then
	echo "usage: $0 [path-to-public-swagger.json]" >&2
	exit 1
fi

if [[ $# -eq 1 ]]; then
	"${SCRIPT_DIR}/prepare-spec.sh" "$1"
fi

require_command java
require_command npx
require_command perl
require_command rsync

if [[ ! -f "${INPUT_SPEC}" ]]; then
	echo "sanitized SDK spec not found at ${INPUT_SPEC}" >&2
	echo "run scripts/prepare-spec.sh first or pass a swagger.json path to this script" >&2
	exit 1
fi

npx -y @openapitools/openapi-generator-cli generate \
	-g python \
	-i "${INPUT_SPEC}" \
	-o "${TMP_DIR}" \
	--global-property apiTests=false,modelTests=false \
	--additional-properties "packageName=rixl_api,projectName=rixl_api,packageVersion=2.0.0,packageUrl=https://github.com/qeeqez/rixl-sdk-python"

perl -0pi -e 's{http://localhost}{https://api.rixl.com}g; s{https://github.com/GIT_USER_ID/GIT_REPO_ID}{https://github.com/qeeqez/rixl-sdk-python}g' "${TMP_DIR}/README.md" "${TMP_DIR}/pyproject.toml"
perl -0pi -e 's{https://github.com/qeeqez/api}{https://github.com/qeeqez/rixl-sdk-python}g' "${TMP_DIR}/setup.py"

rm -rf "${TMP_DIR}/.openapi-generator"
rm -f "${TMP_DIR}/.gitlab-ci.yml" "${TMP_DIR}/.travis.yml" "${TMP_DIR}/git_push.sh"

rsync -a --delete \
	--exclude '.git' \
	--exclude '.github' \
	--exclude 'scripts' \
	--exclude 'openapi' \
	--exclude 'openapitools.json' \
	"${TMP_DIR}/" "${ROOT_DIR}/"

echo "Generated Python SDK at ${ROOT_DIR}"
