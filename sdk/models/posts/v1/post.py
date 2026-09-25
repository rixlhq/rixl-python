from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .post_member1 import PostMember1
    from .post_member2 import PostMember2

@dataclass
class Post(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes PostMember1, PostMember2
    """
    # Composed type representation for type PostMember1
    post_member1: Optional[PostMember1] = None
    # Composed type representation for type PostMember2
    post_member2: Optional[PostMember2] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Post:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Post
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = Post()
        from .post_member1 import PostMember1

        result.post_member1 = PostMember1()
        from .post_member2 import PostMember2

        result.post_member2 = PostMember2()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .post_member1 import PostMember1
        from .post_member2 import PostMember2

        if self.post_member1 or self.post_member2:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.post_member1, self.post_member2)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value(None, self.post_member1, self.post_member2)
    

