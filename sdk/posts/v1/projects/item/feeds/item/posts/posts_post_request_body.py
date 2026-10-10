from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .posts_post_request_body_member1 import PostsPostRequestBodyMember1
    from .posts_post_request_body_member2 import PostsPostRequestBodyMember2

@dataclass
class PostsPostRequestBody(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes PostsPostRequestBodyMember1, PostsPostRequestBodyMember2
    """
    # Composed type representation for type PostsPostRequestBodyMember1
    posts_post_request_body_member1: Optional[PostsPostRequestBodyMember1] = None
    # Composed type representation for type PostsPostRequestBodyMember2
    posts_post_request_body_member2: Optional[PostsPostRequestBodyMember2] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PostsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PostsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = PostsPostRequestBody()
        from .posts_post_request_body_member1 import PostsPostRequestBodyMember1

        result.posts_post_request_body_member1 = PostsPostRequestBodyMember1()
        from .posts_post_request_body_member2 import PostsPostRequestBodyMember2

        result.posts_post_request_body_member2 = PostsPostRequestBodyMember2()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .posts_post_request_body_member1 import PostsPostRequestBodyMember1
        from .posts_post_request_body_member2 import PostsPostRequestBodyMember2

        if self.posts_post_request_body_member1 or self.posts_post_request_body_member2:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.posts_post_request_body_member1, self.posts_post_request_body_member2)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value(None, self.posts_post_request_body_member1, self.posts_post_request_body_member2)
    

