from google.protobuf import descriptor_pb2 as _descriptor_pb2
import networkbasetypes_pb2 as _networkbasetypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GE_BulletImpact: ECitadelGameEvents
GE_DisableSatVolumesEvent: ECitadelGameEvents
GE_EnableSatVolumesEvent: ECitadelGameEvents
GE_FireBullets: ECitadelGameEvents
GE_ParticleSystemManager: ECitadelGameEvents
GE_PlaceSatVolumeEvent: ECitadelGameEvents
GE_PlayerAnimEvent: ECitadelGameEvents
GE_RemoveSatVolumeEvent: ECitadelGameEvents
GE_ScreenTextPretty: ECitadelGameEvents
GE_ServerRequestedTracer: ECitadelGameEvents
PARTICLE_SYSTEM_MANAGER_EVENT_CREATE: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_DESTROY: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_DESTROY_INVOLVING: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_RELEASE: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_ENT: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_FALLBACK: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_FORWARD: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_FROZEN: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_OFFSET: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_ORIENTATION: PARTICLE_SYSTEM_MANAGER_MESSAGE
PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_SHOULD_DRAW: PARTICLE_SYSTEM_MANAGER_MESSAGE

class CMsgBulletImpact(_message.Message):
    __slots__ = ["ability_entindex", "damage", "impact_origin", "impacted_entindex", "impacted_hitbox", "shooter_entindex", "surface_normal", "surface_type", "trace_start", "weapon_subclass_id"]
    ABILITY_ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_FIELD_NUMBER: _ClassVar[int]
    IMPACTED_ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    IMPACTED_HITBOX_FIELD_NUMBER: _ClassVar[int]
    IMPACT_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    SHOOTER_ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    SURFACE_NORMAL_FIELD_NUMBER: _ClassVar[int]
    SURFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRACE_START_FIELD_NUMBER: _ClassVar[int]
    WEAPON_SUBCLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ability_entindex: int
    damage: int
    impact_origin: _networkbasetypes_pb2.CMsgVector
    impacted_entindex: int
    impacted_hitbox: int
    shooter_entindex: int
    surface_normal: _networkbasetypes_pb2.CMsgVector
    surface_type: int
    trace_start: _networkbasetypes_pb2.CMsgVector
    weapon_subclass_id: int
    def __init__(self, trace_start: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., impact_origin: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., surface_normal: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., damage: _Optional[int] = ..., surface_type: _Optional[int] = ..., ability_entindex: _Optional[int] = ..., impacted_entindex: _Optional[int] = ..., impacted_hitbox: _Optional[int] = ..., weapon_subclass_id: _Optional[int] = ..., shooter_entindex: _Optional[int] = ...) -> None: ...

class CMsgDisableSatVolumesEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgEnableSatVolumesEvent(_message.Message):
    __slots__ = ["desat_amount", "desat_tint", "mode", "outline_color", "sat_tint"]
    DESAT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DESAT_TINT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    OUTLINE_COLOR_FIELD_NUMBER: _ClassVar[int]
    SAT_TINT_FIELD_NUMBER: _ClassVar[int]
    desat_amount: float
    desat_tint: int
    mode: int
    outline_color: int
    sat_tint: int
    def __init__(self, mode: _Optional[int] = ..., desat_amount: _Optional[float] = ..., sat_tint: _Optional[int] = ..., desat_tint: _Optional[int] = ..., outline_color: _Optional[int] = ...) -> None: ...

