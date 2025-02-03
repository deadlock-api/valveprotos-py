# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .networkbasetypes_p2p import CMsgQAngle
from .networkbasetypes_p2p import CMsgVector
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class ECitadelGameEvents(IntEnum):
    GE_FireBullets = 450
    GE_PlayerAnimEvent = 451
    GE_ParticleSystemManager = 458
    GE_ScreenTextPretty = 459
    GE_ServerRequestedTracer = 460
    GE_BulletImpact = 461
    GE_EnableSatVolumesEvent = 462
    GE_PlaceSatVolumeEvent = 463
    GE_DisableSatVolumesEvent = 464
    GE_RemoveSatVolumeEvent = 465


class PARTICLE_SYSTEM_MANAGER_MESSAGE(IntEnum):
    PARTICLE_SYSTEM_MANAGER_EVENT_CREATE = 0
    PARTICLE_SYSTEM_MANAGER_EVENT_DESTROY = 1
    PARTICLE_SYSTEM_MANAGER_EVENT_DESTROY_INVOLVING = 2
    PARTICLE_SYSTEM_MANAGER_EVENT_RELEASE = 3
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE = 4
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_FORWARD = 5
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_ORIENTATION = 6
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_FALLBACK = 7
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_ENT = 8
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_OFFSET = 9
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_FROZEN = 10
    PARTICLE_SYSTEM_MANAGER_EVENT_UPDATE_SHOULD_DRAW = 11

class CMsgFireBullets(BaseModel):
    class TracerAssignment(BaseModel):
        tracer_resource_id: int = Field(default=0)
        bullet_indicies: int = Field(default=0)

    origin: CMsgVector = Field()
    angles: CMsgQAngle = Field()
    seed: int = Field(default=0)
    shooter_entity: int = Field(default=0)
    ability: int = Field(default=0)
    penetration_percent: float = Field(default=0.0)
    spread: float = Field(default=0.0)
    fired_from_gun: bool = Field(default=False)
    bullets_override: int = Field(default=0)
    tracer_replacement: "CMsgFireBullets.TracerAssignment" = Field()
    tracer_additional: typing.List["CMsgFireBullets.TracerAssignment"] = Field(default_factory=list)
    angles_original: CMsgQAngle = Field()
    weapon_subclass_id: int = Field(default=0)
    shot_number: int = Field(default=0)
    ignore_entity: int = Field(default=0)
    max_range: float = Field(default=0.0)

class CMsgBulletImpact(BaseModel):
    trace_start: CMsgVector = Field()
    impact_origin: CMsgVector = Field()
    surface_normal: CMsgVector = Field()
    damage: int = Field(default=0)
    surface_type: int = Field(default=0)
    ability_entindex: int = Field(default=0)
    impacted_entindex: int = Field(default=0)
    impacted_hitbox: int = Field(default=0)
    weapon_subclass_id: int = Field(default=0)
    shooter_entindex: int = Field(default=0)

class CMsgPlayerAnimEvent(BaseModel):
    player: float = Field(default=0.0)
    event: int = Field(default=0)
    data: int = Field(default=0)

