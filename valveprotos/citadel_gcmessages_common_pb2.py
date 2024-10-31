# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: citadel_gcmessages_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_pb2 as steammessages__pb2
import gcsdk_gcmessages_pb2 as gcsdk__gcmessages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63itadel_gcmessages_common.proto\x1a\x13steammessages.proto\x1a\x16gcsdk_gcmessages.proto\"\xfc\x03\n\x0f\x43SOCitadelLobby\x12\x10\n\x08lobby_id\x18\x01 \x01(\x04\x12\x10\n\x08match_id\x18\x02 \x01(\x04\x12\x43\n\nmatch_mode\x18\x03 \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\x12@\n\tgame_mode\x18\x04 \x01(\x0e\x32\x11.ECitadelGameMode:\x1ak_ECitadelGameMode_Invalid\x12\x1d\n\x15\x63ompatibility_version\x18\x05 \x01(\r\x12\'\n\x0e\x65xtra_messages\x18\x06 \x03(\x0b\x32\x0f.CExtraMsgBlock\x12\x17\n\x0fserver_steam_id\x18\x07 \x01(\x06\x12\x44\n\x0cserver_state\x18\x08 \x01(\x0e\x32\x12.ELobbyServerState:\x1ak_eLobbyServerState_Assign\x12\x16\n\x0eudp_connect_ip\x18\t \x01(\r\x12\x18\n\x10udp_connect_port\x18\n \x01(\r\x12\x13\n\x0bsdr_address\x18\x0c \x01(\x0c\x12\x16\n\x0eserver_version\x18\r \x01(\r\x12\x17\n\x0fsafe_to_abandon\x18\x0e \x01(\x08\x12\x1f\n\x17match_punishes_abandons\x18\x0f \x01(\x08\"\x90\x01\n\x1a\x43LobbyData_PostMatchSurvey\x12\x39\n\x07surveys\x18\x01 \x03(\x0b\x32(.CLobbyData_PostMatchSurvey.PlayerSurvey\x1a\x37\n\x0cPlayerSurvey\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x13\n\x0bquestion_id\x18\x02 \x01(\r\"\x82\x01\n\x1a\x43MsgHeroSelectionMatchInfo\x12\x39\n\x0fhero_selections\x18\x01 \x03(\x0b\x32 .CMsgHeroSelectionMatchInfo.Hero\x1a)\n\x04Hero\x12\x0f\n\x07hero_id\x18\x01 \x01(\r\x12\x10\n\x08priority\x18\x02 \x01(\r\"\x82\x03\n\x19\x43MsgStartFindingMatchInfo\x12\x19\n\x11server_search_key\x18\x01 \x01(\t\x12\x1d\n\x15server_command_string\x18\x02 \x01(\t\x12\x43\n\nmatch_mode\x18\x03 \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\x12@\n\tgame_mode\x18\x05 \x01(\x0e\x32\x11.ECitadelGameMode:\x1ak_ECitadelGameMode_Invalid\x12\x12\n\nsolo_match\x18\x06 \x01(\x08\x12L\n\x0e\x62ot_difficulty\x18\x07 \x01(\x0e\x32\x16.ECitadelBotDifficulty:\x1ck_ECitadelBotDifficulty_None\x12\x42\n\x0bregion_mode\x18\x08 \x01(\x0e\x32\x13.ECitadelRegionMode:\x18k_ECitadelRegionMode_ROW\"\xa2\x02\n\x18\x43MsgAnyToGCReportAsserts\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x38\n\x07\x61sserts\x18\x02 \x03(\x0b\x32\'.CMsgAnyToGCReportAsserts.TrackedAssert\x1a\xba\x01\n\rTrackedAssert\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x13\n\x0bline_number\x18\x02 \x01(\r\x12\x12\n\nsample_msg\x18\x03 \x01(\t\x12\x14\n\x0csample_stack\x18\x04 \x01(\t\x12\x13\n\x0btimes_fired\x18\x05 \x01(\r\x12\x15\n\rfunction_name\x18\x06 \x01(\t\x12\x11\n\tcondition\x18\x07 \x01(\t\x12\x19\n\x11total_times_fired\x18\x08 \x01(\r\"3\n CMsgAnyToGCReportAssertsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"R\n\x19\x43MsgRegionPingTimesClient\x12\x1d\n\x11\x64\x61ta_center_codes\x18\x01 \x03(\x07\x42\x02\x10\x01\x12\x16\n\nping_times\x18\x02 \x03(\rB\x02\x10\x01\"\x92\x0f\n\x0f\x43SOCitadelParty\x12\x10\n\x08party_id\x18\x01 \x01(\x04\x12(\n\x07members\x18\x02 \x03(\x0b\x32\x17.CSOCitadelParty.Member\x12(\n\x07invites\x18\x03 \x03(\x0b\x32\x17.CSOCitadelParty.Invite\x12\x1a\n\x12\x64\x65v_server_command\x18\x04 \x01(\t\x12\x31\n\x0cleft_members\x18\x05 \x03(\x0b\x32\x1b.CSOCitadelParty.LeftMember\x12\x11\n\tjoin_code\x18\x06 \x01(\x04\x12L\n\x0e\x62ot_difficulty\x18\x07 \x01(\x0e\x32\x16.ECitadelBotDifficulty:\x1ck_ECitadelBotDifficulty_None\x12\x43\n\nmatch_mode\x18\t \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\x12@\n\tgame_mode\x18\n \x01(\x0e\x32\x11.ECitadelGameMode:\x1ak_ECitadelGameMode_Invalid\x12\x1f\n\x17match_making_start_time\x18\x0b \x01(\r\x12\x19\n\x11server_search_key\x18\x0c \x01(\t\x12!\n\x19is_high_skill_range_party\x18\r \x01(\x08\x12\x36\n\tchat_mode\x18\x0e \x01(\x0e\x32\x1a.CSOCitadelParty.EChatMode:\x07k_eNone\x12\x42\n\x0bregion_mode\x18\x0f \x01(\x0e\x32\x13.ECitadelRegionMode:\x18k_ECitadelRegionMode_ROW\x12\x18\n\x10is_private_lobby\x18\x10 \x01(\x08\x12\x45\n\x16private_lobby_settings\x18\x11 \x01(\x0b\x32%.CSOCitadelParty.PrivateLobbySettings\x1a>\n\x10PrivateLobbySlot\x12\x0f\n\x07slot_id\x18\x01 \x01(\r\x12\x19\n\x11player_account_id\x18\x02 \x01(\r\x1a!\n\x0cServerRegion\x12\x11\n\tregion_id\x18\x01 \x01(\r\x1a\xa8\x02\n\x14PrivateLobbySettings\x12\x17\n\x0fmin_roster_size\x18\x01 \x01(\r\x12\x36\n\x0bmatch_slots\x18\x02 \x03(\x0b\x32!.CSOCitadelParty.PrivateLobbySlot\x12\x17\n\x0frandomize_lanes\x18\x03 \x01(\x08\x12\x15\n\rserver_region\x18\x04 \x01(\r\x12\x1b\n\x13is_publicly_visible\x18\x06 \x01(\x08\x12\x16\n\x0e\x63heats_enabled\x18\x07 \x01(\x08\x12\x38\n\x11\x61vailable_regions\x18\x08 \x03(\x0b\x32\x1d.CSOCitadelParty.ServerRegion\x12 \n\x18\x64uplicate_heroes_enabled\x18\t \x01(\x08\x1a\x82\x03\n\x06Member\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x14\n\x0cpersona_name\x18\x02 \x01(\t\x12\x14\n\x0crights_flags\x18\x03 \x01(\r\x12\x10\n\x08is_ready\x18\x04 \x01(\x08\x12G\n\x0bplayer_type\x18\x05 \x01(\x0e\x32\x1c.CSOCitadelParty.EPlayerType:\x14k_ePlayerType_Player\x12\x1d\n\x15\x63ompatibility_version\x18\x06 \x01(\r\x12\x32\n\x08platform\x18\x07 \x01(\x0e\x32\x0c.EGCPlatform:\x12k_eGCPlatform_None\x12\x0c\n\x04team\x18\x08 \x01(\r\x12\x30\n\x0bhero_roster\x18\t \x01(\x0b\x32\x1b.CMsgHeroSelectionMatchInfo\x12\x13\n\x0bpermissions\x18\n \x01(\x04\x12\x1b\n\x13new_player_progress\x18\x0b \x01(\x04\x12\x18\n\x0cowned_heroes\x18\x0c \x03(\rB\x02\x10\x01\x1a\x7f\n\nLeftMember\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x14\n\x0crights_flags\x18\x02 \x01(\r\x12G\n\x0bplayer_type\x18\x03 \x01(\x0e\x32\x1c.CSOCitadelParty.EPlayerType:\x14k_ePlayerType_Player\x1a\x46\n\x06Invite\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x14\n\x0cpersona_name\x18\x02 \x01(\t\x12\x12\n\ninvited_by\x18\x03 \x01(\r\"G\n\rEMemberRights\x12\x19\n\x15k_eMemberRights_Admin\x10\x01\x12\x1b\n\x17k_eMemberRights_Creator\x10\x02\"D\n\x0b\x45PlayerType\x12\x18\n\x14k_ePlayerType_Player\x10\x00\x12\x1b\n\x17k_ePlayerType_Spectator\x10\x01\";\n\tEChatMode\x12\x0b\n\x07k_eNone\x10\x00\x12\x10\n\x0ck_ePartyChat\x10\x01\x12\x0f\n\x0bk_eTeamChat\x10\x02\"\xc1\x02\n\x18\x43MsgMatchPlayerPathsData\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x12\n\ninterval_s\x18\x02 \x01(\x02\x12\x14\n\x0cx_resolution\x18\x03 \x01(\r\x12\x14\n\x0cy_resolution\x18\x04 \x01(\r\x12-\n\x05paths\x18\x05 \x03(\x0b\x32\x1e.CMsgMatchPlayerPathsData.Path\x1a\xa4\x01\n\x04Path\x12\x13\n\x0bplayer_slot\x18\x01 \x01(\r\x12\r\n\x05x_min\x18\x02 \x01(\x02\x12\r\n\x05y_min\x18\x03 \x01(\x02\x12\r\n\x05x_max\x18\x04 \x01(\x02\x12\r\n\x05y_max\x18\x05 \x01(\x02\x12\x11\n\x05x_pos\x18\x06 \x03(\rB\x02\x10\x01\x12\x11\n\x05y_pos\x18\x07 \x03(\rB\x02\x10\x01\x12\x11\n\x05\x61live\x18\x08 \x03(\x08\x42\x02\x10\x01\x12\x12\n\x06health\x18\t \x03(\rB\x02\x10\x01\"\xce\x05\n\x1b\x43MsgMatchPlayerDamageMatrix\x12\x41\n\x0e\x64\x61mage_dealers\x18\x01 \x03(\x0b\x32).CMsgMatchPlayerDamageMatrix.DamageDealer\x12\x19\n\rsample_time_s\x18\x02 \x03(\rB\x02\x10\x01\x12\x42\n\x0esource_details\x18\x03 \x01(\x0b\x32*.CMsgMatchPlayerDamageMatrix.SourceDetails\x1a@\n\x0e\x44\x61mageToPlayer\x12\x1a\n\x12target_player_slot\x18\x01 \x01(\r\x12\x12\n\x06\x64\x61mage\x18\x02 \x03(\rB\x02\x10\x01\x1at\n\x0c\x44\x61mageSource\x12\x46\n\x11\x64\x61mage_to_players\x18\x02 \x03(\x0b\x32+.CMsgMatchPlayerDamageMatrix.DamageToPlayer\x12\x1c\n\x14source_details_index\x18\x04 \x01(\r\x1am\n\x0c\x44\x61mageDealer\x12\x1a\n\x12\x64\x65\x61ler_player_slot\x18\x01 \x01(\r\x12\x41\n\x0e\x64\x61mage_sources\x18\x02 \x03(\x0b\x32).CMsgMatchPlayerDamageMatrix.DamageSource\x1a\x63\n\rSourceDetails\x12=\n\tstat_type\x18\x01 \x03(\x0e\x32&.CMsgMatchPlayerDamageMatrix.EStatTypeB\x02\x10\x01\x12\x13\n\x0bsource_name\x18\x02 \x03(\t\"\x80\x01\n\tEStatType\x12\x12\n\x0ek_eType_Damage\x10\x00\x12\x13\n\x0fk_eType_Healing\x10\x01\x12\x19\n\x15k_eType_HealPrevented\x10\x02\x12\x15\n\x11k_eType_Mitigated\x10\x03\x12\x18\n\x14k_eType_LethalDamage\x10\x04\"\x9a$\n\x19\x43MsgMatchMetaDataContents\x12\x38\n\nmatch_info\x18\x02 \x01(\x0b\x32$.CMsgMatchMetaDataContents.MatchInfo\x1a+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x1a\xc4\x01\n\x06\x44\x65\x61ths\x12\x13\n\x0bgame_time_s\x18\x01 \x01(\r\x12\x1a\n\x12killer_player_slot\x18\t \x01(\r\x12\x36\n\tdeath_pos\x18\n \x01(\x0b\x32#.CMsgMatchMetaDataContents.Position\x12\x37\n\nkiller_pos\x18\x0b \x01(\x0b\x32#.CMsgMatchMetaDataContents.Position\x12\x18\n\x10\x64\x65\x61th_duration_s\x18\x0c \x01(\r\x1a\x80\x01\n\x05Items\x12\x13\n\x0bgame_time_s\x18\x01 \x01(\r\x12\x0f\n\x07item_id\x18\x02 \x01(\r\x12\x12\n\nupgrade_id\x18\x03 \x01(\r\x12\x13\n\x0bsold_time_s\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\x12\x19\n\x11imbued_ability_id\x18\x06 \x01(\r\x1a\x41\n\x04Ping\x12\x11\n\tping_type\x18\x01 \x01(\r\x12\x11\n\tping_data\x18\x02 \x01(\r\x12\x13\n\x0bgame_time_s\x18\x03 \x01(\r\x1a\x90\x01\n\nGoldSource\x12\x42\n\x06source\x18\x01 \x01(\x0e\x32&.CMsgMatchMetaDataContents.EGoldSource:\nk_ePlayers\x12\r\n\x05kills\x18\x02 \x01(\r\x12\x0e\n\x06\x64\x61mage\x18\x03 \x01(\r\x12\x0c\n\x04gold\x18\x04 \x01(\r\x12\x11\n\tgold_orbs\x18\x05 \x01(\r\x1a.\n\x12\x43ustomUserStatInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x1a+\n\x0e\x43ustomUserStat\x12\r\n\x05value\x18\x02 \x01(\r\x12\n\n\x02id\x18\x03 \x01(\r\x1a\xb7\x08\n\x0bPlayerStats\x12\x14\n\x0ctime_stamp_s\x18\x01 \x01(\r\x12\x11\n\tnet_worth\x18\x02 \x01(\r\x12\x13\n\x0bgold_player\x18\x03 \x01(\r\x12\x18\n\x10gold_player_orbs\x18\x04 \x01(\r\x12\x1c\n\x14gold_lane_creep_orbs\x18\x05 \x01(\r\x12\x1f\n\x17gold_neutral_creep_orbs\x18\x06 \x01(\r\x12\x11\n\tgold_boss\x18\x07 \x01(\r\x12\x15\n\rgold_boss_orb\x18\x08 \x01(\r\x12\x15\n\rgold_treasure\x18\t \x01(\r\x12\x13\n\x0bgold_denied\x18\n \x01(\r\x12\x17\n\x0fgold_death_loss\x18\x0b \x01(\r\x12\x17\n\x0fgold_lane_creep\x18\x0c \x01(\r\x12\x1a\n\x12gold_neutral_creep\x18\r \x01(\r\x12\r\n\x05kills\x18\x0e \x01(\r\x12\x0e\n\x06\x64\x65\x61ths\x18\x0f \x01(\r\x12\x0f\n\x07\x61ssists\x18\x10 \x01(\r\x12\x13\n\x0b\x63reep_kills\x18\x11 \x01(\r\x12\x15\n\rneutral_kills\x18\x12 \x01(\r\x12\x17\n\x0fpossible_creeps\x18\x13 \x01(\r\x12\x14\n\x0c\x63reep_damage\x18\x14 \x01(\r\x12\x15\n\rplayer_damage\x18\x15 \x01(\r\x12\x16\n\x0eneutral_damage\x18\x16 \x01(\r\x12\x13\n\x0b\x62oss_damage\x18\x17 \x01(\r\x12\x0e\n\x06\x64\x65nies\x18\x18 \x01(\r\x12\x16\n\x0eplayer_healing\x18\x19 \x01(\r\x12\x16\n\x0e\x61\x62ility_points\x18\x1a \x01(\r\x12\x14\n\x0cself_healing\x18\x1b \x01(\r\x12\x1b\n\x13player_damage_taken\x18\x1c \x01(\r\x12\x12\n\nmax_health\x18\x1d \x01(\r\x12\x14\n\x0cweapon_power\x18\x1e \x01(\r\x12\x12\n\ntech_power\x18\x1f \x01(\r\x12\x11\n\tshots_hit\x18  \x01(\r\x12\x14\n\x0cshots_missed\x18! \x01(\r\x12\x17\n\x0f\x64\x61mage_absorbed\x18\" \x01(\r\x12\x1b\n\x13\x61\x62sorption_provided\x18# \x01(\r\x12\x18\n\x10hero_bullets_hit\x18$ \x01(\r\x12\x1d\n\x15hero_bullets_hit_crit\x18% \x01(\r\x12\x16\n\x0eheal_prevented\x18& \x01(\r\x12\x11\n\theal_lost\x18\' \x01(\r\x12;\n\x0cgold_sources\x18( \x03(\x0b\x32%.CMsgMatchMetaDataContents.GoldSource\x12\x44\n\x11\x63ustom_user_stats\x18) \x03(\x0b\x32).CMsgMatchMetaDataContents.CustomUserStat\x12\x18\n\x10\x64\x61mage_mitigated\x18* \x01(\r\x12\r\n\x05level\x18+ \x01(\r\x1a\x38\n\x0b\x41\x62ilityStat\x12\x12\n\nability_id\x18\x01 \x01(\r\x12\x15\n\rability_value\x18\x02 \x01(\r\x1a\x45\n\nBookReward\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\r\x12\x11\n\txp_amount\x18\x02 \x01(\r\x12\x13\n\x0bstarting_xp\x18\x03 \x01(\r\x1a\xd8\x05\n\x07Players\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x13\n\x0bplayer_slot\x18\x02 \x01(\r\x12\x38\n\rdeath_details\x18\x03 \x03(\x0b\x32!.CMsgMatchMetaDataContents.Deaths\x12/\n\x05items\x18\x04 \x03(\x0b\x32 .CMsgMatchMetaDataContents.Items\x12\x35\n\x05stats\x18\x05 \x03(\x0b\x32&.CMsgMatchMetaDataContents.PlayerStats\x12;\n\x04team\x18\x06 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\r\n\x05kills\x18\x08 \x01(\r\x12\x0e\n\x06\x64\x65\x61ths\x18\t \x01(\r\x12\x0f\n\x07\x61ssists\x18\n \x01(\r\x12\x11\n\tnet_worth\x18\x0b \x01(\r\x12\x0f\n\x07hero_id\x18\x0c \x01(\r\x12\x11\n\tlast_hits\x18\r \x01(\r\x12\x0e\n\x06\x64\x65nies\x18\x0e \x01(\r\x12\x16\n\x0e\x61\x62ility_points\x18\x0f \x01(\r\x12\r\n\x05party\x18\x10 \x01(\r\x12\x15\n\rassigned_lane\x18\x11 \x01(\r\x12\r\n\x05level\x18\x12 \x01(\r\x12.\n\x05pings\x18\x13 \x03(\x0b\x32\x1f.CMsgMatchMetaDataContents.Ping\x12=\n\rability_stats\x18\x14 \x03(\x0b\x32&.CMsgMatchMetaDataContents.AbilityStat\x12\x1b\n\x0fstats_type_stat\x18\x15 \x03(\x02\x42\x02\x10\x01\x12;\n\x0c\x62ook_rewards\x18\x16 \x03(\x0b\x32%.CMsgMatchMetaDataContents.BookReward\x12\x1c\n\x14\x61\x62\x61ndon_match_time_s\x18\x17 \x01(\r\x12\x1a\n\x12ranked_badge_level\x18\x18 \x01(\r\x1a\x8f\x03\n\tObjective\x12O\n\x13legacy_objective_id\x18\x01 \x01(\x0e\x32\x12.ECitadelObjective:\x1ek_eCitadelObjective_Team0_Core\x12\x18\n\x10\x64\x65stroyed_time_s\x18\x02 \x01(\r\x12\x14\n\x0c\x63reep_damage\x18\x04 \x01(\r\x12\x1e\n\x16\x63reep_damage_mitigated\x18\x05 \x01(\r\x12\x15\n\rplayer_damage\x18\x06 \x01(\r\x12\x1f\n\x17player_damage_mitigated\x18\x07 \x01(\r\x12\x1b\n\x13\x66irst_damage_time_s\x18\x08 \x01(\r\x12O\n\x11team_objective_id\x18\t \x01(\x0e\x32\x16.ECitadelTeamObjective:\x1ck_eCitadelTeamObjective_Core\x12;\n\x04team\x18\n \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x1a\xac\x01\n\x07MidBoss\x12\x42\n\x0bteam_killed\x18\x01 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\x43\n\x0cteam_claimed\x18\x02 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\x18\n\x10\x64\x65stroyed_time_s\x18\x03 \x01(\r\x1aK\n\x05Pause\x12\x13\n\x0bgame_time_s\x18\x01 \x01(\r\x12\x18\n\x10pause_duration_s\x18\x02 \x01(\r\x12\x13\n\x0bplayer_slot\x18\x03 \x01(\r\x1a>\n\x12WatchedDeathReplay\x12\x13\n\x0bgame_time_s\x18\x01 \x01(\r\x12\x13\n\x0bplayer_slot\x18\x02 \x01(\r\x1a\xf2\x07\n\tMatchInfo\x12\x12\n\nduration_s\x18\x01 \x01(\r\x12S\n\rmatch_outcome\x18\x02 \x01(\x0e\x32(.CMsgMatchMetaDataContents.EMatchOutcome:\x12k_eOutcome_TeamWin\x12\x43\n\x0cwinning_team\x18\x03 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\x33\n\x07players\x18\x04 \x03(\x0b\x32\".CMsgMatchMetaDataContents.Players\x12\x12\n\nstart_time\x18\x05 \x01(\r\x12\x10\n\x08match_id\x18\x06 \x01(\x04\x12\x1e\n\x16legacy_objectives_mask\x18\x08 \x01(\r\x12@\n\tgame_mode\x18\t \x01(\x0e\x32\x11.ECitadelGameMode:\x1ak_ECitadelGameMode_Invalid\x12\x43\n\nmatch_mode\x18\n \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\x12\x38\n\nobjectives\x18\x0b \x03(\x0b\x32$.CMsgMatchMetaDataContents.Objective\x12.\n\x0bmatch_paths\x18\x0c \x01(\x0b\x32\x19.CMsgMatchPlayerPathsData\x12\x33\n\rdamage_matrix\x18\r \x01(\x0b\x32\x1c.CMsgMatchPlayerDamageMatrix\x12\x36\n\x0cmatch_pauses\x18\x0e \x03(\x0b\x32 .CMsgMatchMetaDataContents.Pause\x12H\n\x11\x63ustom_user_stats\x18\x0f \x03(\x0b\x32-.CMsgMatchMetaDataContents.CustomUserStatInfo\x12L\n\x15watched_death_replays\x18\x10 \x03(\x0b\x32-.CMsgMatchMetaDataContents.WatchedDeathReplay\x12\x1d\n\x15objectives_mask_team0\x18\x11 \x01(\x04\x12\x1d\n\x15objectives_mask_team1\x18\x12 \x01(\x04\x12\x34\n\x08mid_boss\x18\x13 \x03(\x0b\x32\".CMsgMatchMetaDataContents.MidBoss\x12#\n\x1bis_high_skill_range_parties\x18\x14 \x01(\x08\x12\x14\n\x0clow_pri_pool\x18\x15 \x01(\x08\x12\x17\n\x0fnew_player_pool\x18\x16 \x01(\x08\"=\n\rEMatchOutcome\x12\x16\n\x12k_eOutcome_TeamWin\x10\x00\x12\x14\n\x10k_eOutcome_Error\x10\x01\"\x80\x01\n\x0b\x45GoldSource\x12\x0e\n\nk_ePlayers\x10\x01\x12\x11\n\rk_eLaneCreeps\x10\x02\x12\x0f\n\x0bk_eNeutrals\x10\x03\x12\r\n\tk_eBosses\x10\x04\x12\x0f\n\x0bk_eTreasure\x10\x05\x12\x0e\n\nk_eAssists\x10\x06\x12\r\n\tk_eDenies\x10\x07\"M\n\x11\x43MsgMatchMetaData\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x15\n\rmatch_details\x18\x02 \x01(\x0c\x12\x10\n\x08match_id\x18\x03 \x01(\x04\"4\n\x0b\x43MsgMapLine\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0f\n\x07initial\x18\x03 \x01(\x08\"\x90\x01\n\x14\x43MsgAccountHeroStats\x12\x0f\n\x07hero_id\x18\x01 \x01(\r\x12\x0f\n\x07stat_id\x18\x02 \x03(\r\x12\x13\n\x0btotal_value\x18\x03 \x03(\x04\x12\x15\n\rmedals_bronze\x18\x04 \x03(\r\x12\x15\n\rmedals_silver\x18\x05 \x03(\r\x12\x13\n\x0bmedals_gold\x18\x06 \x03(\r\"M\n\x14\x43MsgAccountBookStats\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\r\x12\x0f\n\x07\x62ook_xp\x18\x02 \x01(\r\x12\x13\n\x0b\x62ook_max_xp\x18\x03 \x01(\r\"L\n\x10\x43MsgAccountStats\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12$\n\x05stats\x18\x02 \x03(\x0b\x32\x15.CMsgAccountHeroStats\"E\n\x11\x43MsgGCAccountData\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x1c\n\x14\x63heater_report_score\x18\x02 \x01(\x02*\x8a\x01\n\rCMsgLaneColor\x12\x18\n\x14k_ELaneColor_Invalid\x10\x00\x12\x17\n\x13k_ELaneColor_Yellow\x10\x01\x12\x16\n\x12k_ELaneColor_Green\x10\x03\x12\x15\n\x11k_ELaneColor_Blue\x10\x04\x12\x17\n\x13k_ELaneColor_Purple\x10\x06*d\n\x18\x45GCCitadelCommonMessages\x12\x1f\n\x1ak_EMsgAnyToGCReportAsserts\x10\xd8\x36\x12\'\n\"k_EMsgAnyToGCReportAssertsResponse\x10\xd9\x36*\xa5\x02\n\x11\x45\x43itadelMatchMode\x12\x1f\n\x1bk_ECitadelMatchMode_Invalid\x10\x00\x12 \n\x1ck_ECitadelMatchMode_Unranked\x10\x01\x12$\n k_ECitadelMatchMode_PrivateLobby\x10\x02\x12\x1f\n\x1bk_ECitadelMatchMode_CoopBot\x10\x03\x12\x1e\n\x1ak_ECitadelMatchMode_Ranked\x10\x04\x12\"\n\x1ek_ECitadelMatchMode_ServerTest\x10\x05\x12 \n\x1ck_ECitadelMatchMode_Tutorial\x10\x06\x12 \n\x1ck_ECitadelMatchMode_HeroLabs\x10\x07*t\n\x11\x45\x43itadelLobbyTeam\x12\x1d\n\x19k_ECitadelLobbyTeam_Team0\x10\x00\x12\x1d\n\x19k_ECitadelLobbyTeam_Team1\x10\x01\x12!\n\x1dk_ECitadelLobbyTeam_Spectator\x10\x10*R\n\x18\x45\x43itadelAccountStatMedal\x12\x0b\n\x07k_eNone\x10\x00\x12\r\n\tk_eBronze\x10\x01\x12\r\n\tk_eSilver\x10\x02\x12\x0b\n\x07k_eGold\x10\x03*\xda\x0b\n\x11\x45\x43itadelObjective\x12\"\n\x1ek_eCitadelObjective_Team0_Core\x10\x00\x12)\n%k_eCitadelObjective_Team0_Tier1_Lane1\x10\x01\x12)\n%k_eCitadelObjective_Team0_Tier1_Lane2\x10\x02\x12)\n%k_eCitadelObjective_Team0_Tier1_Lane3\x10\x03\x12)\n%k_eCitadelObjective_Team0_Tier1_Lane4\x10\x04\x12)\n%k_eCitadelObjective_Team0_Tier2_Lane1\x10\x05\x12)\n%k_eCitadelObjective_Team0_Tier2_Lane2\x10\x06\x12)\n%k_eCitadelObjective_Team0_Tier2_Lane3\x10\x07\x12)\n%k_eCitadelObjective_Team0_Tier2_Lane4\x10\x08\x12#\n\x1fk_eCitadelObjective_Team0_Titan\x10\t\x12\x34\n0k_eCitadelObjective_Team0_TitanShieldGenerator_1\x10\n\x12\x34\n0k_eCitadelObjective_Team0_TitanShieldGenerator_2\x10\x0b\x12/\n+k_eCitadelObjective_Team0_BarrackBoss_Lane1\x10\x0c\x12/\n+k_eCitadelObjective_Team0_BarrackBoss_Lane2\x10\r\x12/\n+k_eCitadelObjective_Team0_BarrackBoss_Lane3\x10\x0e\x12/\n+k_eCitadelObjective_Team0_BarrackBoss_Lane4\x10\x0f\x12\"\n\x1ek_eCitadelObjective_Team1_Core\x10\x10\x12)\n%k_eCitadelObjective_Team1_Tier1_Lane1\x10\x11\x12)\n%k_eCitadelObjective_Team1_Tier1_Lane2\x10\x12\x12)\n%k_eCitadelObjective_Team1_Tier1_Lane3\x10\x13\x12)\n%k_eCitadelObjective_Team1_Tier1_Lane4\x10\x14\x12)\n%k_eCitadelObjective_Team1_Tier2_Lane1\x10\x15\x12)\n%k_eCitadelObjective_Team1_Tier2_Lane2\x10\x16\x12)\n%k_eCitadelObjective_Team1_Tier2_Lane3\x10\x17\x12)\n%k_eCitadelObjective_Team1_Tier2_Lane4\x10\x18\x12#\n\x1fk_eCitadelObjective_Team1_Titan\x10\x19\x12\x34\n0k_eCitadelObjective_Team1_TitanShieldGenerator_1\x10\x1a\x12\x34\n0k_eCitadelObjective_Team1_TitanShieldGenerator_2\x10\x1b\x12/\n+k_eCitadelObjective_Team1_BarrackBoss_Lane1\x10\x1c\x12/\n+k_eCitadelObjective_Team1_BarrackBoss_Lane2\x10\x1d\x12/\n+k_eCitadelObjective_Team1_BarrackBoss_Lane3\x10\x1e\x12/\n+k_eCitadelObjective_Team1_BarrackBoss_Lane4\x10\x1f\x12#\n\x1fk_eCitadelObjective_Neutral_Mid\x10 *\xc8\x05\n\x15\x45\x43itadelTeamObjective\x12 \n\x1ck_eCitadelTeamObjective_Core\x10\x00\x12\'\n#k_eCitadelTeamObjective_Tier1_Lane1\x10\x01\x12\'\n#k_eCitadelTeamObjective_Tier1_Lane2\x10\x02\x12\'\n#k_eCitadelTeamObjective_Tier1_Lane3\x10\x03\x12\'\n#k_eCitadelTeamObjective_Tier1_Lane4\x10\x04\x12\'\n#k_eCitadelTeamObjective_Tier2_Lane1\x10\x05\x12\'\n#k_eCitadelTeamObjective_Tier2_Lane2\x10\x06\x12\'\n#k_eCitadelTeamObjective_Tier2_Lane3\x10\x07\x12\'\n#k_eCitadelTeamObjective_Tier2_Lane4\x10\x08\x12!\n\x1dk_eCitadelTeamObjective_Titan\x10\t\x12\x32\n.k_eCitadelTeamObjective_TitanShieldGenerator_1\x10\n\x12\x32\n.k_eCitadelTeamObjective_TitanShieldGenerator_2\x10\x0b\x12-\n)k_eCitadelTeamObjective_BarrackBoss_Lane1\x10\x0c\x12-\n)k_eCitadelTeamObjective_BarrackBoss_Lane2\x10\r\x12-\n)k_eCitadelTeamObjective_BarrackBoss_Lane3\x10\x0e\x12-\n)k_eCitadelTeamObjective_BarrackBoss_Lane4\x10\x0f*\xec\x01\n\x15\x45\x43itadelBotDifficulty\x12 \n\x1ck_ECitadelBotDifficulty_None\x10\x00\x12 \n\x1ck_ECitadelBotDifficulty_Easy\x10\x01\x12\"\n\x1ek_ECitadelBotDifficulty_Medium\x10\x02\x12 \n\x1ck_ECitadelBotDifficulty_Hard\x10\x03\x12%\n!k_ECitadelBotDifficulty_Nightmare\x10\x04\x12\"\n\x1ek_ECitadelBotDifficulty_Guided\x10\x05*\xda\x01\n\x12\x45\x43itadelRegionMode\x12\x1c\n\x18k_ECitadelRegionMode_ROW\x10\x00\x12\x1f\n\x1bk_ECitadelRegionMode_Europe\x10\x01\x12\x1f\n\x1bk_ECitadelRegionMode_SEAsia\x10\x02\x12!\n\x1dk_ECitadelRegionMode_SAmerica\x10\x03\x12\x1f\n\x1bk_ECitadelRegionMode_Russia\x10\x04\x12 \n\x1ck_ECitadelRegionMode_Oceania\x10\x05*\x91\x01\n\x10\x45\x43itadelGameMode\x12\x1e\n\x1ak_ECitadelGameMode_Invalid\x10\x00\x12\x1d\n\x19k_ECitadelGameMode_Normal\x10\x01\x12\x1e\n\x1ak_ECitadelGameMode_1v1Test\x10\x02\x12\x1e\n\x1ak_ECitadelGameMode_Sandbox\x10\x03*\xbc\x01\n\x11\x45LobbyServerState\x12\x1e\n\x1ak_eLobbyServerState_Assign\x10\x00\x12\x1e\n\x1ak_eLobbyServerState_InGame\x10\x01\x12!\n\x1dk_eLobbyServerState_PostMatch\x10\x02\x12!\n\x1dk_eLobbyServerState_SignedOut\x10\x03\x12!\n\x1dk_eLobbyServerState_Abandoned\x10\x04*\xa9\x01\n\x0e\x45\x42\x61nnedFeature\x12\x1c\n\x18k_eBannedFeature_Invalid\x10\x00\x12+\n\'k_eBannedFeature_LowPriorityMatchmaking\x10\x01\x12$\n k_eBannedFeature_CommsRestricted\x10\x02\x12&\n\"k_eBannedFeature_ReportingDisabled\x10\x03*\xd6\x01\n\x11\x45\x46\x65\x61tureBanReason\x12\x1f\n\x1bk_eFeatureBanReason_Invalid\x10\x00\x12\"\n\x1ek_eFeatureBanReason_DevCommand\x10\x01\x12%\n!k_eFeatureBanReason_PlayerReports\x10\x02\x12%\n!k_eFeatureBanReason_MatchAbandons\x10\x03\x12.\n*k_eFeatureBanReason_ExcessivePlayerReports\x10\x04')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'citadel_gcmessages_common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CMSGREGIONPINGTIMESCLIENT.fields_by_name['data_center_codes']._options = None
  _CMSGREGIONPINGTIMESCLIENT.fields_by_name['data_center_codes']._serialized_options = b'\020\001'
  _CMSGREGIONPINGTIMESCLIENT.fields_by_name['ping_times']._options = None
  _CMSGREGIONPINGTIMESCLIENT.fields_by_name['ping_times']._serialized_options = b'\020\001'
  _CSOCITADELPARTY_MEMBER.fields_by_name['owned_heroes']._options = None
  _CSOCITADELPARTY_MEMBER.fields_by_name['owned_heroes']._serialized_options = b'\020\001'
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['x_pos']._options = None
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['x_pos']._serialized_options = b'\020\001'
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['y_pos']._options = None
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['y_pos']._serialized_options = b'\020\001'
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['alive']._options = None
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['alive']._serialized_options = b'\020\001'
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['health']._options = None
  _CMSGMATCHPLAYERPATHSDATA_PATH.fields_by_name['health']._serialized_options = b'\020\001'
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGETOPLAYER.fields_by_name['damage']._options = None
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGETOPLAYER.fields_by_name['damage']._serialized_options = b'\020\001'
  _CMSGMATCHPLAYERDAMAGEMATRIX_SOURCEDETAILS.fields_by_name['stat_type']._options = None
  _CMSGMATCHPLAYERDAMAGEMATRIX_SOURCEDETAILS.fields_by_name['stat_type']._serialized_options = b'\020\001'
  _CMSGMATCHPLAYERDAMAGEMATRIX.fields_by_name['sample_time_s']._options = None
  _CMSGMATCHPLAYERDAMAGEMATRIX.fields_by_name['sample_time_s']._serialized_options = b'\020\001'
  _CMSGMATCHMETADATACONTENTS_PLAYERS.fields_by_name['stats_type_stat']._options = None
  _CMSGMATCHMETADATACONTENTS_PLAYERS.fields_by_name['stats_type_stat']._serialized_options = b'\020\001'
  _CMSGLANECOLOR._serialized_start=9822
  _CMSGLANECOLOR._serialized_end=9960
  _EGCCITADELCOMMONMESSAGES._serialized_start=9962
  _EGCCITADELCOMMONMESSAGES._serialized_end=10062
  _ECITADELMATCHMODE._serialized_start=10065
  _ECITADELMATCHMODE._serialized_end=10358
  _ECITADELLOBBYTEAM._serialized_start=10360
  _ECITADELLOBBYTEAM._serialized_end=10476
  _ECITADELACCOUNTSTATMEDAL._serialized_start=10478
  _ECITADELACCOUNTSTATMEDAL._serialized_end=10560
  _ECITADELOBJECTIVE._serialized_start=10563
  _ECITADELOBJECTIVE._serialized_end=12061
  _ECITADELTEAMOBJECTIVE._serialized_start=12064
  _ECITADELTEAMOBJECTIVE._serialized_end=12776
  _ECITADELBOTDIFFICULTY._serialized_start=12779
  _ECITADELBOTDIFFICULTY._serialized_end=13015
  _ECITADELREGIONMODE._serialized_start=13018
  _ECITADELREGIONMODE._serialized_end=13236
  _ECITADELGAMEMODE._serialized_start=13239
  _ECITADELGAMEMODE._serialized_end=13384
  _ELOBBYSERVERSTATE._serialized_start=13387
  _ELOBBYSERVERSTATE._serialized_end=13575
  _EBANNEDFEATURE._serialized_start=13578
  _EBANNEDFEATURE._serialized_end=13747
  _EFEATUREBANREASON._serialized_start=13750
  _EFEATUREBANREASON._serialized_end=13964
  _CSOCITADELLOBBY._serialized_start=81
  _CSOCITADELLOBBY._serialized_end=589
  _CLOBBYDATA_POSTMATCHSURVEY._serialized_start=592
  _CLOBBYDATA_POSTMATCHSURVEY._serialized_end=736
  _CLOBBYDATA_POSTMATCHSURVEY_PLAYERSURVEY._serialized_start=681
  _CLOBBYDATA_POSTMATCHSURVEY_PLAYERSURVEY._serialized_end=736
  _CMSGHEROSELECTIONMATCHINFO._serialized_start=739
  _CMSGHEROSELECTIONMATCHINFO._serialized_end=869
  _CMSGHEROSELECTIONMATCHINFO_HERO._serialized_start=828
  _CMSGHEROSELECTIONMATCHINFO_HERO._serialized_end=869
  _CMSGSTARTFINDINGMATCHINFO._serialized_start=872
  _CMSGSTARTFINDINGMATCHINFO._serialized_end=1258
  _CMSGANYTOGCREPORTASSERTS._serialized_start=1261
  _CMSGANYTOGCREPORTASSERTS._serialized_end=1551
  _CMSGANYTOGCREPORTASSERTS_TRACKEDASSERT._serialized_start=1365
  _CMSGANYTOGCREPORTASSERTS_TRACKEDASSERT._serialized_end=1551
  _CMSGANYTOGCREPORTASSERTSRESPONSE._serialized_start=1553
  _CMSGANYTOGCREPORTASSERTSRESPONSE._serialized_end=1604
  _CMSGREGIONPINGTIMESCLIENT._serialized_start=1606
  _CMSGREGIONPINGTIMESCLIENT._serialized_end=1688
  _CSOCITADELPARTY._serialized_start=1691
  _CSOCITADELPARTY._serialized_end=3629
  _CSOCITADELPARTY_PRIVATELOBBYSLOT._serialized_start=2439
  _CSOCITADELPARTY_PRIVATELOBBYSLOT._serialized_end=2501
  _CSOCITADELPARTY_SERVERREGION._serialized_start=2503
  _CSOCITADELPARTY_SERVERREGION._serialized_end=2536
  _CSOCITADELPARTY_PRIVATELOBBYSETTINGS._serialized_start=2539
  _CSOCITADELPARTY_PRIVATELOBBYSETTINGS._serialized_end=2835
  _CSOCITADELPARTY_MEMBER._serialized_start=2838
  _CSOCITADELPARTY_MEMBER._serialized_end=3224
  _CSOCITADELPARTY_LEFTMEMBER._serialized_start=3226
  _CSOCITADELPARTY_LEFTMEMBER._serialized_end=3353
  _CSOCITADELPARTY_INVITE._serialized_start=3355
  _CSOCITADELPARTY_INVITE._serialized_end=3425
  _CSOCITADELPARTY_EMEMBERRIGHTS._serialized_start=3427
  _CSOCITADELPARTY_EMEMBERRIGHTS._serialized_end=3498
  _CSOCITADELPARTY_EPLAYERTYPE._serialized_start=3500
  _CSOCITADELPARTY_EPLAYERTYPE._serialized_end=3568
  _CSOCITADELPARTY_ECHATMODE._serialized_start=3570
  _CSOCITADELPARTY_ECHATMODE._serialized_end=3629
  _CMSGMATCHPLAYERPATHSDATA._serialized_start=3632
  _CMSGMATCHPLAYERPATHSDATA._serialized_end=3953
  _CMSGMATCHPLAYERPATHSDATA_PATH._serialized_start=3789
  _CMSGMATCHPLAYERPATHSDATA_PATH._serialized_end=3953
  _CMSGMATCHPLAYERDAMAGEMATRIX._serialized_start=3956
  _CMSGMATCHPLAYERDAMAGEMATRIX._serialized_end=4674
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGETOPLAYER._serialized_start=4149
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGETOPLAYER._serialized_end=4213
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGESOURCE._serialized_start=4215
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGESOURCE._serialized_end=4331
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGEDEALER._serialized_start=4333
  _CMSGMATCHPLAYERDAMAGEMATRIX_DAMAGEDEALER._serialized_end=4442
  _CMSGMATCHPLAYERDAMAGEMATRIX_SOURCEDETAILS._serialized_start=4444
  _CMSGMATCHPLAYERDAMAGEMATRIX_SOURCEDETAILS._serialized_end=4543
  _CMSGMATCHPLAYERDAMAGEMATRIX_ESTATTYPE._serialized_start=4546
  _CMSGMATCHPLAYERDAMAGEMATRIX_ESTATTYPE._serialized_end=4674
  _CMSGMATCHMETADATACONTENTS._serialized_start=4677
  _CMSGMATCHMETADATACONTENTS._serialized_end=9311
  _CMSGMATCHMETADATACONTENTS_POSITION._serialized_start=4764
  _CMSGMATCHMETADATACONTENTS_POSITION._serialized_end=4807
  _CMSGMATCHMETADATACONTENTS_DEATHS._serialized_start=4810
  _CMSGMATCHMETADATACONTENTS_DEATHS._serialized_end=5006
  _CMSGMATCHMETADATACONTENTS_ITEMS._serialized_start=5009
  _CMSGMATCHMETADATACONTENTS_ITEMS._serialized_end=5137
  _CMSGMATCHMETADATACONTENTS_PING._serialized_start=5139
  _CMSGMATCHMETADATACONTENTS_PING._serialized_end=5204
  _CMSGMATCHMETADATACONTENTS_GOLDSOURCE._serialized_start=5207
  _CMSGMATCHMETADATACONTENTS_GOLDSOURCE._serialized_end=5351
  _CMSGMATCHMETADATACONTENTS_CUSTOMUSERSTATINFO._serialized_start=5353
  _CMSGMATCHMETADATACONTENTS_CUSTOMUSERSTATINFO._serialized_end=5399
  _CMSGMATCHMETADATACONTENTS_CUSTOMUSERSTAT._serialized_start=5401
  _CMSGMATCHMETADATACONTENTS_CUSTOMUSERSTAT._serialized_end=5444
  _CMSGMATCHMETADATACONTENTS_PLAYERSTATS._serialized_start=5447
  _CMSGMATCHMETADATACONTENTS_PLAYERSTATS._serialized_end=6526
  _CMSGMATCHMETADATACONTENTS_ABILITYSTAT._serialized_start=6528
  _CMSGMATCHMETADATACONTENTS_ABILITYSTAT._serialized_end=6584
  _CMSGMATCHMETADATACONTENTS_BOOKREWARD._serialized_start=6586
  _CMSGMATCHMETADATACONTENTS_BOOKREWARD._serialized_end=6655
  _CMSGMATCHMETADATACONTENTS_PLAYERS._serialized_start=6658
  _CMSGMATCHMETADATACONTENTS_PLAYERS._serialized_end=7386
  _CMSGMATCHMETADATACONTENTS_OBJECTIVE._serialized_start=7389
  _CMSGMATCHMETADATACONTENTS_OBJECTIVE._serialized_end=7788
  _CMSGMATCHMETADATACONTENTS_MIDBOSS._serialized_start=7791
  _CMSGMATCHMETADATACONTENTS_MIDBOSS._serialized_end=7963
  _CMSGMATCHMETADATACONTENTS_PAUSE._serialized_start=7965
  _CMSGMATCHMETADATACONTENTS_PAUSE._serialized_end=8040
  _CMSGMATCHMETADATACONTENTS_WATCHEDDEATHREPLAY._serialized_start=8042
  _CMSGMATCHMETADATACONTENTS_WATCHEDDEATHREPLAY._serialized_end=8104
  _CMSGMATCHMETADATACONTENTS_MATCHINFO._serialized_start=8107
  _CMSGMATCHMETADATACONTENTS_MATCHINFO._serialized_end=9117
  _CMSGMATCHMETADATACONTENTS_EMATCHOUTCOME._serialized_start=9119
  _CMSGMATCHMETADATACONTENTS_EMATCHOUTCOME._serialized_end=9180
  _CMSGMATCHMETADATACONTENTS_EGOLDSOURCE._serialized_start=9183
  _CMSGMATCHMETADATACONTENTS_EGOLDSOURCE._serialized_end=9311
  _CMSGMATCHMETADATA._serialized_start=9313
  _CMSGMATCHMETADATA._serialized_end=9390
  _CMSGMAPLINE._serialized_start=9392
  _CMSGMAPLINE._serialized_end=9444
  _CMSGACCOUNTHEROSTATS._serialized_start=9447
  _CMSGACCOUNTHEROSTATS._serialized_end=9591
  _CMSGACCOUNTBOOKSTATS._serialized_start=9593
  _CMSGACCOUNTBOOKSTATS._serialized_end=9670
  _CMSGACCOUNTSTATS._serialized_start=9672
  _CMSGACCOUNTSTATS._serialized_end=9748
  _CMSGGCACCOUNTDATA._serialized_start=9750
  _CMSGGCACCOUNTDATA._serialized_end=9819
# @@protoc_insertion_point(module_scope)