class CMsgFireBullets(_message.Message):
    __slots__ = ["ability", "angles", "angles_original", "bullets_override", "fired_from_gun", "ignore_entity", "max_range", "origin", "penetration_percent", "seed", "shooter_entity", "shot_number", "spread", "tracer_additional", "tracer_replacement", "weapon_subclass_id"]
    class TracerAssignment(_message.Message):
        __slots__ = ["bullet_indicies", "tracer_resource_id"]
        BULLET_INDICIES_FIELD_NUMBER: _ClassVar[int]
        TRACER_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        bullet_indicies: int
        tracer_resource_id: int
        def __init__(self, tracer_resource_id: _Optional[int] = ..., bullet_indicies: _Optional[int] = ...) -> None: ...
    ABILITY_FIELD_NUMBER: _ClassVar[int]
    ANGLES_FIELD_NUMBER: _ClassVar[int]
    ANGLES_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    BULLETS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    FIRED_FROM_GUN_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MAX_RANGE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PENETRATION_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    SHOOTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SHOT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SPREAD_FIELD_NUMBER: _ClassVar[int]
    TRACER_ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    TRACER_REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPON_SUBCLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ability: int
    angles: _networkbasetypes_pb2.CMsgQAngle
    angles_original: _networkbasetypes_pb2.CMsgQAngle
    bullets_override: int
    fired_from_gun: bool
    ignore_entity: int
    max_range: float
    origin: _networkbasetypes_pb2.CMsgVector
    penetration_percent: float
    seed: int
    shooter_entity: int
    shot_number: int
    spread: float
    tracer_additional: _containers.RepeatedCompositeFieldContainer[CMsgFireBullets.TracerAssignment]
    tracer_replacement: CMsgFireBullets.TracerAssignment
    weapon_subclass_id: int
    def __init__(self, origin: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., angles: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ..., seed: _Optional[int] = ..., shooter_entity: _Optional[int] = ..., ability: _Optional[int] = ..., penetration_percent: _Optional[float] = ..., spread: _Optional[float] = ..., fired_from_gun: bool = ..., bullets_override: _Optional[int] = ..., tracer_replacement: _Optional[_Union[CMsgFireBullets.TracerAssignment, _Mapping]] = ..., tracer_additional: _Optional[_Iterable[_Union[CMsgFireBullets.TracerAssignment, _Mapping]]] = ..., angles_original: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ..., weapon_subclass_id: _Optional[int] = ..., shot_number: _Optional[int] = ..., ignore_entity: _Optional[int] = ..., max_range: _Optional[float] = ...) -> None: ...

