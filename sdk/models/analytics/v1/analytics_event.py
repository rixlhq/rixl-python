from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_event_member1 import AnalyticsEventMember1
    from .analytics_event_member2 import AnalyticsEventMember2
    from .analytics_event_member3 import AnalyticsEventMember3
    from .analytics_event_member4 import AnalyticsEventMember4
    from .analytics_event_member5 import AnalyticsEventMember5

@dataclass
class AnalyticsEvent(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes AnalyticsEventMember1, AnalyticsEventMember2, AnalyticsEventMember3, AnalyticsEventMember4, AnalyticsEventMember5
    """
    # Composed type representation for type AnalyticsEventMember1
    analytics_event_member1: Optional[AnalyticsEventMember1] = None
    # Composed type representation for type AnalyticsEventMember2
    analytics_event_member2: Optional[AnalyticsEventMember2] = None
    # Composed type representation for type AnalyticsEventMember3
    analytics_event_member3: Optional[AnalyticsEventMember3] = None
    # Composed type representation for type AnalyticsEventMember4
    analytics_event_member4: Optional[AnalyticsEventMember4] = None
    # Composed type representation for type AnalyticsEventMember5
    analytics_event_member5: Optional[AnalyticsEventMember5] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyticsEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyticsEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = AnalyticsEvent()
        from .analytics_event_member1 import AnalyticsEventMember1

        result.analytics_event_member1 = AnalyticsEventMember1()
        from .analytics_event_member2 import AnalyticsEventMember2

        result.analytics_event_member2 = AnalyticsEventMember2()
        from .analytics_event_member3 import AnalyticsEventMember3

        result.analytics_event_member3 = AnalyticsEventMember3()
        from .analytics_event_member4 import AnalyticsEventMember4

        result.analytics_event_member4 = AnalyticsEventMember4()
        from .analytics_event_member5 import AnalyticsEventMember5

        result.analytics_event_member5 = AnalyticsEventMember5()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_event_member1 import AnalyticsEventMember1
        from .analytics_event_member2 import AnalyticsEventMember2
        from .analytics_event_member3 import AnalyticsEventMember3
        from .analytics_event_member4 import AnalyticsEventMember4
        from .analytics_event_member5 import AnalyticsEventMember5

        if self.analytics_event_member1 or self.analytics_event_member2 or self.analytics_event_member3 or self.analytics_event_member4 or self.analytics_event_member5:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.analytics_event_member1, self.analytics_event_member2, self.analytics_event_member3, self.analytics_event_member4, self.analytics_event_member5)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value(None, self.analytics_event_member1, self.analytics_event_member2, self.analytics_event_member3, self.analytics_event_member4, self.analytics_event_member5)
    

