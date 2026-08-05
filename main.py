"""

  fb login method by CURL-XD 

  !!! 

  this method is working but you need to change username and password and ;
  also need to change some values in headers and data to make it work for you.
  
  !!!
   
"""

import requests, time

username = "your email/uid/username here"
password = f"#PWD_FB4A:0:{int(time.time())}:your_password_here"

headers = {
    'host': 'b-graph.facebook.com',
    'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"graphservice"}',
    'x-fb-rmd': 'state=URL_ELIGIBLE',
    'priority': 'u=0',
    'content-encoding': 'gzip',
    'x-zero-eh': '664c0faaac849cb891d0a261fbb72a12',
    'user-agent': '[FBAN/FB4A;FBAV/573.0.0.37.74;FBBV/1032159026;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/Grameenphone;FBMF/ROG;FBBD/ROG;FBPN/com.facebook.katana;FBDV/ASUS_AI2401_A;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'x-zero-f-device-id': '8ebfc41c-752d-449e-bf2c-ad76ec92671e',
    'x-graphql-request-purpose': 'fetch',
    'x-fb-device-group': '1553',
    'x-tigon-is-retry': 'False',
    'x-graphql-client-library': 'graphservice',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-net-hni': '47001',
    'x-fb-sim-hni': '47001',
    'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'x-zero-state': 'unknown',
    'x-meta-zca': 'empty_token',
    'app-scope-id-header': '6a753899-774d-4217-bd4d-dc49a2305764',
    'x-fb-connection-type': 'WIFI',
    'x-meta-usdid': '3fef71eb-692f-4084-902d-26f7c19605a2.1785974939.MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAESRd5kN_OKpW3Jc8dE34XbRtt7Oe8antHjX_5aE_tsUE76ajDio6GS1blXl764Clqx1NTCojrv8wN0UNF2hOgIw.MEQCIFT8Fdg-_McDFHVPQyaYi1zbz685AM791S4OsEWzidz7AiAc86EVRNWxKfFEQGf_lib12YSuuxHLdRQHolna1qmwEA',
    # 'accept-encoding': 'gzip, deflate',
    'x-fb-http-engine': 'Tigon/Liger',
    'x-fb-client-ip': 'True',
    'x-fb-server-cluster': 'True',
    'x-fb-conn-uuid-client': 'pK9gblQP4/RILcf8HaY0bg==',
}