class CMsgParticleSystemManager(_message.Message):
    __slots__ = ["create_particle", "destroy_particle", "destroy_particle_involving", "index", "release_particle_index", "type", "update_particle", "update_particle_ent", "update_particle_fallback", "update_particle_frozen", "update_particle_fwd", "update_particle_offset", "update_particle_orient", "update_particle_should_draw"]
    class CreateParticle(_message.Message):
        __slots__ = ["angles", "attach_type", "entity_handle", "particle_name_index", "position"]
        ANGLES_FIELD_NUMBER: _ClassVar[int]
        ATTACH_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        PARTICLE_NAME_INDEX_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        angles: _networkbasetypes_pb2.CMsgQAngle
        attach_type: int
        entity_handle: int
        particle_name_index: int
        position: _networkbasetypes_pb2.CMsgVector
        def __init__(self, particle_name_index: _Optional[int] = ..., attach_type: _Optional[int] = ..., entity_handle: _Optional[int] = ..., position: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., angles: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ...) -> None: ...
    class DestroyParticle(_message.Message):
        __slots__ = ["destroy_immediately"]
        DESTROY_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
        destroy_immediately: bool
        def __init__(self, destroy_immediately: bool = ...) -> None: ...
    class DestroyParticleInvolving(_message.Message):
        __slots__ = ["destroy_immediately", "entity_handle"]
        DESTROY_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        destroy_immediately: bool
        entity_handle: int
        def __init__(self, destroy_immediately: bool = ..., entity_handle: _Optional[int] = ...) -> None: ...
    class ReleaseParticleIndex(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class UpdateParticle(_message.Message):
        __slots__ = ["control_point", "position"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        position: _networkbasetypes_pb2.CMsgVector
        def __init__(self, control_point: _Optional[int] = ..., position: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...) -> None: ...
    class UpdateParticleEnt(_message.Message):
        __slots__ = ["attach_type", "attachment", "control_point", "entity_handle", "fallback_position"]
        ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        ATTACH_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_POSITION_FIELD_NUMBER: _ClassVar[int]
        attach_type: int
        attachment: int
        control_point: int
        entity_handle: int
        fallback_position: _networkbasetypes_pb2.CMsgVector
        def __init__(self, control_point: _Optional[int] = ..., entity_handle: _Optional[int] = ..., attach_type: _Optional[int] = ..., attachment: _Optional[int] = ..., fallback_position: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...) -> None: ...
    class UpdateParticleFallback(_message.Message):
        __slots__ = ["control_point", "position"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        position: _networkbasetypes_pb2.CMsgVector
        def __init__(self, control_point: _Optional[int] = ..., position: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...) -> None: ...
    class UpdateParticleFrozen(_message.Message):
        __slots__ = ["set_frozen"]
        SET_FROZEN_FIELD_NUMBER: _ClassVar[int]
        set_frozen: bool
        def __init__(self, set_frozen: bool = ...) -> None: ...
    class UpdateParticleFwd(_message.Message):
        __slots__ = ["control_point", "forward"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        FORWARD_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        forward: _networkbasetypes_pb2.CMsgVector
        def __init__(self, control_point: _Optional[int] = ..., forward: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...) -> None: ...
    class UpdateParticleOffset(_message.Message):
        __slots__ = ["control_point", "origin_offset"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_OFFSET_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        origin_offset: _networkbasetypes_pb2.CMsgVector
        def __init__(self, control_point: _Optional[int] = ..., origin_offset: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...) -> None: ...
    class UpdateParticleOrient(_message.Message):
        __slots__ = ["control_point", "forward", "left", "up"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        FORWARD_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        UP_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        forward: _networkbasetypes_pb2.CMsgVector
        left: _networkbasetypes_pb2.CMsgVector
        up: _networkbasetypes_pb2.CMsgVector
        def __init__(self, control_point: _Optional[int] = ..., forward: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., left: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., up: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...) -> None: ...
    class UpdateParticleShouldDraw(_message.Message):
        __slots__ = ["should_draw"]
        SHOULD_DRAW_FIELD_NUMBER: _ClassVar[int]
        should_draw: bool
        def __init__(self, should_draw: bool = ...) -> None: ...
    CREATE_PARTICLE_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PARTICLE_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PARTICLE_INVOLVING_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    RELEASE_PARTICLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_ENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_FROZEN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_FWD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_ORIENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_SHOULD_DRAW_FIELD_NUMBER: _ClassVar[int]
    create_particle: CMsgParticleSystemManager.CreateParticle
    destroy_particle: CMsgParticleSystemManager.DestroyParticle
    destroy_particle_involving: CMsgParticleSystemManager.DestroyParticleInvolving
    index: int
    release_particle_index: CMsgParticleSystemManager.ReleaseParticleIndex
    type: PARTICLE_SYSTEM_MANAGER_MESSAGE
    update_particle: CMsgParticleSystemManager.UpdateParticle
    update_particle_ent: CMsgParticleSystemManager.UpdateParticleEnt
    update_particle_fallback: CMsgParticleSystemManager.UpdateParticleFallback
    update_particle_frozen: CMsgParticleSystemManager.UpdateParticleFrozen
    update_particle_fwd: CMsgParticleSystemManager.UpdateParticleFwd
    update_particle_offset: CMsgParticleSystemManager.UpdateParticleOffset
    update_particle_orient: CMsgParticleSystemManager.UpdateParticleOrient
    update_particle_should_draw: CMsgParticleSystemManager.UpdateParticleShouldDraw
    def __init__(self, type: _Optional[_Union[PARTICLE_SYSTEM_MANAGER_MESSAGE, str]] = ..., index: _Optional[int] = ..., create_particle: _Optional[_Union[CMsgParticleSystemManager.CreateParticle, _Mapping]] = ..., destroy_particle: _Optional[_Union[CMsgParticleSystemManager.DestroyParticle, _Mapping]] = ..., destroy_particle_involving: _Optional[_Union[CMsgParticleSystemManager.DestroyParticleInvolving, _Mapping]] = ..., release_particle_index: _Optional[_Union[CMsgParticleSystemManager.ReleaseParticleIndex, _Mapping]] = ..., update_particle: _Optional[_Union[CMsgParticleSystemManager.UpdateParticle, _Mapping]] = ..., update_particle_fwd: _Optional[_Union[CMsgParticleSystemManager.UpdateParticleFwd, _Mapping]] = ..., update_particle_orient: _Optional[_Union[CMsgParticleSystemManager.UpdateParticleOrient, _Mapping]] = ..., update_particle_fallback: _Optional[_Union[CMsgParticleSystemManager.UpdateParticleFallback, _Mapping]] = ..., update_particle_offset: _Optional[_Union[CMsgParticleSystemManager.UpdateParticleOffset, _Mapping]] = ..., update_particle_ent: _Optional[_Union[CMsgParticleSystemManager.UpdateParticleEnt, _Mapping]] = ..., update_particle_frozen: _Optional[_Union[CMsgParticleSystemManager.UpdateParticleFrozen, _Mapping]] = ..., update_particle_should_draw: _Optional[_Union[CMsgParticleSystemManager.UpdateParticleShouldDraw, _Mapping]] = ...) -> None: ...

class CMsgPlaceSatVolumeEvent(_message.Message):
    __slots__ = ["attachment_handle", "direction", "entity_handle", "falloff_distance", "phi_dot", "position", "radius", "theta_dot", "type", "volume_id"]
    ATTACHMENT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FALLOFF_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    PHI_DOT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    THETA_DOT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    attachment_handle: int
    direction: _networkbasetypes_pb2.CMsgVector
    entity_handle: int
    falloff_distance: float
    phi_dot: float
    position: _networkbasetypes_pb2.CMsgVector
    radius: float
    theta_dot: float
    type: int
    volume_id: int
    def __init__(self, position: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., direction: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., radius: _Optional[float] = ..., falloff_distance: _Optional[float] = ..., theta_dot: _Optional[float] = ..., phi_dot: _Optional[float] = ..., entity_handle: _Optional[int] = ..., attachment_handle: _Optional[int] = ..., type: _Optional[int] = ..., volume_id: _Optional[int] = ...) -> None: ...

class CMsgPlayerAnimEvent(_message.Message):
    __slots__ = ["data", "event", "player"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    data: int
    event: int
    player: int
    def __init__(self, player: _Optional[int] = ..., event: _Optional[int] = ..., data: _Optional[int] = ...) -> None: ...

class CMsgRemoveSatVolumeEvent(_message.Message):
    __slots__ = ["volume_id"]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    volume_id: int
    def __init__(self, volume_id: _Optional[int] = ...) -> None: ...

class CMsgScreenTextPretty(_message.Message):
    __slots__ = ["a", "b", "bold_font", "duration", "font_name", "font_size", "g", "line", "r", "text", "x_pos", "y_pos"]
    A_FIELD_NUMBER: _ClassVar[int]
    BOLD_FONT_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FONT_NAME_FIELD_NUMBER: _ClassVar[int]
    FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    X_POS_FIELD_NUMBER: _ClassVar[int]
    Y_POS_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    bold_font: bool
    duration: float
    font_name: str
    font_size: int
    g: int
    line: int
    r: int
    text: str
    x_pos: float
    y_pos: float
    def __init__(self, x_pos: _Optional[float] = ..., y_pos: _Optional[float] = ..., line: _Optional[int] = ..., text: _Optional[str] = ..., r: _Optional[int] = ..., g: _Optional[int] = ..., b: _Optional[int] = ..., a: _Optional[int] = ..., duration: _Optional[float] = ..., font_name: _Optional[str] = ..., font_size: _Optional[int] = ..., bold_font: bool = ...) -> None: ...

class CMsgServerRequestedTracer(_message.Message):
    __slots__ = ["dps", "end", "entity_handle", "origin", "weaponid"]
    DPS_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    WEAPONID_FIELD_NUMBER: _ClassVar[int]
    dps: float
    end: _networkbasetypes_pb2.CMsgVector
    entity_handle: int
    origin: _networkbasetypes_pb2.CMsgVector
    weaponid: int
    def __init__(self, origin: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., end: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., weaponid: _Optional[int] = ..., entity_handle: _Optional[int] = ..., dps: _Optional[float] = ...) -> None: ...

class ECitadelGameEvents(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PARTICLE_SYSTEM_MANAGER_MESSAGE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
