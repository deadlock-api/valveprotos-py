# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: citadel_usermessages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2
import citadel_gcmessages_common_pb2 as citadel__gcmessages__common__pb2
import gameevents_pb2 as gameevents__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63itadel_usermessages.proto\x1a\x16networkbasetypes.proto\x1a\x1f\x63itadel_gcmessages_common.proto\x1a\x10gameevents.proto\"\"\n\x11\x43UserMessageEmpty\x12\r\n\x05\x65mpty\x18\x01 \x01(\r\"\xd7\x04\n\x1a\x43\x43itadelUserMessage_Damage\x12\x0e\n\x06\x64\x61mage\x18\x01 \x01(\x05\x12\x12\n\npre_damage\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x14\n\x0c\x63itadel_type\x18\x04 \x01(\x05\x12\x1b\n\x06origin\x18\x05 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x0f\x65ntindex_victim\x18\x06 \x01(\x05:\x02-1\x12\x1e\n\x12\x65ntindex_inflictor\x18\x07 \x01(\x05:\x02-1\x12\x1d\n\x11\x65ntindex_attacker\x18\x08 \x01(\x05:\x02-1\x12\x1c\n\x10\x65ntindex_ability\x18\t \x01(\x05:\x02-1\x12\x17\n\x0f\x64\x61mage_absorbed\x18\n \x01(\x05\x12\x19\n\x11victim_health_max\x18\x0b \x01(\x05\x12\x19\n\x11victim_health_new\x18\x0c \x01(\x05\x12\r\n\x05\x66lags\x18\r \x01(\x04\x12\x12\n\nability_id\x18\x0e \x01(\r\x12\x16\n\x0e\x61ttacker_class\x18\x0f \x01(\r\x12\x14\n\x0cvictim_class\x18\x10 \x01(\r\x12\x19\n\x11victim_shield_max\x18\x11 \x01(\x05\x12\x19\n\x11victim_shield_new\x18\x12 \x01(\x05\x12\x0c\n\x04hits\x18\x13 \x01(\x05\x12\x13\n\x0bhealth_lost\x18\x14 \x01(\x05\x12\x13\n\x0bhitgroup_id\x18\x15 \x01(\x05\x12%\n\x19\x65ntindex_attacking_object\x18\x16 \x01(\x05:\x02-1\x12%\n\x10\x64\x61mage_direction\x18\x17 \x01(\x0b\x32\x0b.CMsgVector\"\xd5\x01\n\x0ePingCommonData\x12\x17\n\x0fping_message_id\x18\x01 \x01(\r\x12\"\n\rping_location\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x1e\n\x0c\x65ntity_index\x18\x03 \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x1e\n\x12sender_player_slot\x18\x04 \x01(\x05:\x02-1\x12\x16\n\x0espeech_concept\x18\x05 \x01(\x05\x12\x17\n\x0fresponse_chosen\x18\x06 \x01(\t\x12\x15\n\rcooldown_time\x18\x07 \x01(\x02\"\xb7\x02\n\x17\x43\x43itadelUserMsg_MapPing\x12\"\n\tping_data\x18\x01 \x02(\x0b\x32\x0f.PingCommonData\x12\x12\n\nevent_type\x18\x02 \x01(\r\x12`\n\x1aping_marker_and_sound_info\x18\x03 \x01(\x0e\x32\x16.ChatMsgPingMarkerInfo:$k_EPingMarkerInfo_ShowMarkerAndSound\x12\x1b\n\x13pinged_enemy_entity\x18\x04 \x01(\x08\x12\x1b\n\x13pinged_entity_class\x18\x05 \x01(\r\x12\x17\n\x0fis_minimap_ping\x18\x06 \x01(\x08\x12\x18\n\x10pinged_hero_name\x18\x07 \x01(\t\x12\x15\n\ris_blind_ping\x18\x08 \x01(\x08\"]\n\x19\x43\x43itadelUserMsg_PingWheel\x12\"\n\tping_data\x18\x01 \x02(\x0b\x32\x0f.PingCommonData\x12\x1c\n\x14ping_wheel_option_id\x18\x02 \x01(\r\"\xd1\x01\n\x1b\x43\x43itadelUserMsg_AbilityPing\x12\"\n\tping_data\x18\x01 \x01(\x0b\x32\x0f.PingCommonData\x12\x12\n\nability_id\x18\x02 \x01(\r\x12\x18\n\x10\x61\x62ility_cooldown\x18\x03 \x01(\x02\x12`\n\x1aping_marker_and_sound_info\x18\x04 \x01(\x0e\x32\x16.ChatMsgPingMarkerInfo:$k_EPingMarkerInfo_ShowMarkerAndSound\"\xcb\x01\n\x1d\x43\x43itadelUserMsg_QuickResponse\x12\"\n\tping_data\x18\x01 \x02(\x0b\x32\x0f.PingCommonData\x12%\n\x1dresponding_to_ping_message_id\x18\x02 \x01(\r\x12%\n\x19responding_to_player_slot\x18\x03 \x01(\x05:\x02-1\x12\x38\n\nlane_color\x18\x04 \x01(\x0e\x32\x0e.CMsgLaneColor:\x14k_ELaneColor_Invalid\"X\n\x17\x43\x43itadelUserMsg_MapLine\x12\x1e\n\x12sender_player_slot\x18\x01 \x01(\x05:\x02-1\x12\x1d\n\x07mapline\x18\x02 \x01(\x0b\x32\x0c.CMsgMapLine\"G\n\x1b\x43\x43itadelUserMsg_TeamRewards\x12\n\n\x02xp\x18\x01 \x01(\r\x12\x0c\n\x04gold\x18\x02 \x01(\r\x12\x0e\n\x06winner\x18\x03 \x01(\x08\"\xf0\x01\n\"CCitadelUserMsg_TriggerDamageFlash\x12!\n\x15\x65ntindex_flash_victim\x18\x01 \x01(\x05:\x02-1\x12#\n\x17\x65ntindex_flash_attacker\x18\x02 \x01(\x05:\x02-1\x12\x1f\n\x17\x65ntindex_flash_hitgroup\x18\x03 \x01(\x05\x12\x13\n\x0b\x66lash_value\x18\x04 \x01(\r\x12\x12\n\nflash_type\x18\x05 \x01(\r\x12\x13\n\x0b\x66lash_flags\x18\x06 \x01(\r\x12#\n\x0e\x66lash_position\x18\x07 \x01(\x0b\x32\x0b.CMsgVector\"\x86\x02\n CCitadelUserMsg_AbilitiesChanged\x12!\n\x15purchaser_player_slot\x18\x01 \x01(\x05:\x02-1\x12\x12\n\nability_id\x18\x02 \x01(\r\x12\x42\n\x06\x63hange\x18\x03 \x01(\x0e\x32(.CCitadelUserMsg_AbilitiesChanged.Change:\x08\x45Invalid\"g\n\x06\x43hange\x12\x15\n\x08\x45Invalid\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0e\n\nEPurchased\x10\x00\x12\r\n\tEUpgraded\x10\x01\x12\t\n\x05\x45Sold\x10\x02\x12\x1c\n\x18\x45SwappedActivatedAbility\x10\x03\"\xc0\x01\n\"CCitadelUserMsg_AbilityInterrupted\x12\x1b\n\x0f\x65ntindex_victim\x18\x01 \x01(\x05:\x02-1\x12 \n\x14\x65ntindex_interrupter\x18\x02 \x01(\x05:\x02-1\x12\x1e\n\x16\x61\x62ility_id_interrupted\x18\x03 \x01(\r\x12\x1e\n\x16\x61\x62ility_id_interrupter\x18\x04 \x01(\r\x12\x1b\n\x13hero_id_interrupter\x18\x05 \x01(\r\"u\n\"CCitadelUserMsg_AbilityLateFailure\x12\x1b\n\x0f\x65ntindex_caster\x18\x01 \x01(\x05:\x02-1\x12\x1c\n\x10\x65ntindex_ability\x18\x02 \x01(\x05:\x02-1\x12\x14\n\x0c\x66\x61ilure_type\x18\x03 \x01(\r\"\x86\x05\n#CCitadelUserMsg_RecentDamageSummary\x12\x17\n\x0bplayer_slot\x18\x01 \x01(\x05:\x02-1\x12I\n\x0e\x64\x61mage_records\x18\x02 \x03(\x0b\x32\x31.CCitadelUserMsg_RecentDamageSummary.DamageRecord\x12\x12\n\nstart_time\x18\x03 \x01(\x02\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x02\x12\x14\n\x0ctotal_damage\x18\x05 \x01(\x05\x12\x11\n\tlost_gold\x18\x06 \x01(\x05\x12M\n\x10modifier_records\x18\x07 \x03(\x0b\x32\x33.CCitadelUserMsg_RecentDamageSummary.ModifierRecord\x1a\xc8\x01\n\x0c\x44\x61mageRecord\x12\x0e\n\x06\x64\x61mage\x18\x01 \x01(\x05\x12\x0c\n\x04hits\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x61mage_type\x18\x03 \x01(\r\x12\x0f\n\x07hero_id\x18\x04 \x01(\r\x12\x12\n\nability_id\x18\x05 \x01(\r\x12\x16\n\x0e\x61ttacker_class\x18\x06 \x01(\r\x12\x17\n\x0f\x64\x61mage_absorbed\x18\x07 \x01(\x05\x12\x17\n\x0fis_killing_blow\x18\x08 \x01(\x08\x12\x16\n\x0evictim_hero_id\x18\t \x01(\r\x1a\x91\x01\n\x0eModifierRecord\x12\x12\n\nability_id\x18\x01 \x01(\r\x12\x18\n\x10modifier_type_id\x18\x02 \x01(\r\x12\x1b\n\x0f\x65ntindex_caster\x18\x03 \x01(\x05:\x02-1\x12\x12\n\nstart_time\x18\x04 \x01(\x02\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\x02\x12\x0e\n\x06\x64\x65\x62uff\x18\x06 \x01(\x08\":\n$CCitadelUserMsg_SpectatorTeamChanged\x12\x12\n\nteamnumber\x18\x01 \x01(\x05\"\xd8\x01\n\x19\x43\x43itadelUserMsg_ChatWheel\x12\x17\n\x0f\x63hat_message_id\x18\x01 \x01(\r\x12\x17\n\x0bplayer_slot\x18\x02 \x01(\x05:\x02-1\x12\x19\n\rpawn_entindex\x18\x03 \x01(\x05:\x02-1\x12\x12\n\naccount_id\x18\x04 \x01(\r\x12\x0f\n\x07hero_id\x18\x05 \x01(\r\x12\x0f\n\x07param_1\x18\x06 \x01(\t\x12\x38\n\nlane_color\x18\x07 \x01(\x0e\x32\x0e.CMsgLaneColor:\x14k_ELaneColor_Invalid\"\x8c\x01\n\x17\x43\x43itadelUserMsg_ChatMsg\x12\x17\n\x0bplayer_slot\x18\x01 \x01(\x05:\x02-1\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x10\n\x08\x61ll_chat\x18\x03 \x01(\x08\x12\x38\n\nlane_color\x18\x04 \x01(\x0e\x32\x0e.CMsgLaneColor:\x14k_ELaneColor_Invalid\"\xa7\x02\n\x1b\x43\x43itadelUserMsg_GoldHistory\x12\x1b\n\x0f\x65ntindex_player\x18\x01 \x01(\x05:\x02-1\x12\x41\n\x0eminute_records\x18\x02 \x03(\x0b\x32).CCitadelUserMsg_GoldHistory.MinuteRecord\x1a\x43\n\nGoldRecord\x12\x17\n\x0f\x63urrency_source\x18\x01 \x01(\x05\x12\x0c\n\x04gold\x18\x02 \x01(\x05\x12\x0e\n\x06\x65vents\x18\x03 \x01(\x05\x1a\x63\n\x0cMinuteRecord\x12\x14\n\x0cmatch_minute\x18\x01 \x01(\x05\x12=\n\x0cgold_records\x18\x02 \x03(\x0b\x32\'.CCitadelUserMsg_GoldHistory.GoldRecord\"\xba\n\n CCitadelUserMsg_CameraController\x12.\n\x06\x61\x63tion\x18\x01 \x02(\x0e\x32\r.CameraAction:\x0fk_EAction_AddOp\x12\x39\n\toperation\x18\x02 \x01(\x0e\x32\x10.CameraOperation:\x14k_ECameraOp_Maintain\x12\x31\n\x05param\x18\x03 \x01(\x0e\x32\x0c.CameraParam:\x14k_EParam_ClearAllOps\x12\x44\n\nparam_mode\x18\x0c \x01(\x0e\x32\x10.CameraParamMode:\x1ek_EParamMode_AllowInOneContext\x12\r\n\x05\x64\x65lay\x18\x04 \x01(\x02\x12\x17\n\x0frelative_values\x18\x0b \x01(\x08\x12\x19\n\x11\x63ontext_symbol_id\x18\x05 \x01(\r\x12\x13\n\x08priority\x18\r \x01(\r:\x01\x31\x12<\n\x08maintain\x18\x06 \x01(\x0b\x32*.CCitadelUserMsg_CameraController.Maintain\x12<\n\x08\x61pproach\x18\x07 \x01(\x0b\x32*.CCitadelUserMsg_CameraController.Approach\x12\x38\n\x06spring\x18\x08 \x01(\x0b\x32(.CCitadelUserMsg_CameraController.Spring\x12\x34\n\x04lerp\x18\t \x01(\x0b\x32&.CCitadelUserMsg_CameraController.Lerp\x12\x32\n\x03lag\x18\n \x01(\x0b\x32%.CCitadelUserMsg_CameraController.Lag\x1a\x1f\n\x08Maintain\x12\x13\n\x08\x64uration\x18\x01 \x01(\x02:\x01\x30\x1a\xc4\x01\n\x08\x41pproach\x12\x12\n\x05speed\x18\x01 \x01(\x02:\x03\x36\x30\x30\x12\x1a\n\rdefault_speed\x18\x02 \x01(\x02:\x03\x36\x30\x30\x12\x1a\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x02:\x04\x31\x30\x30\x30\x12\x17\n\x0cmin_duration\x18\x04 \x01(\x02:\x01\x30\x12\x16\n\x0e\x61pproach_float\x18\x05 \x01(\x02\x12$\n\x0f\x61pproach_vector\x18\x06 \x01(\x0b\x32\x0b.CMsgVector\x12\x15\n\rchase_default\x18\x07 \x01(\x08\x1a\x8e\x01\n\x06Spring\x12\x1b\n\x0fspring_strength\x18\x01 \x01(\x02:\x02\x31\x30\x12\x14\n\tmin_speed\x18\x04 \x01(\x02:\x01\x30\x12\x17\n\x0cmax_duration\x18\x05 \x01(\x02:\x01\x30\x12\x14\n\x0ctarget_float\x18\x06 \x01(\x02\x12\"\n\rtarget_vector\x18\x07 \x01(\x0b\x32\x0b.CMsgVector\x1a\xa3\x01\n\x04Lerp\x12\x13\n\x0bstart_float\x18\x01 \x01(\x02\x12!\n\x0cstart_vector\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x11\n\tend_float\x18\x03 \x01(\x02\x12\x1f\n\nend_vector\x18\x04 \x01(\x0b\x32\x0b.CMsgVector\x12\x0c\n\x04\x62ias\x18\x05 \x01(\x02\x12\x0c\n\x04gain\x18\x06 \x01(\x02\x12\x13\n\x08\x64uration\x18\x07 \x01(\x02:\x01\x31\x1a\x9a\x01\n\x03Lag\x12\x14\n\x0cmin_duration\x18\x01 \x01(\x02\x12\x10\n\x08lag_time\x18\x02 \x01(\x02\x12\x11\n\tmax_speed\x18\x03 \x01(\x02\x12\x17\n\x0fspring_strength\x18\x04 \x01(\x02\x12?\n1increase_spring_strength_to_keep_target_on_screen\x18\x05 \x01(\x08:\x04true\"9\n CCitadelUserMsg_PostMatchDetails\x12\x15\n\rmatch_details\x18\x01 \x01(\x0c\"\x8d\x01\n\x19\x43\x43itadelUserMsg_ChatEvent\x12J\n\x04type\x18\x01 \x01(\x0e\x32\x14.ECitadelChatMessage:&CITADEL_CHAT_MESSAGE_UNPAUSE_COUNTDOWN\x12\x0e\n\x06values\x18\x02 \x03(\r\x12\x14\n\x0cplayer_slots\x18\x03 \x03(\x05\"\xe5\x01\n\x1a\x43\x43itadelUserMsg_HeroKilled\x12\x1b\n\x0f\x65ntindex_victim\x18\x01 \x01(\x05:\x02-1\x12\x1e\n\x12\x65ntindex_inflictor\x18\x02 \x01(\x05:\x02-1\x12\x1d\n\x11\x65ntindex_attacker\x18\x03 \x01(\x05:\x02-1\x12\x1a\n\x12\x65ntindex_assisters\x18\x04 \x03(\x05\x12\x1b\n\x0f\x65ntindex_scorer\x18\x05 \x01(\x05:\x02-1\x12\x16\n\x0erespawn_reason\x18\x06 \x01(\x05\x12\x1a\n\x12victim_team_number\x18\x07 \x01(\x05\"~\n*CCitadelEntityMsg_BreakablePropSpawnDebris\x12\x1f\n\nentity_msg\x18\x01 \x01(\x0b\x32\x0b.CEntityMsg\x12\x1f\n\ndamage_pos\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x0e\n\x06\x64\x61mage\x18\x03 \x01(\x02\"t\n\x1a\x43\x43itadelUserMsg_ReturnIdol\x12\x16\n\x0elocation_index\x18\x01 \x01(\x05\x12$\n\x0freturn_location\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x18\n\x10location_enabled\x18\x03 \x01(\x08\"d\n%CCitadelUserMsg_SetClientCameraAngles\x12\x17\n\x0bplayer_slot\x18\x01 \x01(\x05:\x02-1\x12\"\n\rcamera_angles\x18\x02 \x01(\x0b\x32\x0b.CMsgQAngle\"\x8c\x01\n\x1d\x43\x43itadelUserMessage_BulletHit\x12\x0e\n\x06shotid\x18\x01 \x01(\x05\x12\x0e\n\x06pellet\x18\x02 \x01(\x05\x12\x18\n\x0chit_entindex\x18\x03 \x01(\x05:\x02-1\x12\x1b\n\x0fweapon_entindex\x18\x04 \x01(\x05:\x02-1\x12\x14\n\x0cis_predicted\x18\x05 \x01(\x08\"_\n!CCitadelUserMessage_ObjectiveMask\x12\x1c\n\x14objective_mask_team0\x18\x02 \x01(\x04\x12\x1c\n\x14objective_mask_team1\x18\x03 \x01(\x04\"v\n#CCitadelUserMessage_ModifierApplied\x12\x1b\n\x0f\x65ntindex_caster\x18\x01 \x01(\x05:\x02-1\x12\x1b\n\x0f\x65ntindex_parent\x18\x02 \x01(\x05:\x02-1\x12\x15\n\rserial_number\x18\x03 \x01(\x05\"\xcd\x01\n\'CCitadelUserMessage_AuraModifierApplied\x12\x1b\n\x0f\x65ntindex_caster\x18\x01 \x01(\x05:\x02-1\x12\x1b\n\x0f\x65ntindex_target\x18\x02 \x01(\x05:\x02-1\x12\x18\n\x10modifier_type_id\x18\x03 \x01(\r\x12\x1e\n\x16modifier_serial_number\x18\x04 \x01(\x05\x12\x17\n\x0f\x61ura_start_time\x18\x05 \x01(\x02\x12\x15\n\raura_end_time\x18\x06 \x01(\x02\"%\n#CCitadelUserMsg_ObstructedShotFired\"\xfd\x01\n\"CCitadelUserMsg_PostProcessingAnim\x12\x1a\n\x0e\x65ntindex_owner\x18\x01 \x01(\x05:\x02-1\x12\x18\n\x10\x63lear_all_states\x18\x02 \x01(\x08\x12>\n\x05state\x18\x03 \x01(\x0e\x32\x19.PostProcessingGameStates:\x14PostProcState_Killed\x12\x12\n\nstart_time\x18\x04 \x01(\x02\x12\x14\n\x0c\x66\x61\x64\x65_in_time\x18\x05 \x01(\x02\x12\x11\n\thold_time\x18\x06 \x01(\x02\x12\x15\n\rfade_out_time\x18\x07 \x01(\x02\x12\r\n\x05scale\x18\x08 \x01(\x02\"\x98\x01\n\x1f\x43\x43itadelUserMsg_DeathReplayData\x12\x19\n\rkiller_scorer\x18\x01 \x01(\x05:\x02-1\x12\x1c\n\x10killer_inflictor\x18\x02 \x01(\x05:\x02-1\x12<\n\x0e\x64\x61mage_summary\x18\x03 \x01(\x0b\x32$.CCitadelUserMsg_RecentDamageSummary\"!\n\x1f\x43\x43itadelUserMsg_ForceShopClosed\"\xc7\x02\n&CCitadelUserMsg_PlayerLifetimeStatInfo\x12;\n\x05stats\x18\x01 \x03(\x0b\x32,.CCitadelUserMsg_PlayerLifetimeStatInfo.Stat\x12\x10\n\x08match_id\x18\x02 \x01(\x04\x12\x14\n\x0c\x65nd_of_match\x18\x03 \x01(\x08\x12\x19\n\x11is_official_match\x18\x04 \x01(\x08\x1a\x9c\x01\n\x04Stat\x12\x11\n\tstat_name\x18\x01 \x01(\t\x12\x13\n\x0bmatch_total\x18\x02 \x01(\r\x12\x16\n\x0elifetime_value\x18\x03 \x01(\r\x12\x10\n\x08priority\x18\x04 \x01(\r\x12\x19\n\x11prev_lifetime_max\x18\x05 \x01(\r\x12\x11\n\tstat_type\x18\x06 \x01(\r\x12\x14\n\x0cstat_type_id\x18\x07 \x01(\r\"V\n\x1e\x43\x43itadelUserMsg_StaminaDrained\x12\x1b\n\x0f\x65ntindex_victim\x18\x01 \x01(\x05:\x02-1\x12\x17\n\x0fstamina_drained\x18\x02 \x01(\x05\"s\n!CCitadelUserMessage_AbilityNotify\x12\x1b\n\x0f\x65ntindex_victim\x18\x01 \x01(\x05:\x02-1\x12\x1d\n\x11\x65ntindex_attacker\x18\x02 \x01(\x05:\x02-1\x12\x12\n\nability_id\x18\x03 \x01(\r\"\x92\x02\n#CCitadelUserMessage_CurrencyChanged\x12\x1e\n\x12\x65ntindex_hero_pawn\x18\x01 \x01(\x05:\x02-1\x12\x15\n\rcurrency_type\x18\x02 \x01(\x05\x12\x17\n\x0f\x63urrency_source\x18\x03 \x01(\x05\x12\r\n\x05\x64\x65lta\x18\x04 \x01(\x05\x12\x14\n\x0cnotification\x18\x05 \x01(\x08\x12\x1b\n\x0f\x65ntindex_victim\x18\x06 \x01(\x05:\x02-1\x12\x1f\n\nvictim_pos\x18\x07 \x01(\x0b\x32\x0b.CMsgVector\x12\x11\n\tplaysound\x18\x08 \x01(\x05\x12\x12\n\nability_id\x18\t \x01(\r\x12\x11\n\tnew_value\x18\n \x01(\r\"I\n\x1c\x43\x43itadelUserMessage_GameOver\x12\x14\n\x0cwinning_team\x18\x01 \x01(\x05\x12\x13\n\x0bjust_a_test\x18\x02 \x01(\x08\"\x97\x02\n&CCitadelUserMsg_GetDamageStatsResponse\x12\x13\n\x0bplayer_slot\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x62ility_name\x18\x02 \x01(\t\x12@\n\x06\x64\x61mage\x18\x03 \x01(\x0b\x32\x30.CCitadelUserMsg_GetDamageStatsResponse.StatType\x12\x41\n\x07healing\x18\x04 \x01(\x0b\x32\x30.CCitadelUserMsg_GetDamageStatsResponse.StatType\x1a=\n\x08StatType\x12\x1e\n\x12target_player_slot\x18\x01 \x03(\rB\x02\x10\x01\x12\x11\n\x05value\x18\x02 \x03(\rB\x02\x10\x01\"j\n*CCitadelUserMsg_ParticipantStartSoundEvent\x12&\n\x05\x65vent\x18\x01 \x02(\x0b\x32\x17.CMsgSosStartSoundEvent\x12\x14\n\x0cplayer_slots\x18\x02 \x03(\x05\"h\n)CCitadelUserMsg_ParticipantStopSoundEvent\x12%\n\x05\x65vent\x18\x01 \x02(\x0b\x32\x16.CMsgSosStopSoundEvent\x12\x14\n\x0cplayer_slots\x18\x02 \x03(\x05\"p\n-CCitadelUserMsg_ParticipantStopSoundEventHash\x12)\n\x05\x65vent\x18\x01 \x02(\x0b\x32\x1a.CMsgSosStopSoundEventHash\x12\x14\n\x0cplayer_slots\x18\x02 \x03(\x05\"r\n.CCitadelUserMsg_ParticipantSetSoundEventParams\x12*\n\x05\x65vent\x18\x01 \x02(\x0b\x32\x1b.CMsgSosSetSoundEventParams\x12\x14\n\x0cplayer_slots\x18\x02 \x03(\x05\"v\n0CCitadelUserMsg_ParticipantSetLibraryStackFields\x12,\n\x05\x65vent\x18\x01 \x02(\x0b\x32\x1d.CMsgSosSetLibraryStackFields\x12\x14\n\x0cplayer_slots\x18\x02 \x03(\x05\"\x84\x02\n\x1a\x43\x43itadelUserMsg_BossKilled\x12\x16\n\x0eobjective_team\x18\x01 \x01(\x05\x12\x1d\n\x15objective_mask_change\x18\x02 \x01(\x05\x12\x1f\n\rentity_killed\x18\x03 \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x1b\n\x13\x65ntity_killed_class\x18\x04 \x01(\x05\x12\x1f\n\rentity_killer\x18\x05 \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x10\n\x08gametime\x18\x06 \x01(\x02\x12\x18\n\x10\x62osses_remaining\x18\x07 \x01(\x05\x12$\n\x0f\x65ntity_position\x18\x08 \x01(\x0b\x32\x0b.CMsgVector\"m\n\x1b\x43\x43itadelUserMsg_BossDamaged\x12\x16\n\x0eobjective_team\x18\x01 \x02(\x05\x12\x14\n\x0cobjective_id\x18\x02 \x02(\x05\x12 \n\x0e\x65ntity_damaged\x18\x03 \x02(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\" \n\x1e\x43\x43itadelUserMsg_MidBossSpawned\"y\n\x1b\x43\x43itadelUserMsg_RejuvStatus\x12\x14\n\x0ckilling_team\x18\x01 \x01(\x05\x12\x1d\n\x0bplayer_pawn\x18\x02 \x02(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x11\n\tuser_team\x18\x03 \x02(\x05\x12\x12\n\nevent_type\x18\x04 \x02(\x05\"f\n\x1a\x43\x43itadelUserMsg_KillStreak\x12\x1d\n\x0bplayer_pawn\x18\x01 \x02(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x11\n\tnum_kills\x18\x02 \x02(\x05\x12\x16\n\x0eis_first_blood\x18\x03 \x02(\x08\"{\n\x17\x43\x43itadelUserMsg_TeamMsg\x12\x12\n\nevent_type\x18\x01 \x02(\x05\x12\x13\n\x0bteam_number\x18\x02 \x02(\x05\x12\x12\n\nlane_color\x18\x03 \x02(\x05\x12#\n\x11player_controller\x18\x04 \x02(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\"T\n\x1f\x43\x43itadelUserMsg_PlayerRespawned\x12\x1d\n\x0bplayer_pawn\x18\x01 \x02(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x12\n\nfacing_yaw\x18\x02 \x02(\x02\":\n\x1f\x43\x43itadelUserMsg_CallCheaterVote\x12\x17\n\x0bplayer_slot\x18\x01 \x02(\x05:\x02-1\"G\n\x1c\x43\x43itadelUserMessage_MeleeHit\x12\x18\n\x0chit_entindex\x18\x01 \x01(\x05:\x02-1\x12\r\n\x05heavy\x18\x02 \x01(\x08\"R\n CCitadelUserMsg_FlexSlotUnlocked\x12\x13\n\x0bteam_number\x18\x01 \x01(\x05\x12\x19\n\x11\x66lexslot_unlocked\x18\x02 \x01(\x05\"R\n+CCitadelUserMsg_SeasonalAchievementUnlocked\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x0f\n\x07hero_id\x18\x02 \x01(\r*\xd4\r\n\x15\x43itadelUserMessageIds\x12\x16\n\x11k_EUserMsg_Damage\x10\xac\x02\x12\x17\n\x12k_EUserMsg_MapPing\x10\xaf\x02\x12\x1b\n\x16k_EUserMsg_TeamRewards\x10\xb0\x02\x12\x1d\n\x18k_EUserMsg_AbilityFailed\x10\xb2\x02\x12\"\n\x1dk_EUserMsg_TriggerDamageFlash\x10\xb4\x02\x12 \n\x1bk_EUserMsg_AbilitiesChanged\x10\xb5\x02\x12#\n\x1ek_EUserMsg_RecentDamageSummary\x10\xb6\x02\x12$\n\x1fk_EUserMsg_SpectatorTeamChanged\x10\xb7\x02\x12\x19\n\x14k_EUserMsg_ChatWheel\x10\xb8\x02\x12\x1b\n\x16k_EUserMsg_GoldHistory\x10\xb9\x02\x12\x17\n\x12k_EUserMsg_ChatMsg\x10\xba\x02\x12\x1d\n\x18k_EUserMsg_QuickResponse\x10\xbb\x02\x12 \n\x1bk_EUserMsg_PostMatchDetails\x10\xbc\x02\x12\x19\n\x14k_EUserMsg_ChatEvent\x10\xbd\x02\x12\"\n\x1dk_EUserMsg_AbilityInterrupted\x10\xbe\x02\x12\x1a\n\x15k_EUserMsg_HeroKilled\x10\xbf\x02\x12\x1a\n\x15k_EUserMsg_ReturnIdol\x10\xc0\x02\x12%\n k_EUserMsg_SetClientCameraAngles\x10\xc1\x02\x12\x17\n\x12k_EUserMsg_MapLine\x10\xc2\x02\x12\x19\n\x14k_EUserMsg_BulletHit\x10\xc3\x02\x12\x1d\n\x18k_EUserMsg_ObjectiveMask\x10\xc4\x02\x12\x1f\n\x1ak_EUserMsg_ModifierApplied\x10\xc5\x02\x12 \n\x1bk_EUserMsg_CameraController\x10\xc6\x02\x12#\n\x1ek_EUserMsg_AuraModifierApplied\x10\xc7\x02\x12#\n\x1ek_EUserMsg_ObstructedShotFired\x10\xc9\x02\x12\"\n\x1dk_EUserMsg_AbilityLateFailure\x10\xca\x02\x12\x1b\n\x16k_EUserMsg_AbilityPing\x10\xcb\x02\x12\"\n\x1dk_EUserMsg_PostProcessingAnim\x10\xcc\x02\x12\x1f\n\x1ak_EUserMsg_DeathReplayData\x10\xcd\x02\x12&\n!k_EUserMsg_PlayerLifetimeStatInfo\x10\xce\x02\x12\x1f\n\x1ak_EUserMsg_ForceShopClosed\x10\xd0\x02\x12\x1e\n\x19k_EUserMsg_StaminaDrained\x10\xd1\x02\x12\x1d\n\x18k_EUserMsg_AbilityNotify\x10\xd2\x02\x12&\n!k_EUserMsg_GetDamageStatsResponse\x10\xd3\x02\x12*\n%k_EUserMsg_ParticipantStartSoundEvent\x10\xd4\x02\x12)\n$k_EUserMsg_ParticipantStopSoundEvent\x10\xd5\x02\x12-\n(k_EUserMsg_ParticipantStopSoundEventHash\x10\xd6\x02\x12.\n)k_EUserMsg_ParticipantSetSoundEventParams\x10\xd7\x02\x12\x30\n+k_EUserMsg_ParticipantSetLibraryStackFields\x10\xd8\x02\x12\x1f\n\x1ak_EUserMsg_CurrencyChanged\x10\xd9\x02\x12\x18\n\x13k_EUserMsg_GameOver\x10\xda\x02\x12\x1a\n\x15k_EUserMsg_BossKilled\x10\xdb\x02\x12\x1b\n\x16k_EUserMsg_BossDamaged\x10\xdc\x02\x12\x1e\n\x19k_EUserMsg_MidBossSpawned\x10\xdd\x02\x12\x1b\n\x16k_EUserMsg_RejuvStatus\x10\xde\x02\x12\x1a\n\x15k_EUserMsg_KillStreak\x10\xdf\x02\x12\x17\n\x12k_EUserMsg_TeamMsg\x10\xe0\x02\x12\x1f\n\x1ak_EUserMsg_PlayerRespawned\x10\xe1\x02\x12\x1f\n\x1ak_EUserMsg_CallCheaterVote\x10\xe2\x02\x12\x18\n\x13k_EUserMsg_MeleeHit\x10\xe3\x02\x12 \n\x1bk_EUserMsg_FlexSlotUnlocked\x10\xe4\x02\x12+\n&k_EUserMsg_SeasonalAchievementUnlocked\x10\xe5\x02*E\n\x17\x43itadelEntityMessageIds\x12*\n%k_EEntityMsg_BreakablePropSpawnDebris\x10\xf4\x03*\xe0\x01\n\x15\x43hatMsgPingMarkerInfo\x12(\n$k_EPingMarkerInfo_ShowMarkerAndSound\x10\x00\x12(\n$k_EPingMarkerInfo_HideMarkerAndSound\x10\x01\x12(\n$k_EPingMarkerInfo_ShowMarkerOnSender\x10\x02\x12$\n k_EPingMarkerInfo_OnlyShowMarker\x10\x03\x12#\n\x1fk_EPingMarkerInfo_OnlyPlaySound\x10\x04*\x88\x01\n\x0f\x43\x61meraOperation\x12\x18\n\x14k_ECameraOp_Maintain\x10\x02\x12\x18\n\x14k_ECameraOp_Approach\x10\x03\x12\x16\n\x12k_ECameraOp_Spring\x10\x04\x12\x14\n\x10k_ECameraOp_Lerp\x10\x05\x12\x13\n\x0fk_ECameraOp_Lag\x10\x06*\xc4\x01\n\x0b\x43\x61meraParam\x12\x18\n\x14k_EParam_ClearAllOps\x10\x00\x12\"\n\x1ek_EParam_ClearAllOpsForContext\x10\x01\x12\x15\n\x11k_EParam_Distance\x10\x02\x12\x10\n\x0ck_EParam_FOV\x10\x03\x12\x1b\n\x17k_EParam_TargetPosition\x10\x04\x12\x17\n\x13k_EParam_VertOffset\x10\x05\x12\x18\n\x14k_EParam_HorizOffset\x10\x06*_\n\x0f\x43\x61meraParamMode\x12\"\n\x1ek_EParamMode_AllowInOneContext\x10\x00\x12(\n$k_EParamMode_AllowInMultipleContexts\x10\x01*`\n\x0c\x43\x61meraAction\x12\x13\n\x0fk_EAction_AddOp\x10\x00\x12\x19\n\x15k_EAction_ClearAllOps\x10\x01\x12 \n\x1ck_EAction_ClearOpsForContext\x10\x02*\x99\x04\n\x13\x45\x43itadelChatMessage\x12*\n&CITADEL_CHAT_MESSAGE_UNPAUSE_COUNTDOWN\x10\x01\x12!\n\x1d\x43ITADEL_CHAT_MESSAGE_UNPAUSED\x10\x02\x12&\n\"CITADEL_CHAT_MESSAGE_AUTO_UNPAUSED\x10\x03\x12(\n$CITADEL_CHAT_MESSAGE_PAUSE_COUNTDOWN\x10\x04\x12\x1f\n\x1b\x43ITADEL_CHAT_MESSAGE_PAUSED\x10\x05\x12\"\n\x1e\x43ITADEL_CHAT_MESSAGE_YOUPAUSED\x10\x06\x12\"\n\x1e\x43ITADEL_CHAT_MESSAGE_CANTPAUSE\x10\x07\x12(\n$CITADEL_CHAT_MESSAGE_CANTUNPAUSETEAM\x10\x08\x12%\n!CITADEL_CHAT_MESSAGE_NOPAUSESLEFT\x10\t\x12%\n!CITADEL_CHAT_MESSAGE_CANTPAUSEYET\x10\n\x12*\n&CITADEL_CHAT_MESSAGE_PREGAME_COUNTDOWN\x10\x0b\x12)\n%CITADEL_CHAT_MESSAGE_NOTEAMPAUSESLEFT\x10\x0c\x12)\n%CITADEL_CHAT_MESSAGE_COMMS_RESTRICTED\x10\r*\x89\x01\n\x18PostProcessingGameStates\x12\x18\n\x14PostProcState_Killed\x10\x00\x12\x17\n\x13PostProcState_Black\x10\x01\x12\x19\n\x15PostProcState_Blinded\x10\x02\x12\x1f\n\x1bPostProcState_ShivPossessed\x10\x03')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'citadel_usermessages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE_STATTYPE.fields_by_name['target_player_slot']._options = None
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE_STATTYPE.fields_by_name['target_player_slot']._serialized_options = b'\020\001'
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE_STATTYPE.fields_by_name['value']._options = None
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE_STATTYPE.fields_by_name['value']._serialized_options = b'\020\001'
  _CITADELUSERMESSAGEIDS._serialized_start=10198
  _CITADELUSERMESSAGEIDS._serialized_end=11946
  _CITADELENTITYMESSAGEIDS._serialized_start=11948
  _CITADELENTITYMESSAGEIDS._serialized_end=12017
  _CHATMSGPINGMARKERINFO._serialized_start=12020
  _CHATMSGPINGMARKERINFO._serialized_end=12244
  _CAMERAOPERATION._serialized_start=12247
  _CAMERAOPERATION._serialized_end=12383
  _CAMERAPARAM._serialized_start=12386
  _CAMERAPARAM._serialized_end=12582
  _CAMERAPARAMMODE._serialized_start=12584
  _CAMERAPARAMMODE._serialized_end=12679
  _CAMERAACTION._serialized_start=12681
  _CAMERAACTION._serialized_end=12777
  _ECITADELCHATMESSAGE._serialized_start=12780
  _ECITADELCHATMESSAGE._serialized_end=13317
  _POSTPROCESSINGGAMESTATES._serialized_start=13320
  _POSTPROCESSINGGAMESTATES._serialized_end=13457
  _CUSERMESSAGEEMPTY._serialized_start=105
  _CUSERMESSAGEEMPTY._serialized_end=139
  _CCITADELUSERMESSAGE_DAMAGE._serialized_start=142
  _CCITADELUSERMESSAGE_DAMAGE._serialized_end=741
  _PINGCOMMONDATA._serialized_start=744
  _PINGCOMMONDATA._serialized_end=957
  _CCITADELUSERMSG_MAPPING._serialized_start=960
  _CCITADELUSERMSG_MAPPING._serialized_end=1271
  _CCITADELUSERMSG_PINGWHEEL._serialized_start=1273
  _CCITADELUSERMSG_PINGWHEEL._serialized_end=1366
  _CCITADELUSERMSG_ABILITYPING._serialized_start=1369
  _CCITADELUSERMSG_ABILITYPING._serialized_end=1578
  _CCITADELUSERMSG_QUICKRESPONSE._serialized_start=1581
  _CCITADELUSERMSG_QUICKRESPONSE._serialized_end=1784
  _CCITADELUSERMSG_MAPLINE._serialized_start=1786
  _CCITADELUSERMSG_MAPLINE._serialized_end=1874
  _CCITADELUSERMSG_TEAMREWARDS._serialized_start=1876
  _CCITADELUSERMSG_TEAMREWARDS._serialized_end=1947
  _CCITADELUSERMSG_TRIGGERDAMAGEFLASH._serialized_start=1950
  _CCITADELUSERMSG_TRIGGERDAMAGEFLASH._serialized_end=2190
  _CCITADELUSERMSG_ABILITIESCHANGED._serialized_start=2193
  _CCITADELUSERMSG_ABILITIESCHANGED._serialized_end=2455
  _CCITADELUSERMSG_ABILITIESCHANGED_CHANGE._serialized_start=2352
  _CCITADELUSERMSG_ABILITIESCHANGED_CHANGE._serialized_end=2455
  _CCITADELUSERMSG_ABILITYINTERRUPTED._serialized_start=2458
  _CCITADELUSERMSG_ABILITYINTERRUPTED._serialized_end=2650
  _CCITADELUSERMSG_ABILITYLATEFAILURE._serialized_start=2652
  _CCITADELUSERMSG_ABILITYLATEFAILURE._serialized_end=2769
  _CCITADELUSERMSG_RECENTDAMAGESUMMARY._serialized_start=2772
  _CCITADELUSERMSG_RECENTDAMAGESUMMARY._serialized_end=3418
  _CCITADELUSERMSG_RECENTDAMAGESUMMARY_DAMAGERECORD._serialized_start=3070
  _CCITADELUSERMSG_RECENTDAMAGESUMMARY_DAMAGERECORD._serialized_end=3270
  _CCITADELUSERMSG_RECENTDAMAGESUMMARY_MODIFIERRECORD._serialized_start=3273
  _CCITADELUSERMSG_RECENTDAMAGESUMMARY_MODIFIERRECORD._serialized_end=3418
  _CCITADELUSERMSG_SPECTATORTEAMCHANGED._serialized_start=3420
  _CCITADELUSERMSG_SPECTATORTEAMCHANGED._serialized_end=3478
  _CCITADELUSERMSG_CHATWHEEL._serialized_start=3481
  _CCITADELUSERMSG_CHATWHEEL._serialized_end=3697
  _CCITADELUSERMSG_CHATMSG._serialized_start=3700
  _CCITADELUSERMSG_CHATMSG._serialized_end=3840
  _CCITADELUSERMSG_GOLDHISTORY._serialized_start=3843
  _CCITADELUSERMSG_GOLDHISTORY._serialized_end=4138
  _CCITADELUSERMSG_GOLDHISTORY_GOLDRECORD._serialized_start=3970
  _CCITADELUSERMSG_GOLDHISTORY_GOLDRECORD._serialized_end=4037
  _CCITADELUSERMSG_GOLDHISTORY_MINUTERECORD._serialized_start=4039
  _CCITADELUSERMSG_GOLDHISTORY_MINUTERECORD._serialized_end=4138
  _CCITADELUSERMSG_CAMERACONTROLLER._serialized_start=4141
  _CCITADELUSERMSG_CAMERACONTROLLER._serialized_end=5479
  _CCITADELUSERMSG_CAMERACONTROLLER_MAINTAIN._serialized_start=4781
  _CCITADELUSERMSG_CAMERACONTROLLER_MAINTAIN._serialized_end=4812
  _CCITADELUSERMSG_CAMERACONTROLLER_APPROACH._serialized_start=4815
  _CCITADELUSERMSG_CAMERACONTROLLER_APPROACH._serialized_end=5011
  _CCITADELUSERMSG_CAMERACONTROLLER_SPRING._serialized_start=5014
  _CCITADELUSERMSG_CAMERACONTROLLER_SPRING._serialized_end=5156
  _CCITADELUSERMSG_CAMERACONTROLLER_LERP._serialized_start=5159
  _CCITADELUSERMSG_CAMERACONTROLLER_LERP._serialized_end=5322
  _CCITADELUSERMSG_CAMERACONTROLLER_LAG._serialized_start=5325
  _CCITADELUSERMSG_CAMERACONTROLLER_LAG._serialized_end=5479
  _CCITADELUSERMSG_POSTMATCHDETAILS._serialized_start=5481
  _CCITADELUSERMSG_POSTMATCHDETAILS._serialized_end=5538
  _CCITADELUSERMSG_CHATEVENT._serialized_start=5541
  _CCITADELUSERMSG_CHATEVENT._serialized_end=5682
  _CCITADELUSERMSG_HEROKILLED._serialized_start=5685
  _CCITADELUSERMSG_HEROKILLED._serialized_end=5914
  _CCITADELENTITYMSG_BREAKABLEPROPSPAWNDEBRIS._serialized_start=5916
  _CCITADELENTITYMSG_BREAKABLEPROPSPAWNDEBRIS._serialized_end=6042
  _CCITADELUSERMSG_RETURNIDOL._serialized_start=6044
  _CCITADELUSERMSG_RETURNIDOL._serialized_end=6160
  _CCITADELUSERMSG_SETCLIENTCAMERAANGLES._serialized_start=6162
  _CCITADELUSERMSG_SETCLIENTCAMERAANGLES._serialized_end=6262
  _CCITADELUSERMESSAGE_BULLETHIT._serialized_start=6265
  _CCITADELUSERMESSAGE_BULLETHIT._serialized_end=6405
  _CCITADELUSERMESSAGE_OBJECTIVEMASK._serialized_start=6407
  _CCITADELUSERMESSAGE_OBJECTIVEMASK._serialized_end=6502
  _CCITADELUSERMESSAGE_MODIFIERAPPLIED._serialized_start=6504
  _CCITADELUSERMESSAGE_MODIFIERAPPLIED._serialized_end=6622
  _CCITADELUSERMESSAGE_AURAMODIFIERAPPLIED._serialized_start=6625
  _CCITADELUSERMESSAGE_AURAMODIFIERAPPLIED._serialized_end=6830
  _CCITADELUSERMSG_OBSTRUCTEDSHOTFIRED._serialized_start=6832
  _CCITADELUSERMSG_OBSTRUCTEDSHOTFIRED._serialized_end=6869
  _CCITADELUSERMSG_POSTPROCESSINGANIM._serialized_start=6872
  _CCITADELUSERMSG_POSTPROCESSINGANIM._serialized_end=7125
  _CCITADELUSERMSG_DEATHREPLAYDATA._serialized_start=7128
  _CCITADELUSERMSG_DEATHREPLAYDATA._serialized_end=7280
  _CCITADELUSERMSG_FORCESHOPCLOSED._serialized_start=7282
  _CCITADELUSERMSG_FORCESHOPCLOSED._serialized_end=7315
  _CCITADELUSERMSG_PLAYERLIFETIMESTATINFO._serialized_start=7318
  _CCITADELUSERMSG_PLAYERLIFETIMESTATINFO._serialized_end=7645
  _CCITADELUSERMSG_PLAYERLIFETIMESTATINFO_STAT._serialized_start=7489
  _CCITADELUSERMSG_PLAYERLIFETIMESTATINFO_STAT._serialized_end=7645
  _CCITADELUSERMSG_STAMINADRAINED._serialized_start=7647
  _CCITADELUSERMSG_STAMINADRAINED._serialized_end=7733
  _CCITADELUSERMESSAGE_ABILITYNOTIFY._serialized_start=7735
  _CCITADELUSERMESSAGE_ABILITYNOTIFY._serialized_end=7850
  _CCITADELUSERMESSAGE_CURRENCYCHANGED._serialized_start=7853
  _CCITADELUSERMESSAGE_CURRENCYCHANGED._serialized_end=8127
  _CCITADELUSERMESSAGE_GAMEOVER._serialized_start=8129
  _CCITADELUSERMESSAGE_GAMEOVER._serialized_end=8202
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE._serialized_start=8205
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE._serialized_end=8484
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE_STATTYPE._serialized_start=8423
  _CCITADELUSERMSG_GETDAMAGESTATSRESPONSE_STATTYPE._serialized_end=8484
  _CCITADELUSERMSG_PARTICIPANTSTARTSOUNDEVENT._serialized_start=8486
  _CCITADELUSERMSG_PARTICIPANTSTARTSOUNDEVENT._serialized_end=8592
  _CCITADELUSERMSG_PARTICIPANTSTOPSOUNDEVENT._serialized_start=8594
  _CCITADELUSERMSG_PARTICIPANTSTOPSOUNDEVENT._serialized_end=8698
  _CCITADELUSERMSG_PARTICIPANTSTOPSOUNDEVENTHASH._serialized_start=8700
  _CCITADELUSERMSG_PARTICIPANTSTOPSOUNDEVENTHASH._serialized_end=8812
  _CCITADELUSERMSG_PARTICIPANTSETSOUNDEVENTPARAMS._serialized_start=8814
  _CCITADELUSERMSG_PARTICIPANTSETSOUNDEVENTPARAMS._serialized_end=8928
  _CCITADELUSERMSG_PARTICIPANTSETLIBRARYSTACKFIELDS._serialized_start=8930
  _CCITADELUSERMSG_PARTICIPANTSETLIBRARYSTACKFIELDS._serialized_end=9048
  _CCITADELUSERMSG_BOSSKILLED._serialized_start=9051
  _CCITADELUSERMSG_BOSSKILLED._serialized_end=9311
  _CCITADELUSERMSG_BOSSDAMAGED._serialized_start=9313
  _CCITADELUSERMSG_BOSSDAMAGED._serialized_end=9422
  _CCITADELUSERMSG_MIDBOSSSPAWNED._serialized_start=9424
  _CCITADELUSERMSG_MIDBOSSSPAWNED._serialized_end=9456
  _CCITADELUSERMSG_REJUVSTATUS._serialized_start=9458
  _CCITADELUSERMSG_REJUVSTATUS._serialized_end=9579
  _CCITADELUSERMSG_KILLSTREAK._serialized_start=9581
  _CCITADELUSERMSG_KILLSTREAK._serialized_end=9683
  _CCITADELUSERMSG_TEAMMSG._serialized_start=9685
  _CCITADELUSERMSG_TEAMMSG._serialized_end=9808
  _CCITADELUSERMSG_PLAYERRESPAWNED._serialized_start=9810
  _CCITADELUSERMSG_PLAYERRESPAWNED._serialized_end=9894
  _CCITADELUSERMSG_CALLCHEATERVOTE._serialized_start=9896
  _CCITADELUSERMSG_CALLCHEATERVOTE._serialized_end=9954
  _CCITADELUSERMESSAGE_MELEEHIT._serialized_start=9956
  _CCITADELUSERMESSAGE_MELEEHIT._serialized_end=10027
  _CCITADELUSERMSG_FLEXSLOTUNLOCKED._serialized_start=10029
  _CCITADELUSERMSG_FLEXSLOTUNLOCKED._serialized_end=10111
  _CCITADELUSERMSG_SEASONALACHIEVEMENTUNLOCKED._serialized_start=10113
  _CCITADELUSERMSG_SEASONALACHIEVEMENTUNLOCKED._serialized_end=10195
# @@protoc_insertion_point(module_scope)
