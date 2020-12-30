host='http://192.168.1.117/kw/'
headers = {
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) yunji/0.0.1 Chrome/76.0.3809.146 Electron/6.1.12 Safari/537.36',
}
#loginApi
wholeURl='admin/signin/'
data1={"username":"admin","password":"adminadmin"}
data2={"username":"admin","password":"admin"}
data3={"username":"Admin","password":"adminadmin"}
data4={"username":"admin","password":"123456"}
#rebuid_member_a_list

#upload_file
wu='api/resources/uploadsignature/'
data={"type":2,"extension":"png"}
#wholeURl_upload
wholeURl_upload='admin/procedures/6bb9f788-cb02-11ea-a2d1-38f9d355d676/extends/'
dataUploa={"procedure_id":"6bb9f788-cb02-11ea-a2d1-38f9d355d676","type":8,"values":[{"resource_key":"sa_procedure/2ef6c8fa-0d04-11eb-92d4-0242ac190005.png","name":"logo.33b66427.png"},{"resource_key":"sa_procedure/31b5f472-0f60-11eb-92d4-0242ac190005.png","name":"logo.33b66427.png"}]}
# upload_file_data
host1='http://192.168.1.117:9001/'
upload_file_data_url='inspection/sa_procedure/76d6a1d0-11b0-11eb-92d4-0242ac190005.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20201019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201019T021157Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=50754a75b673ece0a11b9b649c8b346a64bb4f4ffe9c38f050ed50353b0fc2a1'
# new_rebuited_worksheet
new_rebuited_data_url='inspection/sa_rail_work_sheet_remark/1c9aea2c-11bb-11eb-9511-0242ac190005.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20201019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201019T032810Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4739fd6b96c853e8da208f4f65f9462ae4d39a327e75f70c07451c580a7f3d96'
duty_url='desktop/inspection_sheets/field_values/?page=1&page_size=100'
duty_data='{"data":{"count":56,"next":null,"previous":null,"results":[{"label":"4534driver","value":"driver","extras":[]},{"label":"俄是","value":"wanger","extras":[]},{"label":"司机一","value":"dv1","extras":[]},{"label":"司机二","value":"dv2","extras":[]},{"label":"司机老王","value":"driver1","extras":[]},{"label":"唐一","value":"smt1","extras":[]},{"label":"唐三","value":"smt3","extras":[]},{"label":"唐二","value":"smt2","extras":[]},{"label":"唐五","value":"smt5","extras":[]},{"label":"唐六","value":"smt6","extras":[]},{"label":"唐四","value":"smt4","extras":[]},{"label":"李一","value":"lyc1","extras":[]},{"label":"李七","value":"lyc7","extras":[]},{"label":"李三","value":"lyc3","extras":[]},{"label":"李二","value":"lyc2","extras":[]},{"label":"李五","value":"lyc5","extras":[]},{"label":"李八","value":"lyc8","extras":[]},{"label":"李六","value":"lyc6","extras":[]},{"label":"李四","value":"lyc4","extras":[]},{"label":"杜一","value":"dyy1","extras":[]},{"label":"杜三","value":"dyy3","extras":[]},{"label":"杜二","value":"dyy2","extras":[]},{"label":"杜五","value":"dyy5","extras":[]},{"label":"杜四","value":"dyy4","extras":[]},{"label":"杨一","value":"ybx1","extras":[]},{"label":"杨一一","value":"yang1","extras":[]},{"label":"杨三","value":"ybx3","extras":[]},{"label":"杨二","value":"ybx2","extras":[]},{"label":"杨二二","value":"yang2","extras":[]},{"label":"测一","value":"test1","extras":[]},{"label":"测七","value":"test7","extras":[]},{"label":"测三","value":"test3","extras":[]},{"label":"测九九","value":"ybx4","extras":[]},{"label":"测二","value":"test2","extras":[]},{"label":"测五","value":"test5","extras":[]},{"label":"测八","value":"test8","extras":[]},{"label":"测六","value":"test6","extras":[]},{"label":"测十九","value":"18KL0034","extras":[]},{"label":"测四","value":"test4","extras":[]},{"label":"王一","value":"wy1","extras":[]},{"label":"王三","value":"wy3","extras":[]},{"label":"王二","value":"wy2","extras":[]},{"label":"胡一","value":"8bc27a7e92952c05478df971de7a8dd0","extras":[]},{"label":"胡三","value":"f2af440281a5bf7fc6db110e97838046","extras":[]},{"label":"胡二","value":"d642d41569da60fb05efd53cd03a5174","extras":[]},{"label":"赖一","value":"lxm1","extras":[]},{"label":"赖三","value":"lxm3","extras":[]},{"label":"赖二","value":"lxm2","extras":[]},{"label":"赖五","value":"lxm","extras":[]},{"label":"赖四","value":"lxm4","extras":[]},{"label":"陈一","value":"xmj1","extras":[]},{"label":"陈三","value":"xmj3","extras":[]},{"label":"陈二","value":"xmj2","extras":[]},{"label":"陈五","value":"xmj5","extras":[]},{"label":"陈四","value":"xmj4","extras":[]},{"label":"黄一","value":"hxh","extras":[]}]}}'
# editor_userinfor
editor_userinfor_host='admin/users/f941f6d6-fd76-11ea-aaac-0242ac190005/'
editor_userinfor_data={"username":"fdca1ef55eadbfe2707aea9f36f6b15a","password":"","last_name":"","first_name":"手机二","mobile":"","id_number":"111111111111111111","bind_devices":[]}
#work_setting_add_meterail
add_meterail_host='admin/procedures/eba533a6-11be-11eb-b6ca-0242ac190005/extends/'
add_meterail_data={"procedure_id":"eba533a6-11be-11eb-b6ca-0242ac190005","type":0,
                   "values":["{\"name\":\"das\",\"unit\":\"adas\",\"count\":\"asda\",\"id\":\"1du6scrjcyy\"}",
                            {"name":"sdas","unit":"asd ","count":"asd a","id":"znr1hj8q9c"}     ]}
#videoUpload
videouploadurl_host='desktop/work_videos/'
videouploadurl_data='desktop/work_videos/'
videouploadurl_list_host='desktop/work_videos/?form_id=null&page=1&page_size=20'