class CMsgParticleSystemManager(BaseModel):
    class CreateParticle(BaseModel):
        particle_name_index: float = Field(default=0.0)
        attach_type: int = Field(default=0)
        entity_handle: int = Field(default=0)
        position: CMsgVector = Field()
        angles: CMsgQAngle = Field()

    class DestroyParticle(BaseModel):
        destroy_immediately: bool = Field(default=False)

    class DestroyParticleInvolving(BaseModel):
        destroy_immediately: bool = Field(default=False)
        entity_handle: int = Field(default=0)

    class ReleaseParticleIndex(BaseModel):
        pass

    class UpdateParticle(BaseModel):
        control_point: int = Field(default=0)
        position: CMsgVector = Field()

    class UpdateParticleFwd(BaseModel):
        control_point: int = Field(default=0)
        forward: CMsgVector = Field()

    class UpdateParticleOrient(BaseModel):
        control_point: int = Field(default=0)
        forward: CMsgVector = Field()
        left: CMsgVector = Field()
        up: CMsgVector = Field()

    class UpdateParticleFallback(BaseModel):
        control_point: int = Field(default=0)
        position: CMsgVector = Field()

    class UpdateParticleEnt(BaseModel):
        control_point: int = Field(default=0)
        entity_handle: int = Field(default=0)
        attach_type: int = Field(default=0)
        attachment: int = Field(default=0)
        fallback_position: CMsgVector = Field()

    class UpdateParticleOffset(BaseModel):
        control_point: int = Field(default=0)
        origin_offset: CMsgVector = Field()

    class UpdateParticleFrozen(BaseModel):
        set_frozen: bool = Field(default=False)

    class UpdateParticleShouldDraw(BaseModel):
        should_draw: bool = Field(default=False)

    type: PARTICLE_SYSTEM_MANAGER_MESSAGE = Field(default=0)
    index: int = Field(default=0)
    create_particle: "CMsgParticleSystemManager.CreateParticle" = Field()
    destroy_particle: "CMsgParticleSystemManager.DestroyParticle" = Field()
    destroy_particle_involving: "CMsgParticleSystemManager.DestroyParticleInvolving" = Field()
    release_particle_index: "CMsgParticleSystemManager.ReleaseParticleIndex" = Field()
    update_particle: "CMsgParticleSystemManager.UpdateParticle" = Field()
    update_particle_fwd: "CMsgParticleSystemManager.UpdateParticleFwd" = Field()
    update_particle_orient: "CMsgParticleSystemManager.UpdateParticleOrient" = Field()
    update_particle_fallback: "CMsgParticleSystemManager.UpdateParticleFallback" = Field()
    update_particle_offset: "CMsgParticleSystemManager.UpdateParticleOffset" = Field()
    update_particle_ent: "CMsgParticleSystemManager.UpdateParticleEnt" = Field()
    update_particle_frozen: "CMsgParticleSystemManager.UpdateParticleFrozen" = Field()
    update_particle_should_draw: "CMsgParticleSystemManager.UpdateParticleShouldDraw" = Field()

class CMsgScreenTextPretty(BaseModel):
    x_pos: float = Field(default=0.0)
    y_pos: float = Field(default=0.0)
    line: int = Field(default=0)
    text: str = Field(default="")
    r: int = Field(default=0)
    g: int = Field(default=0)
    b: int = Field(default=0)
    a: int = Field(default=0)
    duration: float = Field(default=0.0)
    font_name: str = Field(default="")
    font_size: int = Field(default=0)
    bold_font: bool = Field(default=False)

class CMsgServerRequestedTracer(BaseModel):
    origin: CMsgVector = Field()
    end: CMsgVector = Field()
    weaponid: int = Field(default=0)
    entity_handle: int = Field(default=0)
    dps: float = Field(default=0.0)

class CMsgEnableSatVolumesEvent(BaseModel):
    mode: int = Field(default=0)
    desat_amount: float = Field(default=0.0)
    sat_tint: float = Field(default=0.0)
    desat_tint: float = Field(default=0.0)
    outline_color: float = Field(default=0.0)

class CMsgPlaceSatVolumeEvent(BaseModel):
    position: CMsgVector = Field()
    direction: CMsgVector = Field()
    radius: float = Field(default=0.0)
    falloff_distance: float = Field(default=0.0)
    theta_dot: float = Field(default=0.0)
    phi_dot: float = Field(default=0.0)
    entity_handle: int = Field(default=0)
    attachment_handle: int = Field(default=0)
    type: int = Field(default=0)
    volume_id: int = Field(default=0)

class CMsgRemoveSatVolumeEvent(BaseModel):
    volume_id: int = Field(default=0)

class CMsgDisableSatVolumesEvent(BaseModel):
    pass
