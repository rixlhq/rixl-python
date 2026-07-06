from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .blog.blog_request_builder import BlogRequestBuilder
    from .email.email_request_builder import EmailRequestBuilder
    from .invitations.invitations_request_builder import InvitationsRequestBuilder
    from .login.login_request_builder import LoginRequestBuilder
    from .logout.logout_request_builder import LogoutRequestBuilder
    from .memberships.memberships_request_builder import MembershipsRequestBuilder
    from .passkey.passkey_request_builder import PasskeyRequestBuilder
    from .password.password_request_builder import PasswordRequestBuilder
    from .policies.policies_request_builder import PoliciesRequestBuilder
    from .providers.providers_request_builder import ProvidersRequestBuilder
    from .register.register_request_builder import RegisterRequestBuilder
    from .token.token_request_builder import TokenRequestBuilder
    from .userinfo.userinfo_request_builder import UserinfoRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder
    from .verify_passkey.verify_passkey_request_builder import VerifyPasskeyRequestBuilder
    from .verify_totp.verify_totp_request_builder import VerifyTotpRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1", path_parameters)
    
    @property
    def blog(self) -> BlogRequestBuilder:
        """
        The blog property
        """
        from .blog.blog_request_builder import BlogRequestBuilder

        return BlogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email(self) -> EmailRequestBuilder:
        """
        The email property
        """
        from .email.email_request_builder import EmailRequestBuilder

        return EmailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invitations(self) -> InvitationsRequestBuilder:
        """
        The invitations property
        """
        from .invitations.invitations_request_builder import InvitationsRequestBuilder

        return InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def login(self) -> LoginRequestBuilder:
        """
        The login property
        """
        from .login.login_request_builder import LoginRequestBuilder

        return LoginRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logout(self) -> LogoutRequestBuilder:
        """
        The logout property
        """
        from .logout.logout_request_builder import LogoutRequestBuilder

        return LogoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def memberships(self) -> MembershipsRequestBuilder:
        """
        The memberships property
        """
        from .memberships.memberships_request_builder import MembershipsRequestBuilder

        return MembershipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passkey(self) -> PasskeyRequestBuilder:
        """
        The passkey property
        """
        from .passkey.passkey_request_builder import PasskeyRequestBuilder

        return PasskeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password(self) -> PasswordRequestBuilder:
        """
        The password property
        """
        from .password.password_request_builder import PasswordRequestBuilder

        return PasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> PoliciesRequestBuilder:
        """
        The policies property
        """
        from .policies.policies_request_builder import PoliciesRequestBuilder

        return PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def providers(self) -> ProvidersRequestBuilder:
        """
        The providers property
        """
        from .providers.providers_request_builder import ProvidersRequestBuilder

        return ProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def register(self) -> RegisterRequestBuilder:
        """
        The register property
        """
        from .register.register_request_builder import RegisterRequestBuilder

        return RegisterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token(self) -> TokenRequestBuilder:
        """
        The token property
        """
        from .token.token_request_builder import TokenRequestBuilder

        return TokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def userinfo(self) -> UserinfoRequestBuilder:
        """
        The userinfo property
        """
        from .userinfo.userinfo_request_builder import UserinfoRequestBuilder

        return UserinfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        The users property
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify_passkey(self) -> VerifyPasskeyRequestBuilder:
        """
        The verifyPasskey property
        """
        from .verify_passkey.verify_passkey_request_builder import VerifyPasskeyRequestBuilder

        return VerifyPasskeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify_totp(self) -> VerifyTotpRequestBuilder:
        """
        The verifyTotp property
        """
        from .verify_totp.verify_totp_request_builder import VerifyTotpRequestBuilder

        return VerifyTotpRequestBuilder(self.request_adapter, self.path_parameters)
    

