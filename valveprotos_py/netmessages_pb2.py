# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: netmessages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11netmessages.proto\x1a\x16networkbasetypes.proto\"}\n\x12\x43\x43LCMsg_ClientInfo\x12\x16\n\x0esend_table_crc\x18\x01 \x01(\x07\x12\x14\n\x0cserver_count\x18\x02 \x01(\r\x12\x0f\n\x07is_hltv\x18\x03 \x01(\x08\x12\x12\n\nfriends_id\x18\x05 \x01(\r\x12\x14\n\x0c\x66riends_name\x18\x06 \x01(\t\"9\n\x0c\x43\x43LCMsg_Move\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x1b\n\x13last_command_number\x18\x04 \x01(\r\"\x8f\x02\n\x0e\x43MsgVoiceAudio\x12:\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x12.VoiceDataFormat_t:\x16VOICEDATA_FORMAT_STEAM\x12\x12\n\nvoice_data\x18\x02 \x01(\x0c\x12\x16\n\x0esequence_bytes\x18\x03 \x01(\x05\x12\x16\n\x0esection_number\x18\x04 \x01(\r\x12\x13\n\x0bsample_rate\x18\x05 \x01(\r\x12\"\n\x1auncompressed_sample_offset\x18\x06 \x01(\r\x12\x13\n\x0bnum_packets\x18\x07 \x01(\r\x12\x1a\n\x0epacket_offsets\x18\x08 \x03(\rB\x02\x10\x01\x12\x13\n\x0bvoice_level\x18\t \x01(\x02\"O\n\x11\x43\x43LCMsg_VoiceData\x12\x1e\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x0f.CMsgVoiceAudio\x12\x0c\n\x04xuid\x18\x02 \x01(\x06\x12\x0c\n\x04tick\x18\x03 \x01(\r\"A\n\x13\x43\x43LCMsg_BaselineAck\x12\x15\n\rbaseline_tick\x18\x01 \x01(\x05\x12\x13\n\x0b\x62\x61seline_nr\x18\x02 \x01(\x05\"*\n\x14\x43\x43LCMsg_ListenEvents\x12\x12\n\nevent_mask\x18\x01 \x03(\x07\"\\\n\x18\x43\x43LCMsg_RespondCvarValue\x12\x0e\n\x06\x63ookie\x18\x01 \x01(\x05\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\"m\n\x14\x43\x43LCMsg_FileCRCCheck\x12\x11\n\tcode_path\x18\x01 \x01(\x05\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x15\n\rcode_filename\x18\x03 \x01(\x05\x12\x10\n\x08\x66ilename\x18\x04 \x01(\t\x12\x0b\n\x03\x63rc\x18\x05 \x01(\x07\"+\n\x17\x43\x43LCMsg_LoadingProgress\x12\x10\n\x08progress\x18\x01 \x01(\x05\"0\n\x1a\x43\x43LCMsg_SplitPlayerConnect\x12\x12\n\nplayername\x18\x01 \x01(\t\"-\n\x1d\x43\x43LCMsg_SplitPlayerDisconnect\x12\x0c\n\x04slot\x18\x01 \x01(\x05\"*\n\x14\x43\x43LCMsg_ServerStatus\x12\x12\n\nsimplified\x18\x01 \x01(\x08\"Z\n\x14\x43\x43LCMsg_RequestPause\x12-\n\npause_type\x18\x01 \x01(\x0e\x32\x0f.RequestPause_t:\x08RP_PAUSE\x12\x13\n\x0bpause_group\x18\x02 \x01(\x05\"$\n\x14\x43\x43LCMsg_CmdKeyValues\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"*\n\x19\x43\x43LCMsg_RconServerDetails\x12\r\n\x05token\x18\x01 \x01(\x0c\"\xdd\x02\n\x16\x43MsgSource2SystemSpecs\x12\x0e\n\x06\x63pu_id\x18\x01 \x01(\t\x12\x11\n\tcpu_brand\x18\x02 \x01(\t\x12\x11\n\tcpu_model\x18\x03 \x01(\r\x12\x18\n\x10\x63pu_num_physical\x18\x04 \x01(\r\x12\x1d\n\x15ram_physical_total_mb\x18\x15 \x01(\r\x12!\n\x19gpu_rendersystem_dll_name\x18) \x01(\t\x12\x15\n\rgpu_vendor_id\x18* \x01(\r\x12\x17\n\x0fgpu_driver_name\x18+ \x01(\t\x12\x1f\n\x17gpu_driver_version_high\x18, \x01(\r\x12\x1e\n\x16gpu_driver_version_low\x18- \x01(\r\x12\x1c\n\x14gpu_dx_support_level\x18. \x01(\r\x12\"\n\x1agpu_texture_memory_size_mb\x18/ \x01(\r\"\x81\x04\n\x1e\x43MsgSource2VProfLiteReportItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63tive_samples\x18\x02 \x01(\r\x12\x1e\n\x16\x61\x63tive_samples_1secmax\x18\x04 \x01(\r\x12\x10\n\x08usec_max\x18\x03 \x01(\r\x12\x17\n\x0fusec_avg_active\x18\x0b \x01(\r\x12\x17\n\x0fusec_p50_active\x18\x0c \x01(\r\x12\x17\n\x0fusec_p99_active\x18\r \x01(\r\x12\x14\n\x0cusec_avg_all\x18\x15 \x01(\r\x12\x14\n\x0cusec_p50_all\x18\x16 \x01(\r\x12\x14\n\x0cusec_p99_all\x18\x17 \x01(\r\x12\x1f\n\x17usec_1secmax_avg_active\x18\x1f \x01(\r\x12\x1f\n\x17usec_1secmax_p50_active\x18  \x01(\r\x12\x1f\n\x17usec_1secmax_p95_active\x18! \x01(\r\x12\x1f\n\x17usec_1secmax_p99_active\x18\" \x01(\r\x12\x1c\n\x14usec_1secmax_avg_all\x18) \x01(\r\x12\x1c\n\x14usec_1secmax_p50_all\x18* \x01(\r\x12\x1c\n\x14usec_1secmax_p95_all\x18+ \x01(\r\x12\x1c\n\x14usec_1secmax_p99_all\x18, \x01(\r\"\x96\x01\n\x1a\x43MsgSource2VProfLiteReport\x12.\n\x05total\x18\x01 \x01(\x0b\x32\x1f.CMsgSource2VProfLiteReportItem\x12.\n\x05items\x18\x02 \x03(\x0b\x32\x1f.CMsgSource2VProfLiteReportItem\x12\x18\n\x10\x64iscarded_frames\x18\x03 \x01(\r\"\xb5\x06\n\x1d\x43MsgSource2NetworkFlowQuality\x12\x10\n\x08\x64uration\x18\x01 \x01(\r\x12\x13\n\x0b\x62ytes_total\x18\x05 \x01(\x04\x12\x1c\n\x14\x62ytes_total_reliable\x18\x06 \x01(\x04\x12\x19\n\x11\x62ytes_total_voice\x18\x07 \x01(\x04\x12\x15\n\rbytes_sec_p95\x18\n \x01(\r\x12\x15\n\rbytes_sec_p99\x18\x0b \x01(\r\x12\x18\n\x10\x65nginemsgs_total\x18\x14 \x01(\r\x12\x1a\n\x12\x65nginemsgs_sec_p95\x18\x15 \x01(\r\x12\x1a\n\x12\x65nginemsgs_sec_p99\x18\x16 \x01(\r\x12\x13\n\x0bticks_total\x18( \x01(\r\x12\x12\n\nticks_good\x18) \x01(\r\x12\x1e\n\x16ticks_good_almost_late\x18* \x01(\r\x12\x1b\n\x13ticks_fixed_dropped\x18+ \x01(\r\x12\x18\n\x10ticks_fixed_late\x18, \x01(\r\x12\x19\n\x11ticks_bad_dropped\x18- \x01(\r\x12\x16\n\x0eticks_bad_late\x18. \x01(\r\x12\x17\n\x0fticks_bad_other\x18/ \x01(\r\x12#\n\x1btick_missrate_samples_total\x18\x32 \x01(\r\x12%\n\x1dtick_missrate_samples_perfect\x18\x33 \x01(\r\x12(\n tick_missrate_samples_perfectnet\x18\x34 \x01(\r\x12 \n\x18tick_missratenet_p75_x10\x18\x35 \x01(\r\x12 \n\x18tick_missratenet_p95_x10\x18\x36 \x01(\r\x12 \n\x18tick_missratenet_p99_x10\x18\x37 \x01(\r\x12\x15\n\rrecvmargin_p1\x18= \x01(\x11\x12\x15\n\rrecvmargin_p5\x18> \x01(\x11\x12\x16\n\x0erecvmargin_p25\x18? \x01(\x11\x12\x16\n\x0erecvmargin_p50\x18@ \x01(\x11\x12\x16\n\x0erecvmargin_p75\x18\x41 \x01(\x11\x12\x16\n\x0erecvmargin_p95\x18\x42 \x01(\x11\"v\n\x12\x43\x43LCMsg_Diagnostic\x12-\n\x0csystem_specs\x18\x01 \x01(\x0b\x32\x17.CMsgSource2SystemSpecs\x12\x31\n\x0cvprof_report\x18\x02 \x01(\x0b\x32\x1b.CMsgSource2VProfLiteReport\"\xff\x02\n-CSource2Metrics_MatchPerfSummary_Notification\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\tgame_mode\x18\x02 \x01(\t\x12\x17\n\x0fserver_build_id\x18\x03 \x01(\r\x12\x33\n\x0eserver_profile\x18\n \x01(\x0b\x32\x1b.CMsgSource2VProfLiteReport\x12\x46\n\x07\x63lients\x18\x0b \x03(\x0b\x32\x35.CSource2Metrics_MatchPerfSummary_Notification.Client\x12\x0b\n\x03map\x18\x14 \x01(\t\x1a\x88\x01\n\x06\x43lient\x12-\n\x0csystem_specs\x18\x01 \x01(\x0b\x32\x17.CMsgSource2SystemSpecs\x12,\n\x07profile\x18\x02 \x01(\x0b\x32\x1b.CMsgSource2VProfLiteReport\x12\x10\n\x08\x62uild_id\x18\x03 \x01(\r\x12\x0f\n\x07steamid\x18\n \x01(\x06\"\x87\x03\n\x12\x43SVCMsg_ServerInfo\x12\x10\n\x08protocol\x18\x01 \x01(\x05\x12\x14\n\x0cserver_count\x18\x02 \x01(\x05\x12\x14\n\x0cis_dedicated\x18\x03 \x01(\x08\x12\x0f\n\x07is_hltv\x18\x04 \x01(\x08\x12\x0c\n\x04\x63_os\x18\x06 \x01(\x05\x12\x13\n\x0bmax_clients\x18\n \x01(\x05\x12\x13\n\x0bmax_classes\x18\x0b \x01(\x05\x12\x17\n\x0bplayer_slot\x18\x0c \x01(\x05:\x02-1\x12\x15\n\rtick_interval\x18\r \x01(\x02\x12\x10\n\x08game_dir\x18\x0e \x01(\t\x12\x10\n\x08map_name\x18\x0f \x01(\t\x12\x10\n\x08sky_name\x18\x10 \x01(\t\x12\x11\n\thost_name\x18\x11 \x01(\t\x12\x12\n\naddon_name\x18\x12 \x01(\t\x12>\n\x13game_session_config\x18\x13 \x01(\x0b\x32!.CSVCMsg_GameSessionConfiguration\x12\x1d\n\x15game_session_manifest\x18\x14 \x01(\x0c\"\x8b\x01\n\x11\x43SVCMsg_ClassInfo\x12\x18\n\x10\x63reate_on_client\x18\x01 \x01(\x08\x12+\n\x07\x63lasses\x18\x02 \x03(\x0b\x32\x1a.CSVCMsg_ClassInfo.class_t\x1a/\n\x07\x63lass_t\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\x05\x12\x12\n\nclass_name\x18\x03 \x01(\t\"\"\n\x10\x43SVCMsg_SetPause\x12\x0e\n\x06paused\x18\x01 \x01(\x08\"G\n\x11\x43SVCMsg_VoiceInit\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12\r\n\x05\x63odec\x18\x02 \x01(\t\x12\x12\n\x07version\x18\x03 \x01(\x05:\x01\x30\"\x1d\n\rCSVCMsg_Print\x12\x0c\n\x04text\x18\x01 \x01(\t\"\xe3\x03\n\x0e\x43SVCMsg_Sounds\x12\x16\n\x0ereliable_sound\x18\x01 \x01(\x08\x12+\n\x06sounds\x18\x02 \x03(\x0b\x32\x1b.CSVCMsg_Sounds.sounddata_t\x1a\x8b\x03\n\x0bsounddata_t\x12\x10\n\x08origin_x\x18\x01 \x01(\x11\x12\x10\n\x08origin_y\x18\x02 \x01(\x11\x12\x10\n\x08origin_z\x18\x03 \x01(\x11\x12\x0e\n\x06volume\x18\x04 \x01(\r\x12\x13\n\x0b\x64\x65lay_value\x18\x05 \x01(\x02\x12\x17\n\x0fsequence_number\x18\x06 \x01(\x05\x12\x18\n\x0c\x65ntity_index\x18\x07 \x01(\x05:\x02-1\x12\x0f\n\x07\x63hannel\x18\x08 \x01(\x05\x12\r\n\x05pitch\x18\t \x01(\x05\x12\r\n\x05\x66lags\x18\n \x01(\x05\x12\x11\n\tsound_num\x18\x0b \x01(\r\x12\x18\n\x10sound_num_handle\x18\x0c \x01(\x07\x12\x16\n\x0espeaker_entity\x18\r \x01(\x05\x12\x13\n\x0brandom_seed\x18\x0e \x01(\x05\x12\x13\n\x0bsound_level\x18\x0f \x01(\x05\x12\x13\n\x0bis_sentence\x18\x10 \x01(\x08\x12\x12\n\nis_ambient\x18\x11 \x01(\x08\x12\x0c\n\x04guid\x18\x12 \x01(\r\x12\x19\n\x11sound_resource_id\x18\x13 \x01(\x06\"X\n\x10\x43SVCMsg_Prefetch\x12\x13\n\x0bsound_index\x18\x01 \x01(\x05\x12/\n\rresource_type\x18\x02 \x01(\x0e\x32\r.PrefetchType:\tPFT_SOUND\"=\n\x0f\x43SVCMsg_SetView\x12\x18\n\x0c\x65ntity_index\x18\x01 \x01(\x05:\x02-1\x12\x10\n\x04slot\x18\x02 \x01(\x05:\x02-1\"@\n\x10\x43SVCMsg_FixAngle\x12\x10\n\x08relative\x18\x01 \x01(\x08\x12\x1a\n\x05\x61ngle\x18\x02 \x01(\x0b\x32\x0b.CMsgQAngle\"4\n\x16\x43SVCMsg_CrosshairAngle\x12\x1a\n\x05\x61ngle\x18\x01 \x01(\x0b\x32\x0b.CMsgQAngle\"\x8e\x01\n\x10\x43SVCMsg_BSPDecal\x12\x18\n\x03pos\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x13\x64\x65\x63\x61l_texture_index\x18\x02 \x01(\x05\x12\x18\n\x0c\x65ntity_index\x18\x03 \x01(\x05:\x02-1\x12\x13\n\x0bmodel_index\x18\x04 \x01(\x05\x12\x14\n\x0clow_priority\x18\x05 \x01(\x08\"~\n\x13\x43SVCMsg_SplitScreen\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x18.ESplitScreenMessageType:\x17MSG_SPLITSCREEN_ADDUSER\x12\x0c\n\x04slot\x18\x02 \x01(\x05\x12\x18\n\x0cplayer_index\x18\x03 \x01(\x05:\x02-1\"9\n\x14\x43SVCMsg_GetCvarValue\x12\x0e\n\x06\x63ookie\x18\x01 \x01(\x05\x12\x11\n\tcvar_name\x18\x02 \x01(\t\"<\n\x0c\x43SVCMsg_Menu\x12\x13\n\x0b\x64ialog_type\x18\x01 \x01(\x05\x12\x17\n\x0fmenu_key_values\x18\x02 \x01(\x0c\"N\n\x13\x43SVCMsg_UserMessage\x12\x10\n\x08msg_type\x18\x01 \x01(\x05\x12\x10\n\x08msg_data\x18\x02 \x01(\x0c\x12\x13\n\x0bpassthrough\x18\x03 \x01(\x05\"\xb0\x02\n\x11\x43SVCMsg_SendTable\x12\x0e\n\x06is_end\x18\x01 \x01(\x08\x12\x16\n\x0enet_table_name\x18\x02 \x01(\t\x12\x15\n\rneeds_decoder\x18\x03 \x01(\x08\x12,\n\x05props\x18\x04 \x03(\x0b\x32\x1d.CSVCMsg_SendTable.sendprop_t\x1a\xad\x01\n\nsendprop_t\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x10\n\x08var_name\x18\x02 \x01(\t\x12\r\n\x05\x66lags\x18\x03 \x01(\x05\x12\x10\n\x08priority\x18\x04 \x01(\x05\x12\x0f\n\x07\x64t_name\x18\x05 \x01(\t\x12\x14\n\x0cnum_elements\x18\x06 \x01(\x05\x12\x11\n\tlow_value\x18\x07 \x01(\x02\x12\x12\n\nhigh_value\x18\x08 \x01(\x02\x12\x10\n\x08num_bits\x18\t \x01(\x05\"\xd1\x01\n\x15\x43SVCMsg_GameEventList\x12\x38\n\x0b\x64\x65scriptors\x18\x01 \x03(\x0b\x32#.CSVCMsg_GameEventList.descriptor_t\x1a#\n\x05key_t\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x1aY\n\x0c\x64\x65scriptor_t\x12\x0f\n\x07\x65ventid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x04keys\x18\x03 \x03(\x0b\x32\x1c.CSVCMsg_GameEventList.key_t\"\xd9\x06\n\x16\x43SVCMsg_PacketEntities\x12\x13\n\x0bmax_entries\x18\x01 \x01(\x05\x12\x17\n\x0fupdated_entries\x18\x02 \x01(\x05\x12\x17\n\x0flegacy_is_delta\x18\x03 \x01(\x08\x12\x17\n\x0fupdate_baseline\x18\x04 \x01(\x08\x12\x10\n\x08\x62\x61seline\x18\x05 \x01(\x05\x12\x12\n\ndelta_from\x18\x06 \x01(\x05\x12\x13\n\x0b\x65ntity_data\x18\x07 \x01(\x0c\x12\x1a\n\x12pending_full_frame\x18\x08 \x01(\x08\x12 \n\x18\x61\x63tive_spawngroup_handle\x18\t \x01(\r\x12\'\n\x1fmax_spawngroup_creationsequence\x18\n \x01(\r\x12 \n\x18last_cmd_number_executed\x18\x0b \x01(\r\x12\"\n\x1alast_cmd_number_recv_delta\x18\x11 \x01(\x11\x12\x13\n\x0bserver_tick\x18\x0c \x01(\r\x12\x1b\n\x13serialized_entities\x18\r \x01(\x0c\x12I\n\x13\x61lternate_baselines\x18\x0f \x03(\x0b\x32,.CSVCMsg_PacketEntities.alternate_baseline_t\x12#\n\x1bhas_pvs_vis_bits_deprecated\x18\x10 \x01(\r\x12\x1b\n\x0f\x63md_recv_status\x18\x16 \x03(\x11\x42\x02\x10\x01\x12T\n\x18non_transmitted_entities\x18\x13 \x01(\x0b\x32\x32.CSVCMsg_PacketEntities.non_transmitted_entities_t\x12 \n\x18\x63q_starved_command_ticks\x18\x14 \x01(\r\x12\"\n\x1a\x63q_discarded_command_ticks\x18\x15 \x01(\r\x12\x14\n\x0b\x64\x65v_padding\x18\xe7\x07 \x01(\x0c\x1a\x44\n\x14\x61lternate_baseline_t\x12\x14\n\x0c\x65ntity_index\x18\x01 \x01(\x05\x12\x16\n\x0e\x62\x61seline_index\x18\x02 \x01(\x05\x1a@\n\x1anon_transmitted_entities_t\x12\x14\n\x0cheader_count\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"R\n\x14\x43SVCMsg_TempEntities\x12\x10\n\x08reliable\x18\x01 \x01(\x08\x12\x13\n\x0bnum_entries\x18\x02 \x01(\x05\x12\x13\n\x0b\x65ntity_data\x18\x03 \x01(\x0c\"\x89\x02\n\x19\x43SVCMsg_CreateStringTable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bnum_entries\x18\x02 \x01(\x05\x12\x1c\n\x14user_data_fixed_size\x18\x03 \x01(\x08\x12\x16\n\x0euser_data_size\x18\x04 \x01(\x05\x12\x1b\n\x13user_data_size_bits\x18\x05 \x01(\x05\x12\r\n\x05\x66lags\x18\x06 \x01(\x05\x12\x13\n\x0bstring_data\x18\x07 \x01(\x0c\x12\x19\n\x11uncompressed_size\x18\x08 \x01(\x05\x12\x17\n\x0f\x64\x61ta_compressed\x18\t \x01(\x08\x12\x1e\n\x16using_varint_bitcounts\x18\n \x01(\x08\"_\n\x19\x43SVCMsg_UpdateStringTable\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\x1b\n\x13num_changed_entries\x18\x02 \x01(\x05\x12\x13\n\x0bstring_data\x18\x03 \x01(\x0c\"\xa1\x01\n\x11\x43SVCMsg_VoiceData\x12\x1e\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x0f.CMsgVoiceAudio\x12\x12\n\x06\x63lient\x18\x02 \x01(\x05:\x02-1\x12\x11\n\tproximity\x18\x03 \x01(\x08\x12\x0c\n\x04xuid\x18\x04 \x01(\x06\x12\x14\n\x0c\x61udible_mask\x18\x05 \x01(\x05\x12\x0c\n\x04tick\x18\x06 \x01(\r\x12\x13\n\x0bpassthrough\x18\x07 \x01(\x05\"K\n\x16\x43SVCMsg_PacketReliable\x12\x0c\n\x04tick\x18\x01 \x01(\x05\x12\x14\n\x0cmessagessize\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\x08\"T\n\x16\x43SVCMsg_FullFrameSplit\x12\x0c\n\x04tick\x18\x01 \x01(\x05\x12\x0f\n\x07section\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"U\n\x12\x43SVCMsg_HLTVStatus\x12\x0e\n\x06master\x18\x01 \x01(\t\x12\x0f\n\x07\x63lients\x18\x02 \x01(\x05\x12\r\n\x05slots\x18\x03 \x01(\x05\x12\x0f\n\x07proxies\x18\x04 \x01(\x05\")\n\x15\x43SVCMsg_ServerSteamID\x12\x10\n\x08steam_id\x18\x01 \x01(\x04\"$\n\x14\x43SVCMsg_CmdKeyValues\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\";\n\x19\x43SVCMsg_RconServerDetails\x12\r\n\x05token\x18\x01 \x01(\x0c\x12\x0f\n\x07\x64\x65tails\x18\x02 \x01(\t\";\n\x0e\x43MsgIPCAddress\x12\x15\n\rcomputer_guid\x18\x01 \x01(\x06\x12\x12\n\nprocess_id\x18\x02 \x01(\r\"\xa4\x01\n\x0e\x43MsgServerPeer\x12\x17\n\x0bplayer_slot\x18\x01 \x01(\x05:\x02-1\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\x12\x1c\n\x03ipc\x18\x03 \x01(\x0b\x32\x0f.CMsgIPCAddress\x12\x15\n\rthey_hear_you\x18\x04 \x01(\x08\x12\x15\n\ryou_hear_them\x18\x05 \x01(\x08\x12\x1c\n\x14is_listenserver_host\x18\x06 \x01(\x08\"1\n\x10\x43SVCMsg_PeerList\x12\x1d\n\x04peer\x18\x01 \x03(\x0b\x32\x0f.CMsgServerPeer\"N\n\x1c\x43SVCMsg_ClearAllStringTables\x12\x0f\n\x07mapname\x18\x01 \x01(\t\x12\x1d\n\x15\x63reate_tables_skipped\x18\x03 \x01(\x08\"\xf3\x03\n\x1fProtoFlattenedSerializerField_t\x12\x14\n\x0cvar_type_sym\x18\x01 \x01(\x05\x12\x14\n\x0cvar_name_sym\x18\x02 \x01(\x05\x12\x11\n\tbit_count\x18\x03 \x01(\x05\x12\x11\n\tlow_value\x18\x04 \x01(\x02\x12\x12\n\nhigh_value\x18\x05 \x01(\x02\x12\x14\n\x0c\x65ncode_flags\x18\x06 \x01(\x05\x12!\n\x19\x66ield_serializer_name_sym\x18\x07 \x01(\x05\x12 \n\x18\x66ield_serializer_version\x18\x08 \x01(\x05\x12\x15\n\rsend_node_sym\x18\t \x01(\x05\x12\x17\n\x0fvar_encoder_sym\x18\n \x01(\x05\x12O\n\x11polymorphic_types\x18\x0b \x03(\x0b\x32\x34.ProtoFlattenedSerializerField_t.polymorphic_field_t\x12\x1a\n\x12var_serializer_sym\x18\x0c \x01(\x05\x1ar\n\x13polymorphic_field_t\x12-\n%polymorphic_field_serializer_name_sym\x18\x01 \x01(\x05\x12,\n$polymorphic_field_serializer_version\x18\x02 \x01(\x05\"k\n\x1aProtoFlattenedSerializer_t\x12\x1b\n\x13serializer_name_sym\x18\x01 \x01(\x05\x12\x1a\n\x12serializer_version\x18\x02 \x01(\x05\x12\x14\n\x0c\x66ields_index\x18\x03 \x03(\x05\"\x92\x01\n\x1b\x43SVCMsg_FlattenedSerializer\x12\x30\n\x0bserializers\x18\x01 \x03(\x0b\x32\x1b.ProtoFlattenedSerializer_t\x12\x0f\n\x07symbols\x18\x02 \x03(\t\x12\x30\n\x06\x66ields\x18\x03 \x03(\x0b\x32 .ProtoFlattenedSerializerField_t\"!\n\x11\x43SVCMsg_StopSound\x12\x0c\n\x04guid\x18\x01 \x01(\x07\"y\n\x1e\x43\x42idirMsg_RebroadcastGameEvent\x12\x14\n\x0cposttoserver\x18\x01 \x01(\x08\x12\x0f\n\x07\x62uftype\x18\x02 \x01(\x05\x12\x16\n\x0e\x63lientbitcount\x18\x03 \x01(\r\x12\x18\n\x10receivingclients\x18\x04 \x01(\x04\"2\n\x1b\x43\x42idirMsg_RebroadcastSource\x12\x13\n\x0b\x65ventsource\x18\x01 \x01(\x05\"\x9a\x01\n\x19\x43\x42idirMsg_PredictionEvent\x12\x10\n\x08\x65vent_id\x18\x01 \x02(\r\x12\x12\n\nevent_data\x18\x02 \x02(\x0c\x12\x11\n\tsync_type\x18\x03 \x01(\r\x12\x17\n\x0fsync_val_uint32\x18\x04 \x01(\r\"+\n\tESyncType\x12\x0b\n\x07ST_Tick\x10\x00\x12\x11\n\rST_UserCmdNum\x10\x01\"\xc5\x06\n\x16\x43MsgServerNetworkStats\x12\x11\n\tdedicated\x18\x01 \x01(\x08\x12\x11\n\tcpu_usage\x18\x02 \x01(\x05\x12\x16\n\x0ememory_used_mb\x18\x03 \x01(\x05\x12\x16\n\x0ememory_free_mb\x18\x04 \x01(\x05\x12\x0e\n\x06uptime\x18\x05 \x01(\x05\x12\x13\n\x0bspawn_count\x18\x06 \x01(\x05\x12\x13\n\x0bnum_clients\x18\x08 \x01(\x05\x12\x10\n\x08num_bots\x18\t \x01(\x05\x12\x16\n\x0enum_spectators\x18\n \x01(\x05\x12\x15\n\rnum_tv_relays\x18\x0b \x01(\x05\x12\x0b\n\x03\x66ps\x18\x0c \x01(\x02\x12+\n\x05ports\x18\x11 \x03(\x0b\x32\x1c.CMsgServerNetworkStats.Port\x12\x13\n\x0b\x61vg_ping_ms\x18\x12 \x01(\x02\x12\x1e\n\x16\x61vg_engine_latency_out\x18\x13 \x01(\x02\x12\x17\n\x0f\x61vg_packets_out\x18\x14 \x01(\x02\x12\x16\n\x0e\x61vg_packets_in\x18\x15 \x01(\x02\x12\x14\n\x0c\x61vg_loss_out\x18\x16 \x01(\x02\x12\x13\n\x0b\x61vg_loss_in\x18\x17 \x01(\x02\x12\x14\n\x0c\x61vg_data_out\x18\x18 \x01(\x02\x12\x13\n\x0b\x61vg_data_in\x18\x19 \x01(\x02\x12\x15\n\rtotal_data_in\x18\x1a \x01(\x04\x12\x18\n\x10total_packets_in\x18\x1b \x01(\x04\x12\x16\n\x0etotal_data_out\x18\x1c \x01(\x04\x12\x19\n\x11total_packets_out\x18\x1d \x01(\x04\x12/\n\x07players\x18\x1e \x03(\x0b\x32\x1e.CMsgServerNetworkStats.Player\x1a\"\n\x04Port\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xaa\x01\n\x06Player\x12\x0f\n\x07steamid\x18\x01 \x01(\x04\x12\x13\n\x0bremote_addr\x18\x02 \x01(\t\x12\x13\n\x0bping_avg_ms\x18\x04 \x01(\x05\x12\x17\n\x0fpacket_loss_pct\x18\x05 \x01(\x02\x12\x0e\n\x06is_bot\x18\x06 \x01(\x08\x12\x0f\n\x07loss_in\x18\x07 \x01(\x02\x12\x10\n\x08loss_out\x18\x08 \x01(\x02\x12\x19\n\x11\x65ngine_latency_ms\x18\t \x01(\x05\"\xda\x01\n\x12\x43SVCMsg_HltvReplay\x12\r\n\x05\x64\x65lay\x18\x01 \x01(\x05\x12\x1a\n\x0eprimary_target\x18\x02 \x01(\x05:\x02-1\x12\x16\n\x0ereplay_stop_at\x18\x03 \x01(\x05\x12\x17\n\x0freplay_start_at\x18\x04 \x01(\x05\x12\x1d\n\x15replay_slowdown_begin\x18\x05 \x01(\x05\x12\x1b\n\x13replay_slowdown_end\x18\x06 \x01(\x05\x12\x1c\n\x14replay_slowdown_rate\x18\x07 \x01(\x02\x12\x0e\n\x06reason\x18\x08 \x01(\x05\"\x85\x01\n\x12\x43\x43LCMsg_HltvReplay\x12\x0f\n\x07request\x18\x01 \x01(\x05\x12\x17\n\x0fslowdown_length\x18\x02 \x01(\x02\x12\x15\n\rslowdown_rate\x18\x03 \x01(\x02\x12\x1a\n\x0eprimary_target\x18\x04 \x01(\x05:\x02-1\x12\x12\n\nevent_time\x18\x05 \x01(\x02\"(\n\x19\x43SVCMsg_Broadcast_Command\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\"\xef\x01\n\x1d\x43\x43LCMsg_HltvFixupOperatorTick\x12\x0c\n\x04tick\x18\x01 \x01(\x05\x12\x12\n\nprops_data\x18\x02 \x01(\x0c\x12\x1b\n\x06origin\x18\x03 \x01(\x0b\x32\x0b.CMsgVector\x12\x1f\n\neye_angles\x18\x04 \x01(\x0b\x32\x0b.CMsgQAngle\x12\x15\n\robserver_mode\x18\x05 \x01(\x05\x12\x1c\n\x14\x63\x61meraman_scoreboard\x18\x06 \x01(\x08\x12\x17\n\x0fobserver_target\x18\x07 \x01(\x05\x12 \n\x0bview_offset\x18\x08 \x01(\x0b\x32\x0b.CMsgVector\"O\n\x1f\x43SVCMsg_HltvFixupOperatorStatus\x12\x0c\n\x04mode\x18\x01 \x01(\r\x12\x1e\n\x16override_operator_name\x18\x02 \x01(\t\"\x81\x01\n\x11\x43MsgServerUserCmd\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x12\n\ncmd_number\x18\x02 \x01(\x05\x12\x17\n\x0bplayer_slot\x18\x03 \x01(\x05:\x02-1\x12\x1c\n\x14server_tick_executed\x18\x04 \x01(\x05\x12\x13\n\x0b\x63lient_tick\x18\x05 \x01(\x05\"<\n\x14\x43SVCMsg_UserCommands\x12$\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x12.CMsgServerUserCmd*\xe1\x02\n\x0c\x43LC_Messages\x12\x12\n\x0e\x63lc_ClientInfo\x10\x14\x12\x0c\n\x08\x63lc_Move\x10\x15\x12\x11\n\rclc_VoiceData\x10\x16\x12\x13\n\x0f\x63lc_BaselineAck\x10\x17\x12\x18\n\x14\x63lc_RespondCvarValue\x10\x19\x12\x14\n\x10\x63lc_FileCRCCheck\x10\x1a\x12\x17\n\x13\x63lc_LoadingProgress\x10\x1b\x12\x1a\n\x16\x63lc_SplitPlayerConnect\x10\x1c\x12\x1d\n\x19\x63lc_SplitPlayerDisconnect\x10\x1e\x12\x14\n\x10\x63lc_ServerStatus\x10\x1f\x12\x14\n\x10\x63lc_RequestPause\x10!\x12\x14\n\x10\x63lc_CmdKeyValues\x10\"\x12\x19\n\x15\x63lc_RconServerDetails\x10#\x12\x12\n\x0e\x63lc_HltvReplay\x10$\x12\x12\n\x0e\x63lc_Diagnostic\x10%*\x97\x05\n\x0cSVC_Messages\x12\x12\n\x0esvc_ServerInfo\x10(\x12\x1b\n\x17svc_FlattenedSerializer\x10)\x12\x11\n\rsvc_ClassInfo\x10*\x12\x10\n\x0csvc_SetPause\x10+\x12\x19\n\x15svc_CreateStringTable\x10,\x12\x19\n\x15svc_UpdateStringTable\x10-\x12\x11\n\rsvc_VoiceInit\x10.\x12\x11\n\rsvc_VoiceData\x10/\x12\r\n\tsvc_Print\x10\x30\x12\x0e\n\nsvc_Sounds\x10\x31\x12\x0f\n\x0bsvc_SetView\x10\x32\x12\x1c\n\x18svc_ClearAllStringTables\x10\x33\x12\x14\n\x10svc_CmdKeyValues\x10\x34\x12\x10\n\x0csvc_BSPDecal\x10\x35\x12\x13\n\x0fsvc_SplitScreen\x10\x36\x12\x16\n\x12svc_PacketEntities\x10\x37\x12\x10\n\x0csvc_Prefetch\x10\x38\x12\x0c\n\x08svc_Menu\x10\x39\x12\x14\n\x10svc_GetCvarValue\x10:\x12\x11\n\rsvc_StopSound\x10;\x12\x10\n\x0csvc_PeerList\x10<\x12\x16\n\x12svc_PacketReliable\x10=\x12\x12\n\x0esvc_HLTVStatus\x10>\x12\x15\n\x11svc_ServerSteamID\x10?\x12\x16\n\x12svc_FullFrameSplit\x10\x46\x12\x19\n\x15svc_RconServerDetails\x10G\x12\x13\n\x0fsvc_UserMessage\x10H\x12\x19\n\x15svc_Broadcast_Command\x10J\x12\x1f\n\x1bsvc_HltvFixupOperatorStatus\x10K\x12\x10\n\x0csvc_UserCmds\x10L*g\n\x11VoiceDataFormat_t\x12\x1a\n\x16VOICEDATA_FORMAT_STEAM\x10\x00\x12\x1b\n\x17VOICEDATA_FORMAT_ENGINE\x10\x01\x12\x19\n\x15VOICEDATA_FORMAT_OPUS\x10\x02*B\n\x0eRequestPause_t\x12\x0c\n\x08RP_PAUSE\x10\x00\x12\x0e\n\nRP_UNPAUSE\x10\x01\x12\x12\n\x0eRP_TOGGLEPAUSE\x10\x02*\x1d\n\x0cPrefetchType\x12\r\n\tPFT_SOUND\x10\x00*V\n\x17\x45SplitScreenMessageType\x12\x1b\n\x17MSG_SPLITSCREEN_ADDUSER\x10\x00\x12\x1e\n\x1aMSG_SPLITSCREEN_REMOVEUSER\x10\x01*\xb3\x01\n\x15\x45QueryCvarValueStatus\x12%\n!eQueryCvarValueStatus_ValueIntact\x10\x00\x12&\n\"eQueryCvarValueStatus_CvarNotFound\x10\x01\x12\"\n\x1e\x65QueryCvarValueStatus_NotACvar\x10\x02\x12\'\n#eQueryCvarValueStatus_CvarProtected\x10\x03*h\n\x0b\x44IALOG_TYPE\x12\x0e\n\nDIALOG_MSG\x10\x00\x12\x0f\n\x0b\x44IALOG_MENU\x10\x01\x12\x0f\n\x0b\x44IALOG_TEXT\x10\x02\x12\x10\n\x0c\x44IALOG_ENTRY\x10\x03\x12\x15\n\x11\x44IALOG_ASKCONNECT\x10\x04*+\n\x19SVC_Messages_LowFrequency\x12\x0e\n\tsvc_dummy\x10\xd8\x04*y\n\x16\x42idirectional_Messages\x12\x1b\n\x17\x62i_RebroadcastGameEvent\x10\x10\x12\x18\n\x14\x62i_RebroadcastSource\x10\x11\x12\x10\n\x0c\x62i_GameEvent\x10\x12\x12\x16\n\x12\x62i_PredictionEvent\x10\x13*M\n#Bidirectional_Messages_LowFrequency\x12\x11\n\x0c\x62i_RelayInfo\x10\xbc\x05\x12\x13\n\x0e\x62i_RelayPacket\x10\xbd\x05*\xa1\x01\n\x11ReplayEventType_t\x12\x17\n\x13REPLAY_EVENT_CANCEL\x10\x00\x12\x16\n\x12REPLAY_EVENT_DEATH\x10\x01\x12\x18\n\x14REPLAY_EVENT_GENERIC\x10\x02\x12\'\n#REPLAY_EVENT_STUCK_NEED_FULL_UPDATE\x10\x03\x12\x18\n\x14REPLAY_EVENT_VICTORY\x10\x04')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'netmessages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CMSGVOICEAUDIO.fields_by_name['packet_offsets']._options = None
  _CMSGVOICEAUDIO.fields_by_name['packet_offsets']._serialized_options = b'\020\001'
  _CSVCMSG_PACKETENTITIES.fields_by_name['cmd_recv_status']._options = None
  _CSVCMSG_PACKETENTITIES.fields_by_name['cmd_recv_status']._serialized_options = b'\020\001'
  _CLC_MESSAGES._serialized_start=11149
  _CLC_MESSAGES._serialized_end=11502
  _SVC_MESSAGES._serialized_start=11505
  _SVC_MESSAGES._serialized_end=12168
  _VOICEDATAFORMAT_T._serialized_start=12170
  _VOICEDATAFORMAT_T._serialized_end=12273
  _REQUESTPAUSE_T._serialized_start=12275
  _REQUESTPAUSE_T._serialized_end=12341
  _PREFETCHTYPE._serialized_start=12343
  _PREFETCHTYPE._serialized_end=12372
  _ESPLITSCREENMESSAGETYPE._serialized_start=12374
  _ESPLITSCREENMESSAGETYPE._serialized_end=12460
  _EQUERYCVARVALUESTATUS._serialized_start=12463
  _EQUERYCVARVALUESTATUS._serialized_end=12642
  _DIALOG_TYPE._serialized_start=12644
  _DIALOG_TYPE._serialized_end=12748
  _SVC_MESSAGES_LOWFREQUENCY._serialized_start=12750
  _SVC_MESSAGES_LOWFREQUENCY._serialized_end=12793
  _BIDIRECTIONAL_MESSAGES._serialized_start=12795
  _BIDIRECTIONAL_MESSAGES._serialized_end=12916
  _BIDIRECTIONAL_MESSAGES_LOWFREQUENCY._serialized_start=12918
  _BIDIRECTIONAL_MESSAGES_LOWFREQUENCY._serialized_end=12995
  _REPLAYEVENTTYPE_T._serialized_start=12998
  _REPLAYEVENTTYPE_T._serialized_end=13159
  _CCLCMSG_CLIENTINFO._serialized_start=45
  _CCLCMSG_CLIENTINFO._serialized_end=170
  _CCLCMSG_MOVE._serialized_start=172
  _CCLCMSG_MOVE._serialized_end=229
  _CMSGVOICEAUDIO._serialized_start=232
  _CMSGVOICEAUDIO._serialized_end=503
  _CCLCMSG_VOICEDATA._serialized_start=505
  _CCLCMSG_VOICEDATA._serialized_end=584
  _CCLCMSG_BASELINEACK._serialized_start=586
  _CCLCMSG_BASELINEACK._serialized_end=651
  _CCLCMSG_LISTENEVENTS._serialized_start=653
  _CCLCMSG_LISTENEVENTS._serialized_end=695
  _CCLCMSG_RESPONDCVARVALUE._serialized_start=697
  _CCLCMSG_RESPONDCVARVALUE._serialized_end=789
  _CCLCMSG_FILECRCCHECK._serialized_start=791
  _CCLCMSG_FILECRCCHECK._serialized_end=900
  _CCLCMSG_LOADINGPROGRESS._serialized_start=902
  _CCLCMSG_LOADINGPROGRESS._serialized_end=945
  _CCLCMSG_SPLITPLAYERCONNECT._serialized_start=947
  _CCLCMSG_SPLITPLAYERCONNECT._serialized_end=995
  _CCLCMSG_SPLITPLAYERDISCONNECT._serialized_start=997
  _CCLCMSG_SPLITPLAYERDISCONNECT._serialized_end=1042
  _CCLCMSG_SERVERSTATUS._serialized_start=1044
  _CCLCMSG_SERVERSTATUS._serialized_end=1086
  _CCLCMSG_REQUESTPAUSE._serialized_start=1088
  _CCLCMSG_REQUESTPAUSE._serialized_end=1178
  _CCLCMSG_CMDKEYVALUES._serialized_start=1180
  _CCLCMSG_CMDKEYVALUES._serialized_end=1216
  _CCLCMSG_RCONSERVERDETAILS._serialized_start=1218
  _CCLCMSG_RCONSERVERDETAILS._serialized_end=1260
  _CMSGSOURCE2SYSTEMSPECS._serialized_start=1263
  _CMSGSOURCE2SYSTEMSPECS._serialized_end=1612
  _CMSGSOURCE2VPROFLITEREPORTITEM._serialized_start=1615
  _CMSGSOURCE2VPROFLITEREPORTITEM._serialized_end=2128
  _CMSGSOURCE2VPROFLITEREPORT._serialized_start=2131
  _CMSGSOURCE2VPROFLITEREPORT._serialized_end=2281
  _CMSGSOURCE2NETWORKFLOWQUALITY._serialized_start=2284
  _CMSGSOURCE2NETWORKFLOWQUALITY._serialized_end=3105
  _CCLCMSG_DIAGNOSTIC._serialized_start=3107
  _CCLCMSG_DIAGNOSTIC._serialized_end=3225
  _CSOURCE2METRICS_MATCHPERFSUMMARY_NOTIFICATION._serialized_start=3228
  _CSOURCE2METRICS_MATCHPERFSUMMARY_NOTIFICATION._serialized_end=3611
  _CSOURCE2METRICS_MATCHPERFSUMMARY_NOTIFICATION_CLIENT._serialized_start=3475
  _CSOURCE2METRICS_MATCHPERFSUMMARY_NOTIFICATION_CLIENT._serialized_end=3611
  _CSVCMSG_SERVERINFO._serialized_start=3614
  _CSVCMSG_SERVERINFO._serialized_end=4005
  _CSVCMSG_CLASSINFO._serialized_start=4008
  _CSVCMSG_CLASSINFO._serialized_end=4147
  _CSVCMSG_CLASSINFO_CLASS_T._serialized_start=4100
  _CSVCMSG_CLASSINFO_CLASS_T._serialized_end=4147
  _CSVCMSG_SETPAUSE._serialized_start=4149
  _CSVCMSG_SETPAUSE._serialized_end=4183
  _CSVCMSG_VOICEINIT._serialized_start=4185
  _CSVCMSG_VOICEINIT._serialized_end=4256
  _CSVCMSG_PRINT._serialized_start=4258
  _CSVCMSG_PRINT._serialized_end=4287
  _CSVCMSG_SOUNDS._serialized_start=4290
  _CSVCMSG_SOUNDS._serialized_end=4773
  _CSVCMSG_SOUNDS_SOUNDDATA_T._serialized_start=4378
  _CSVCMSG_SOUNDS_SOUNDDATA_T._serialized_end=4773
  _CSVCMSG_PREFETCH._serialized_start=4775
  _CSVCMSG_PREFETCH._serialized_end=4863
  _CSVCMSG_SETVIEW._serialized_start=4865
  _CSVCMSG_SETVIEW._serialized_end=4926
  _CSVCMSG_FIXANGLE._serialized_start=4928
  _CSVCMSG_FIXANGLE._serialized_end=4992
  _CSVCMSG_CROSSHAIRANGLE._serialized_start=4994
  _CSVCMSG_CROSSHAIRANGLE._serialized_end=5046
  _CSVCMSG_BSPDECAL._serialized_start=5049
  _CSVCMSG_BSPDECAL._serialized_end=5191
  _CSVCMSG_SPLITSCREEN._serialized_start=5193
  _CSVCMSG_SPLITSCREEN._serialized_end=5319
  _CSVCMSG_GETCVARVALUE._serialized_start=5321
  _CSVCMSG_GETCVARVALUE._serialized_end=5378
  _CSVCMSG_MENU._serialized_start=5380
  _CSVCMSG_MENU._serialized_end=5440
  _CSVCMSG_USERMESSAGE._serialized_start=5442
  _CSVCMSG_USERMESSAGE._serialized_end=5520
  _CSVCMSG_SENDTABLE._serialized_start=5523
  _CSVCMSG_SENDTABLE._serialized_end=5827
  _CSVCMSG_SENDTABLE_SENDPROP_T._serialized_start=5654
  _CSVCMSG_SENDTABLE_SENDPROP_T._serialized_end=5827
  _CSVCMSG_GAMEEVENTLIST._serialized_start=5830
  _CSVCMSG_GAMEEVENTLIST._serialized_end=6039
  _CSVCMSG_GAMEEVENTLIST_KEY_T._serialized_start=5913
  _CSVCMSG_GAMEEVENTLIST_KEY_T._serialized_end=5948
  _CSVCMSG_GAMEEVENTLIST_DESCRIPTOR_T._serialized_start=5950
  _CSVCMSG_GAMEEVENTLIST_DESCRIPTOR_T._serialized_end=6039
  _CSVCMSG_PACKETENTITIES._serialized_start=6042
  _CSVCMSG_PACKETENTITIES._serialized_end=6899
  _CSVCMSG_PACKETENTITIES_ALTERNATE_BASELINE_T._serialized_start=6765
  _CSVCMSG_PACKETENTITIES_ALTERNATE_BASELINE_T._serialized_end=6833
  _CSVCMSG_PACKETENTITIES_NON_TRANSMITTED_ENTITIES_T._serialized_start=6835
  _CSVCMSG_PACKETENTITIES_NON_TRANSMITTED_ENTITIES_T._serialized_end=6899
  _CSVCMSG_TEMPENTITIES._serialized_start=6901
  _CSVCMSG_TEMPENTITIES._serialized_end=6983
  _CSVCMSG_CREATESTRINGTABLE._serialized_start=6986
  _CSVCMSG_CREATESTRINGTABLE._serialized_end=7251
  _CSVCMSG_UPDATESTRINGTABLE._serialized_start=7253
  _CSVCMSG_UPDATESTRINGTABLE._serialized_end=7348
  _CSVCMSG_VOICEDATA._serialized_start=7351
  _CSVCMSG_VOICEDATA._serialized_end=7512
  _CSVCMSG_PACKETRELIABLE._serialized_start=7514
  _CSVCMSG_PACKETRELIABLE._serialized_end=7589
  _CSVCMSG_FULLFRAMESPLIT._serialized_start=7591
  _CSVCMSG_FULLFRAMESPLIT._serialized_end=7675
  _CSVCMSG_HLTVSTATUS._serialized_start=7677
  _CSVCMSG_HLTVSTATUS._serialized_end=7762
  _CSVCMSG_SERVERSTEAMID._serialized_start=7764
  _CSVCMSG_SERVERSTEAMID._serialized_end=7805
  _CSVCMSG_CMDKEYVALUES._serialized_start=7807
  _CSVCMSG_CMDKEYVALUES._serialized_end=7843
  _CSVCMSG_RCONSERVERDETAILS._serialized_start=7845
  _CSVCMSG_RCONSERVERDETAILS._serialized_end=7904
  _CMSGIPCADDRESS._serialized_start=7906
  _CMSGIPCADDRESS._serialized_end=7965
  _CMSGSERVERPEER._serialized_start=7968
  _CMSGSERVERPEER._serialized_end=8132
  _CSVCMSG_PEERLIST._serialized_start=8134
  _CSVCMSG_PEERLIST._serialized_end=8183
  _CSVCMSG_CLEARALLSTRINGTABLES._serialized_start=8185
  _CSVCMSG_CLEARALLSTRINGTABLES._serialized_end=8263
  _PROTOFLATTENEDSERIALIZERFIELD_T._serialized_start=8266
  _PROTOFLATTENEDSERIALIZERFIELD_T._serialized_end=8765
  _PROTOFLATTENEDSERIALIZERFIELD_T_POLYMORPHIC_FIELD_T._serialized_start=8651
  _PROTOFLATTENEDSERIALIZERFIELD_T_POLYMORPHIC_FIELD_T._serialized_end=8765
  _PROTOFLATTENEDSERIALIZER_T._serialized_start=8767
  _PROTOFLATTENEDSERIALIZER_T._serialized_end=8874
  _CSVCMSG_FLATTENEDSERIALIZER._serialized_start=8877
  _CSVCMSG_FLATTENEDSERIALIZER._serialized_end=9023
  _CSVCMSG_STOPSOUND._serialized_start=9025
  _CSVCMSG_STOPSOUND._serialized_end=9058
  _CBIDIRMSG_REBROADCASTGAMEEVENT._serialized_start=9060
  _CBIDIRMSG_REBROADCASTGAMEEVENT._serialized_end=9181
  _CBIDIRMSG_REBROADCASTSOURCE._serialized_start=9183
  _CBIDIRMSG_REBROADCASTSOURCE._serialized_end=9233
  _CBIDIRMSG_PREDICTIONEVENT._serialized_start=9236
  _CBIDIRMSG_PREDICTIONEVENT._serialized_end=9390
  _CBIDIRMSG_PREDICTIONEVENT_ESYNCTYPE._serialized_start=9347
  _CBIDIRMSG_PREDICTIONEVENT_ESYNCTYPE._serialized_end=9390
  _CMSGSERVERNETWORKSTATS._serialized_start=9393
  _CMSGSERVERNETWORKSTATS._serialized_end=10230
  _CMSGSERVERNETWORKSTATS_PORT._serialized_start=10023
  _CMSGSERVERNETWORKSTATS_PORT._serialized_end=10057
  _CMSGSERVERNETWORKSTATS_PLAYER._serialized_start=10060
  _CMSGSERVERNETWORKSTATS_PLAYER._serialized_end=10230
  _CSVCMSG_HLTVREPLAY._serialized_start=10233
  _CSVCMSG_HLTVREPLAY._serialized_end=10451
  _CCLCMSG_HLTVREPLAY._serialized_start=10454
  _CCLCMSG_HLTVREPLAY._serialized_end=10587
  _CSVCMSG_BROADCAST_COMMAND._serialized_start=10589
  _CSVCMSG_BROADCAST_COMMAND._serialized_end=10629
  _CCLCMSG_HLTVFIXUPOPERATORTICK._serialized_start=10632
  _CCLCMSG_HLTVFIXUPOPERATORTICK._serialized_end=10871
  _CSVCMSG_HLTVFIXUPOPERATORSTATUS._serialized_start=10873
  _CSVCMSG_HLTVFIXUPOPERATORSTATUS._serialized_end=10952
  _CMSGSERVERUSERCMD._serialized_start=10955
  _CMSGSERVERUSERCMD._serialized_end=11084
  _CSVCMSG_USERCOMMANDS._serialized_start=11086
  _CSVCMSG_USERCOMMANDS._serialized_end=11146
# @@protoc_insertion_point(module_scope)
