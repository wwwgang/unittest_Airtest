# coding=utf8

import os, glob

'''通用配置'''
report_path = os.path.dirname(__file__) + '/report.html'

out_files = 'log.html'

# 老后台的
Authorization = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkZTRjZDgwMzMwY2ExODRlZGQwNGVlOSIsImlhdCI6MTU4MDg4NTI4NywiZXhwIjoxNTgyMDk0ODg3fQ.BUK91kbngeAiUaCh1ncDikc-o2iKWBAdZmUKYQeEAW8'
ShadowAuthorization = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkZTRjZDgwMzMwY2ExODRlZGQwNGVlOSIsImlhdCI6MTU4MDg4NTI4NywiZXhwIjoxNTgyMDk0ODg3fQ.BUK91kbngeAiUaCh1ncDikc-o2iKWBAdZmUKYQeEAW8'
# 新后台的
onionsToken = r'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkZTRjZDgwMzMwY2ExODRlZGQwNGVlOSIsImlhdCI6MTU4MTA1ODQ3MywiZXhwIjoxNTgyMjY4MDczfQ.I5c3kQT_NTXMV0eC7IDm88fXC5CaQ9zxivQlroPx-H8'
shadowToken = r'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkZTRjZDgwMzMwY2ExODRlZGQwNGVlOSIsImlhdCI6MTU4MTA1ODQ3MywiZXhwIjoxNTgyMjY4MDczfQ.I5c3kQT_NTXMV0eC7IDm88fXC5CaQ9zxivQlroPx-H8'
persist_root = r'{"routing":"{\"location\":{\"pathname\":\"/\",\"search\":\"\",\"hash\":\"\",\"query\":{},\"key\":\"mp6u6t\"}}","@@dva":"0","activities":"{\"goodsListById\":{},\"goodsIds\":[],\"risksListById\":{},\"risksIds\":[],\"activityMeta\":{},\"allGoodsListById\":{},\"allGoodsIds\":[]}","admission":"{\"admissionListById\":{},\"admissionIds\":[],\"curAdmissionDetailList\":[],\"enrollmentPlanList\":[],\"activityPageById\":{},\"activityPageIds\":[],\"admissionDetailListById\":{},\"admissionDetailIds\":[],\"gradePublisherList\":{},\"courseListById\":{},\"courseIds\":[],\"commodityListById\":{},\"commodityIds\":[],\"classListById\":{},\"classIds\":[]}","agentRebate":"{\"commodityListById\":{},\"commodityIds\":[],\"curAgentRebateConfig\":{},\"agentRebateLogList\":[],\"internalCommissionLogList\":[]}","agentUrl":"{\"agentUrlListById\":{},\"agentUrlIds\":[],\"agentSchollById\":{},\"agentSchollIds\":[]}","channel":"{\"originLinkList\":[],\"agentList\":[],\"firstChannelList\":[],\"secondChannelList\":[],\"thirdChannelList\":[],\"agentUrlList\":[],\"channelList\":[],\"codeList\":[],\"originLinkCount\":0,\"promotionCount\":0,\"channelCount\":0,\"codeCount\":0}","classManage":"{\"typeList\":[],\"gradeList\":[],\"classList\":[],\"totalCount\":0,\"wxInfoList\":[],\"volumeList\":[],\"allPublisherId\":[],\"oneClassInfo\":{\"description\":\"\",\"endTime\":\"\",\"grade\":\"\",\"invalidTime\":\"\",\"isPost\":true,\"name\":\"\",\"startTime\":\"\",\"stopTime\":\"\",\"studentCount\":180,\"type\":\"\",\"learnPlanId\":\"\"},\"userIdsByClassId\":{},\"userListByUserId\":{},\"goalInfoByClassId\":{},\"recordListByUserId\":{},\"courseListByClassId\":{},\"selectUserId\":\"\",\"notConvertReasonsList\":[],\"intentionList\":[],\"userScoreList\":[],\"channelList\":[],\"changeCourseTotalCount\":0,\"smsTemplateById\":{},\"smsTemplateIdsByClassId\":{},\"planListIds\":[],\"planListItemById\":{},\"userDataByClassId\":{},\"userCourseFinishByUserId\":{}}","configure":"{\"totalCount\":0,\"weChatInfoIds\":[],\"weChatInfoById\":{},\"wechatRuleListIds\":[],\"wechatRuleListById\":{}}","course":"{\"unlockIds\":[],\"coursePkgs\":[],\"chapterList\":[],\"middleSemesters\":[],\"specialCourse\":{\"levels\":[],\"id\":\"\",\"name\":\"\",\"type\":\"\"},\"createData\":{\"name\":\"\",\"courses\":[],\"allWeek\":0,\"unlockMode\":\"\",\"semesterId\":\"\",\"publisherId\":\"\",\"isMultiProblems\":true},\"unlockItemById\":{},\"courseItemById\":{},\"courseIds\":[],\"courseCount\":0}","exercises":"{\"exerciseListById\":{},\"userFinishByUserId\":{},\"goalListByCourseId\":{},\"courseListByCourseId\":{},\"userIdsByCourseId\":{},\"exerciseStates\":[{\"key\":\"uncommitted\",\"value\":\"未提交\"},{\"key\":\"notCorrected\",\"value\":\"未批改\"},{\"key\":\"corrected\",\"value\":\"已批改\"}],\"exerciseScores\":[{\"key\":\"5\",\"value\":\"优秀\"}],\"selCourseId\":\"\",\"selUserId\":\"\",\"selExerciseId\":\"\",\"selTopicId\":\"\",\"exerciseCount\":0,\"focusGoal\":false}","global":"{\"notices\":[],\"collapsed\":true,\"semesterIds\":[],\"allPublisherIds\":[],\"semesterItemById\":{},\"allPublisherItemById\":{}}","learningPlan":"{\"learningPlanCount\":0,\"learningPlanIds\":[],\"learningPlanById\":{},\"learnPlanBase\":{\"name\":\"\",\"allNum\":0,\"curriculumId\":\"\"},\"learnPlanDetails\":[],\"checkedCourseName\":\"\",\"checkedCourseTopics\":[]}","login":"{}","materials":"{\"totalCount\":0,\"materialsIds\":[],\"materialInfoById\":{}}","resources":"{\"bannerListById\":{},\"bannerIds\":[],\"popupListById\":{},\"popupIds\":[]}","settings":"{\"navTheme\":\"dark\",\"primaryColor\":\"#1890FF\",\"layout\":\"sidemenu\",\"contentWidth\":\"Fluid\",\"fixedHeader\":false,\"autoHideHeader\":false,\"fixSiderbar\":false,\"colorWeak\":false,\"menu\":{\"locale\":true},\"title\":\"洋葱数学-小学\",\"pwa\":false,\"iconfontUrl\":\"\"}","user":"{\"id\":\"5de4cd80330ca184edd04ee9\",\"name\":\"王刚\",\"mail\":\"wanggang_test@guanghe.tv\",\"username\":\"wanggang_test\",\"roles\":[\"shadow_primarySchool_course_all\",\"shadow_primarySchool_class_searchAll\",\"shadow_primarySchool_class_searchPersonal\",\"shadow_primarySchool_activationCode_all\",\"shadow_primarySchool_customMenu_all\",\"shadow_primarySchool_autoResponseServiceNum_all\",\"shadow_primarySchool_customTemplate_all\",\"shadow_primarySchool_config_manager\",\"shadow_primarySchool_questionnaire_investigation\",\"shadow_primarySchool_referral_activities\",\"shadow_primarySchool_custom_template\",\"shadow_primarySchool_customerService_message\",\"shadow_primarySchool_search_allClasses\",\"shadow_primarySchool_search_ownClasses\",\"shadow_primarySchool_invalid_Invaliduser\",\"shadow_primarySchool_coupon_all\",\"shadow_primarySchool_operate_management\",\"shadow_primarySchool_sponsored_links\",\"shadow_primarySchool_origin_links\",\"shadow_primarySchool_code_management\",\"shadow_primarySchool_channel_management\",\"shadow_primarySchool_banner_management\",\"shadow_primarySchool_send_groupMessage\",\"shadow_primarySchool_find_verificationCode\",\"shadow_primarySchool_configCenter_customerServiceMessage\",\"shadow_primarySchool_distributionActivity_risk\"]}","loading":"{\"global\":false,\"models\":{\"user\":false},\"effects\":{\"user/login\":false}}","_persist":"{\"version\":-1,\"rehydrated\":true}"}'
antd_pro_authority = r'["shadow_primarySchool_course_all","shadow_primarySchool_class_searchAll","shadow_primarySchool_class_searchPersonal","shadow_primarySchool_activationCode_all","shadow_primarySchool_customMenu_all","shadow_primarySchool_autoResponseServiceNum_all","shadow_primarySchool_customTemplate_all","shadow_primarySchool_config_manager","shadow_primarySchool_questionnaire_investigation","shadow_primarySchool_referral_activities","shadow_primarySchool_custom_template","shadow_primarySchool_customerService_message","shadow_primarySchool_search_allClasses","shadow_primarySchool_search_ownClasses","shadow_primarySchool_invalid_Invaliduser","shadow_primarySchool_coupon_all","shadow_primarySchool_operate_management","shadow_primarySchool_sponsored_links","shadow_primarySchool_origin_links","shadow_primarySchool_code_management","shadow_primarySchool_channel_management","shadow_primarySchool_banner_management","shadow_primarySchool_send_groupMessage","shadow_primarySchool_find_verificationCode","shadow_primarySchool_configCenter_customerServiceMessage","shadow_primarySchool_distributionActivity_risk"]'
localstorage_list = [
    {'key': 'onionsToken',
     'value': onionsToken},
    {'key': 'shadowToken',
     'value': shadowToken},
    {'key': 'persist:root',
     'value': persist_root},
    {'key': 'antd-pro-authority',
     'value': antd_pro_authority},
]
'''WEB的配置'''
chromedrive_path = os.path.dirname(__file__) + '/tools/chromedriver'