data = {
    'method': 'post',
    'format': 'json',
    'server_timestamps': 'true',
    'locale': 'en_US',
    'purpose': 'fetch',
    'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'fb_api_caller_class': 'graphservice',
    'client_doc_id': '119940804210317832728820035388',
    'fb_api_client_context': '{"is_background":false}',
    'variables': '{"params":{"params":"{\\"params\\":\\"{\\\\\\"client_input_params\\\\\\":{\\\\\\"blocked_uids\\\\\\":[],\\\\\\"aac\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"aac_init_timestamp\\\\\\\\\\\\\\":1785971326,\\\\\\\\\\\\\\"aacjid\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"b7701724-e62a-4c75-bf5f-7c246f9e3ce3\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"aaccs\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"oQhlpPzSRK88EDV79aqOpqXSh3zZOgIggb9RrLv5e78\\\\\\\\\\\\\\"}\\\\\\",\\\\\\"sim_phones\\\\\\":[],\\\\\\"aymh_accounts\\\\\\":[{\\\\\\"profiles\\\\\\":{\\\\\\"id\\\\\\":{\\\\\\"is_derived\\\\\\":0,\\\\\\"credentials\\\\\\":[],\\\\\\"account_center_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"profile_picture_url\\\\\\":\\\\\\"\\\\\\",\\\\\\"small_profile_picture_url\\\\\\":null,\\\\\\"notification_count\\\\\\":0,\\\\\\"token\\\\\\":\\\\\\"\\\\\\",\\\\\\"last_access_time\\\\\\":0,\\\\\\"has_smartlock\\\\\\":0,\\\\\\"credential_type\\\\\\":\\\\\\"none\\\\\\",\\\\\\"password\\\\\\":\\\\\\"\\\\\\",\\\\\\"from_accurate_privacy_result\\\\\\":0,\\\\\\"dbln_validated\\\\\\":0,\\\\\\"user_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"name\\\\\\":\\\\\\"\\\\\\",\\\\\\"nta_eligibility_reason\\\\\\":null,\\\\\\"username\\\\\\":\\\\\\"\\\\\\",\\\\\\"account_source\\\\\\":\\\\\\"\\\\\\"}},\\\\\\"id\\\\\\":\\\\\\"\\\\\\"}],\\\\\\"network_bssid\\\\\\":null,\\\\\\"secure_family_device_id\\\\\\":\\\\\\"9cfa6396-fbf2-4724-ba71-3ff43a01cff7\\\\\\",\\\\\\"attestation_result\\\\\\":{\\\\\\"keyHash\\\\\\":\\\\\\"b9f79472dfef3a352ef27fb799e4c1c03a276d8b893cd99252b1bdc182f35621\\\\\\",\\\\\\"data\\\\\\":\\\\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiJyMzVoMnlobnZ2Y2NrcVZoWldzdmhjdEVLV0dYYTA4T2thRGtUZWs4OTdFPSIsInVzZXJuYW1lIjoiaW1yYW4ifQ==\\\\\\",\\\\\\"signature\\\\\\":\\\\\\"MEUCIFZazzTELeg2LXWYF0pTKP8VNZkTUhTIn01Pv5chR1GHAiEA4K2QpPxIVyjoTd+qyd7kLPfLgCf+4aIoN5b0LBYchps=\\\\\\"},\\\\\\"has_granted_read_contacts_permissions\\\\\\":0,\\\\\\"auth_secure_device_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"has_whatsapp_installed\\\\\\":0,\\\\\\"si_device_param_network_info\\\\\\":{\\\\\\"active_subscriptions_info\\\\\\":null,\\\\\\"default_subscription_info\\\\\\":{\\\\\\"network_type\\\\\\":null,\\\\\\"is_data_roaming\\\\\\":1,\\\\\\"is_esim\\\\\\":null,\\\\\\"is_gsm_roaming\\\\\\":0,\\\\\\"is_sim_sms_capable\\\\\\":null,\\\\\\"is_mobile_data_enabled\\\\\\":1,\\\\\\"sim_carrier_id\\\\\\":1362,\\\\\\"sim_carrier_id_name\\\\\\":null,\\\\\\"sim_state\\\\\\":5,\\\\\\"sim_operator\\\\\\":\\\\\\"47001\\\\\\",\\\\\\"sim_operator_name\\\\\\":\\\\\\"GrameenPhone+Ltd\\\\\\",\\\\\\"signal_strength\\\\\\":null,\\\\\\"group_id_level_1\\\\\\":null,\\\\\\"network_operator\\\\\\":\\\\\\"47001\\\\\\"},\\\\\\"is_airplane_mode\\\\\\":0,\\\\\\"is_active_network_cellular\\\\\\":0,\\\\\\"is_device_sms_capable\\\\\\":1,\\\\\\"sim_count\\\\\\":1,\\\\\\"is_wifi\\\\\\":1},\\\\\\"password\\\\\\":\\\\\\"'+password+'\\\\\\",\\\\\\"sso_token_map_json_string\\\\\\":\\\\\\"\\\\\\",\\\\\\"block_store_machine_id\\\\\\":null,\\\\\\"cloud_trust_token\\\\\\":null,\\\\\\"event_flow\\\\\\":\\\\\\"login_manual\\\\\\",\\\\\\"password_contains_non_ascii\\\\\\":\\\\\\"false\\\\\\",\\\\\\"sim_serials\\\\\\":[],\\\\\\"client_known_key_hash\\\\\\":\\\\\\"\\\\\\",\\\\\\"sso_accounts_auth_data\\\\\\":[],\\\\\\"encrypted_msisdn\\\\\\":\\\\\\"\\\\\\",\\\\\\"has_granted_read_phone_permissions\\\\\\":0,\\\\\\"app_manager_id\\\\\\":\\\\\\"null\\\\\\",\\\\\\"should_show_nested_nta_from_aymh\\\\\\":0,\\\\\\"device_id\\\\\\":\\\\\\"6a753899-774d-4217-bd4d-dc49a2305764\\\\\\",\\\\\\"zero_balance_state\\\\\\":\\\\\\"init\\\\\\",\\\\\\"login_attempt_count\\\\\\":1,\\\\\\"machine_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"flash_call_permission_status\\\\\\":{\\\\\\"READ_PHONE_STATE\\\\\\":\\\\\\"DENIED\\\\\\",\\\\\\"READ_CALL_LOG\\\\\\":\\\\\\"DENIED\\\\\\",\\\\\\"ANSWER_PHONE_CALLS\\\\\\":\\\\\\"DENIED\\\\\\"},\\\\\\"accounts_list\\\\\\":[],\\\\\\"gms_incoming_call_retriever_eligibility\\\\\\":\\\\\\"not_eligible\\\\\\",\\\\\\"family_device_id\\\\\\":\\\\\\"8ebfc41c-752d-449e-bf2c-ad76ec92671e\\\\\\",\\\\\\"fb_ig_device_id\\\\\\":[],\\\\\\"device_emails\\\\\\":[],\\\\\\"try_num\\\\\\":1,\\\\\\"lois_settings\\\\\\":{\\\\\\"lois_token\\\\\\":\\\\\\"\\\\\\"},\\\\\\"event_step\\\\\\":\\\\\\"home_page\\\\\\",\\\\\\"headers_infra_flow_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"openid_tokens\\\\\\":{},\\\\\\"contact_point\\\\\\":\\\\\\"'+username+'\\\\\\"},\\\\\\"server_params\\\\\\":{\\\\\\"should_trigger_override_login_2fa_action\\\\\\":0,\\\\\\"is_from_logged_out\\\\\\":0,\\\\\\"should_trigger_override_login_success_action\\\\\\":0,\\\\\\"login_credential_type\\\\\\":\\\\\\"none\\\\\\",\\\\\\"server_login_source\\\\\\":\\\\\\"login\\\\\\",\\\\\\"waterfall_id\\\\\\":\\\\\\"dcaccd24-f922-4ec7-8e87-ebcf3f09bcdf\\\\\\",\\\\\\"two_step_login_type\\\\\\":\\\\\\"one_step_login\\\\\\",\\\\\\"login_source\\\\\\":\\\\\\"Login\\\\\\",\\\\\\"is_platform_login\\\\\\":0,\\\\\\"pw_encryption_try_count\\\\\\":1,\\\\\\"login_entry_point\\\\\\":\\\\\\"logged_out\\\\\\",\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\":36707139,\\\\\\"is_from_aymh\\\\\\":0,\\\\\\"offline_experiment_group\\\\\\":\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\",\\\\\\"is_from_landing_page\\\\\\":0,\\\\\\"left_nav_button_action\\\\\\":\\\\\\"BACK\\\\\\",\\\\\\"password_text_input_id\\\\\\":\\\\\\"p81ykq:107\\\\\\",\\\\\\"is_from_empty_password\\\\\\":0,\\\\\\"is_from_msplit_fallback\\\\\\":0,\\\\\\"ar_event_source\\\\\\":\\\\\\"login_home_page\\\\\\",\\\\\\"username_text_input_id\\\\\\":\\\\\\"p81ykq:106\\\\\\",\\\\\\"layered_homepage_experiment_group\\\\\\":null,\\\\\\"device_id\\\\\\":\\\\\\"6a753899-774d-4217-bd4d-dc49a2305764\\\\\\",\\\\\\"login_surface\\\\\\":\\\\\\"login_home\\\\\\",\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\":152518279400779,\\\\\\"reg_flow_source\\\\\\":\\\\\\"lid_landing_screen\\\\\\",\\\\\\"is_caa_perf_enabled\\\\\\":1,\\\\\\"credential_type\\\\\\":\\\\\\"password\\\\\\",\\\\\\"is_from_password_entry_page\\\\\\":0,\\\\\\"caller\\\\\\":\\\\\\"gslr\\\\\\",\\\\\\"family_device_id\\\\\\":\\\\\\"8ebfc41c-752d-449e-bf2c-ad76ec92671e\\\\\\",\\\\\\"is_from_assistive_id\\\\\\":0,\\\\\\"access_flow_version\\\\\\":\\\\\\"pre_mt_behavior\\\\\\",\\\\\\"is_from_logged_in_switcher\\\\\\":0}}\\"}","bloks_versioning_id":"b63bcccd91c16cc71c83f742a3e37107f36e5b7b6974c9c16fa21bda3d124019","app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"},"scale":"2","nt_context":{"using_white_navbar":true,"styles_id":"a07b73c926a84224348806e6cd486365","pixel_ratio":2,"is_push_on":true,"is_flipper_enabled":false,"android_device_performance_class":null,"debug_tooling_metadata_token":null,"gpu_memory_mb":256,"theme_params":[{"value":[],"design_system_name":"FDS"}],"bloks_version":"b63bcccd91c16cc71c83f742a3e37107f36e5b7b6974c9c16fa21bda3d124019","android_os_api_level":28}}',
    'fb_api_analytics_tags': '["GraphServices"]',
    'client_trace_id': 'ea8a7c7e-5772-4cc8-8d51-fe618450939e',
}

response = requests.post('https://b-graph.facebook.com/graphql', headers=headers, data=data).text
print(response)