log_path = os.path.dirname(__file__) + '/log'

logs_path = glob.glob(log_path + '/*')

airtest_result = log_path + '/__init__.py'

case_path = os.path.dirname(__file__) + '/test_case_web'

cases_path = glob.glob(case_path + '/air*.py')

rm_log = os.path.dirname(__file__) + '/log'

rm_logs = glob.glob(os.path.dirname(__file__) + r'/*log')

rm_reports_txt = os.path.dirname(__file__) + '/report.html'
# web case静态资源
admin_web_images = os.path.dirname(__file__) + '/static/admin_web'
# 小学web通用验证码
verification_code = '**'

'''ADNROID的配置'''
android_case_path = os.path.dirname(__file__) + '/test_case_android'

android_log_path = os.path.dirname(__file__) + '/log'

android_cases_path = glob.glob(android_case_path + '/air*.py')

android_address = ["Android://127.0.0.1:5037", ]

mobile_path = os.path.dirname(__file__) + '/static/onion_android/mobile.csv'

'''IOS的配置'''

ios_case_path = os.path.dirname(__file__) + '/test_case_ios'

ios_log_path = os.path.dirname(__file__) + '/log'

ios_cases_path = glob.glob(ios_case_path + '/air*.py')

ios_address = ["ios:///http://127.0.0.1:8100", ]
