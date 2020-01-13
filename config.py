import os, glob

'''WEB的配置'''
chromedrive_path = os.path.dirname(__file__) + '/tools/chromedriver'

log_path = os.path.dirname(__file__) + '/log'

logs_path = glob.glob(log_path + '/*')

airtest_result = log_path + '/__init__.py'

case_path = os.path.dirname(__file__) + '/test_case_web'

cases_path = glob.glob(case_path + '/air*.py')

out_files = 'log.html'

report_path = os.path.dirname(__file__) + '/report.html'

rm_log = os.path.dirname(__file__) + '/log'

rm_logs = glob.glob(os.path.dirname(__file__) + r'/*log')

rm_reports_txt = os.path.dirname(__file__) + '/report.html'

verification_code = '****'

onionsToken = r'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkZTRjZDgwMzMwY2ExODRlZGQwNGVlOSIsImlhdCI6MTU3NzcwMTg1MCwiZXhwIjoxNTc4OTExNDUwfQ.1bvCTvu_4qGR15f0Mr5kF_97I6f--WBAEbwOKy639q4'

shadowToken = r'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkZTRjZDgwMzMwY2ExODRlZGQwNGVlOSIsImlhdCI6MTU3NzcwMTg1MCwiZXhwIjoxNTc4OTExNDUwfQ.1bvCTvu_4qGR15f0Mr5kF_97I6f--WBAEbwOKy639q4'

persist_root = r'{"routing":"{\"location\":{\"pathname\":\"/\",\"search\":\"\",\"hash\":\"\",\"query\":{},\"key\":\"tvow8k\"}}","@@dva":"0","activities":"{\"goodsListById\":{},\"goodsIds\":[],\"risksListById\":{},\"risksIds\":[],\"activityMeta\":{},\"allGoodsListById\":{},\"allGoodsIds\":[]}","admission":"{\"admissionListById\":{},\"admissionIds\":[],\"activityPageById\":{},\"activityPageIds\":[],\"admissionDetailListById\":{},\"admissionDetailIds\":[],\"gradePublisherList\":{},\"courseListById\":{},\"courseIds\":[],\"commodityListById\":{},\"commodityIds\":[],\"classListById\":{},\"classIds\":[]}","classManage":"{\"typeList\":[{\"id\":\"春季班\",\"name\":\"春季班\"},{\"id\":\"体验班\",\"name\":\"体验班\"},{\"id\":\"暑期班\",\"name\":\"暑期班\"},{\"id\":\"赠送暑期班\",\"name\":\"赠送暑期班\"},{\"id\":\"秋季班\",\"name\":\"秋季班\"},{\"id\":\"寒假班\",\"name\":\"寒假班\"},{\"id\":\"期中班\",\"name\":\"期中班\"},{\"id\":\"期末班\",\"name\":\"期末班\"},{\"id\":\"免费班\",\"name\":\"免费班\"},{\"id\":\"直播课招生\",\"name\":\"直播课招生\"}],\"gradeList\":[{\"id\":\"2\",\"name\":\"一年级\"},{\"id\":\"4\",\"name\":\"二年级\"},{\"id\":\"6\",\"name\":\"三年级\"},{\"id\":\"8\",\"name\":\"四年级\"},{\"id\":\"10\",\"name\":\"五年级\"},{\"id\":\"11\",\"name\":\"六年级\"}],\"classList\":[],\"totalCount\":0,\"wxInfoList\":[{\"_id\":\"5da18b2df98da277d2ff2e39\",\"teacherWeChat\":\"c\",\"nickName\":\"c11\",\"qrCode\":\"https://wx-static.yangcong345.com/1573111338025日比谷-山本彩.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b2df98da277d2ff2e3a\",\"teacherWeChat\":\"d\",\"nickName\":\"d22222\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b2df98da277d2ff2e3c\",\"teacherWeChat\":\"f\",\"nickName\":\"f\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b2df98da277d2ff2e3e\",\"teacherWeChat\":\"h\",\"nickName\":\"h\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e3f\",\"teacherWeChat\":\"11\",\"nickName\":\"11\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e40\",\"teacherWeChat\":\"12\",\"nickName\":\"12\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e43\",\"teacherWeChat\":\"15\",\"nickName\":\"15\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e44\",\"teacherWeChat\":\"16\",\"nickName\":\"16\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e45\",\"teacherWeChat\":\"17\",\"nickName\":\"17\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e46\",\"teacherWeChat\":\"18\",\"nickName\":\"18\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e47\",\"teacherWeChat\":\"19\",\"nickName\":\"19\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e48\",\"teacherWeChat\":\"10\",\"nickName\":\"10\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e4a\",\"teacherWeChat\":\"1b\",\"nickName\":\"1b\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e4f\",\"teacherWeChat\":\"1g\",\"nickName\":\"1g\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18b72f98da277d2ff2e50\",\"teacherWeChat\":\"1h\",\"nickName\":\"1h\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e51\",\"teacherWeChat\":\"111\",\"nickName\":\"111\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e52\",\"teacherWeChat\":\"112\",\"nickName\":\"112\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e53\",\"teacherWeChat\":\"113\",\"nickName\":\"113\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e54\",\"teacherWeChat\":\"114\",\"nickName\":\"114\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e55\",\"teacherWeChat\":\"115\",\"nickName\":\"115\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e56\",\"teacherWeChat\":\"116\",\"nickName\":\"116\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e57\",\"teacherWeChat\":\"117\",\"nickName\":\"117\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e5a\",\"teacherWeChat\":\"110\",\"nickName\":\"110\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e5c\",\"teacherWeChat\":\"11b\",\"nickName\":\"11b\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e5e\",\"teacherWeChat\":\"11d\",\"nickName\":\"11d\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e5f\",\"teacherWeChat\":\"11e\",\"nickName\":\"11e\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e60\",\"teacherWeChat\":\"11f\",\"nickName\":\"11f\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da18bb5f98da277d2ff2e61\",\"teacherWeChat\":\"11g\",\"nickName\":\"11g\",\"qrCode\":\"https://fp.yangcong345.com/20190429104924-155953422497742.jpg\",\"state\":\"1\",\"createdAt\":\"2019-06-05T06:15:28.712Z\"},{\"_id\":\"5da3e11f7b6c27000fccc76a\",\"createdAt\":\"2019-10-14T02:44:47.202Z\",\"teacherWeChat\":\"测试\",\"nickName\":\"123456\",\"qrCode\":\"https://wx-static.yangcong345.com/15710210480872-2-扫码进小程序海报.png\",\"state\":\"1\"},{\"_id\":\"5da435200547fe000ff0a0d3\",\"createdAt\":\"2019-10-14T08:43:12.233Z\",\"teacherWeChat\":\"asdasd\",\"nickName\":\"啊实打实大师的\",\"qrCode\":\"https://wx-static.yangcong345.com/1571042550926957daf31e3f7207b.jpg\",\"state\":\"1\"},{\"_id\":\"5da6de44d1a31c0010e3408d\",\"createdAt\":\"2019-10-16T09:09:24.200Z\",\"teacherWeChat\":\"12312wq\",\"nickName\":\"88888\",\"qrCode\":\"https://wx-static.yangcong345.com/1572405071095banner-分销.png\",\"state\":\"1\"},{\"_id\":\"5da83efbdd43f500107c2af8\",\"createdAt\":\"2019-10-17T10:14:19.720Z\",\"teacherWeChat\":\"test111\",\"nickName\":\"测试\",\"qrCode\":\"https://wx-static.yangcong345.com/15713072202092-2-扫码进小程序海报.png\",\"state\":\"1\"},{\"_id\":\"5dad28c037eb900010a7c4be\",\"createdAt\":\"2019-10-21T03:40:48.330Z\",\"teacherWeChat\":\"asdasddsfsdf\",\"nickName\":\"asdazszxczxsdff\",\"qrCode\":\"https://wx-static.yangcong345.com/1571629202074blastoise.png\",\"state\":\"1\"},{\"_id\":\"5daea4d03810aa0010f3a1d7\",\"createdAt\":\"2019-10-22T06:42:24.043Z\",\"teacherWeChat\":\"lll123\",\"nickName\":\"31lll\",\"qrCode\":\"https://fp.yangcong345.com/touxing-15717264995161319.jpeg\",\"state\":\"1\"},{\"_id\":\"5daec9d27f2b32001090366d\",\"createdAt\":\"2019-10-22T09:20:18.748Z\",\"teacherWeChat\":\"测试\",\"nickName\":\"1312\",\"qrCode\":\"https://wx-static.yangcong345.com/15717359774112-2-扫码进小程序海报.png\",\"state\":\"1\"},{\"_id\":\"5daeccbd7f2b32001090367e\",\"createdAt\":\"2019-10-22T09:32:45.360Z\",\"teacherWeChat\":\"chenlaoshi\",\"nickName\":\"chenlaoshi\",\"qrCode\":\"https://wx-static.yangcong345.com/1571736724242picture_wechat_link@2x.png\",\"state\":\"1\"},{\"_id\":\"5daeccd07f2b32001090367f\",\"createdAt\":\"2019-10-22T09:33:04.023Z\",\"teacherWeChat\":\"chenlaoshi\",\"nickName\":\"chenlaoshi\",\"qrCode\":\"https://wx-static.yangcong345.com/1571736740701me_ic_diamond@2x.png\",\"state\":\"1\"},{\"_id\":\"5daecd727f2b320010903680\",\"createdAt\":\"2019-10-22T09:35:46.335Z\",\"teacherWeChat\":\"chenlaoshi\",\"nickName\":\"chenlaoshi\",\"qrCode\":\"https://wx-static.yangcong345.com/1571736904985积的近似数-人教版.png\",\"state\":\"1\"},{\"_id\":\"5daeceaa7610680010dccf08\",\"createdAt\":\"2019-10-22T09:40:58.776Z\",\"teacherWeChat\":\"aa\",\"nickName\":\"aaa\",\"qrCode\":\"https://wx-static.yangcong345.com/157173721605017_28_29__10_22_2019.jpg\",\"state\":\"1\"},{\"_id\":\"5db6a9d88e8db50010ff6c2c\",\"createdAt\":\"2019-10-28T08:42:00.347Z\",\"teacherWeChat\":\"test888\",\"nickName\":\"9999\",\"qrCode\":\"https://wx-static.yangcong345.com/1572405132364timg.jpeg\",\"state\":\"1\"},{\"_id\":\"5db6a9ff8e8db50010ff6c2d\",\"createdAt\":\"2019-10-28T08:42:39.191Z\",\"teacherWeChat\":\"test1231\",\"nickName\":\"3212313333\",\"qrCode\":\"https://wx-static.yangcong345.com/15722520977902-2-扫码进小程序海报.png\",\"state\":\"1\"},{\"_id\":\"5db6aa0e8e8db50010ff6c2e\",\"createdAt\":\"2019-10-28T08:42:54.834Z\",\"teacherWeChat\":\"撒发哇\",\"nickName\":\"撒地方大声是否地方撒\",\"qrCode\":\"https://wx-static.yangcong345.com/15722521318262-2-扫码进小程序海报.png\",\"state\":\"1\"},{\"_id\":\"5db80d0955ff93001021f165\",\"createdAt\":\"2019-10-29T09:57:29.994Z\",\"teacherWeChat\":\"aaaa\",\"nickName\":\"aaaaa\",\"qrCode\":\"https://wx-static.yangcong345.com/157234300466217_28_29__10_22_2019.jpg\",\"state\":\"1\"},{\"_id\":\"5dba45915f99ca001070b127\",\"createdAt\":\"2019-10-31T02:23:13.506Z\",\"teacherWeChat\":\"ycsx0743\",\"nickName\":\"洋葱数学-大鱼老师\",\"qrCode\":\"https://wx-static.yangcong345.com/1573029590765banner-双十一分销.png\",\"state\":\"1\"},{\"_id\":\"5dc120ed291c020010e5494e\",\"createdAt\":\"2019-11-05T07:12:45.802Z\",\"teacherWeChat\":\"ycsx0424\",\"nickName\":\"洋葱数学-田田老师\",\"qrCode\":\"https://wx-static.yangcong345.com/15729379188708a3820311d5dcebf7855c9fb4f158f8f.jpg\",\"state\":\"1\"},{\"_id\":\"5dc28779d2dff500107dd211\",\"createdAt\":\"2019-11-06T08:42:33.547Z\",\"teacherWeChat\":\"ycsx0730\",\"nickName\":\"洋葱数学-燕燕老师\",\"qrCode\":\"https://wx-static.yangcong345.com/15730297076008a3820311d5dcebf7855c9fb4f158f8f.jpg\",\"state\":\"1\"},{\"_id\":\"5dc531d677b3cf00100f4a47\",\"createdAt\":\"2019-11-08T09:13:58.258Z\",\"teacherWeChat\":\"测试132132132\",\"nickName\":\"123都发顺丰撒发撒发\",\"qrCode\":\"https://wx-static.yangcong345.com/15732042860371de3cff80489c69651ae4a7e969897c.jpg\",\"state\":\"1\"},{\"_id\":\"5dca7314d5e31e00102d250d\",\"createdAt\":\"2019-11-12T08:53:40.397Z\",\"teacherWeChat\":\"fdfdg\",\"nickName\":\"dfgdg\",\"qrCode\":\"https://wx-static.yangcong345.com/15735487717231323345392-664886173_q.jpg\",\"state\":\"1\"},{\"_id\":\"5dca7a31a99f6f00107de135\",\"createdAt\":\"2019-11-12T09:24:01.304Z\",\"teacherWeChat\":\"ghjkl\",\"nickName\":\"ghjkl\",\"qrCode\":\"https://wx-static.yangcong345.com/15735505926461323345392-664886173_q.jpg\",\"state\":\"1\"},{\"_id\":\"5dca7a3da99f6f00107de136\",\"createdAt\":\"2019-11-12T09:24:13.586Z\",\"teacherWeChat\":\"fghjkl\",\"nickName\":\"ghjkl;\",\"qrCode\":\"https://wx-static.yangcong345.com/15735506051571323345392-664886173_q.jpg\",\"state\":\"1\"},{\"_id\":\"5dca7a58a99f6f00107de137\",\"createdAt\":\"2019-11-12T09:24:40.197Z\",\"teacherWeChat\":\"fghjkljkl\",\"nickName\":\"ghjklhjk\",\"qrCode\":\"https://wx-static.yangcong345.com/15735506174241323345392-664886173_q.jpg\",\"state\":\"1\"},{\"_id\":\"5dd77e1a7ba7ec0010decfe7\",\"createdAt\":\"2019-11-22T06:20:10.047Z\",\"teacherWeChat\":\"测试123321\",\"nickName\":\"测试123321\",\"qrCode\":\"https://wx-static.yangcong345.com/15744035510291de3cff80489c69651ae4a7e969897c.jpg\",\"state\":\"1\"},{\"_id\":\"5e05752d79b901006fae8c2c\",\"createdAt\":\"2019-12-27T03:06:21.446Z\",\"teacherWeChat\":\"ycsx0596\",\"nickName\":\"洋葱班主任-冰冰\",\"qrCode\":\"https://wx-static.yangcong345.com/1577415911938lADPDgQ9rZKcC7jNAa7NAa4_430_430.jpg\",\"state\":\"1\"}],\"volumeList\":[{\"key\":\"1\",\"value\":\"一年级上册\"},{\"key\":\"2\",\"value\":\"一年级下册\"},{\"key\":\"3\",\"value\":\"二年级上册\"},{\"key\":\"4\",\"value\":\"二年级下册\"},{\"key\":\"5\",\"value\":\"三年级上册\"},{\"key\":\"6\",\"value\":\"三年级下册\"},{\"key\":\"7\",\"value\":\"四年级上册\"},{\"key\":\"8\",\"value\":\"四年级下册\"},{\"key\":\"9\",\"value\":\"五年级上册\"},{\"key\":\"10\",\"value\":\"五年级下册\"},{\"key\":\"11\",\"value\":\"六年级上册\"},{\"key\":\"12\",\"value\":\"六年级下册\"}],\"allPublisherId\":[{\"key\":\"1\",\"value\":\"人教版\"},{\"key\":\"2\",\"value\":\"北师大版\"},{\"key\":\"6\",\"value\":\"苏科版\"}],\"userIdsByClassId\":{},\"userListByUserId\":{},\"goalInfoByClassId\":{},\"recordListByUserId\":{},\"courseListByClassId\":{},\"selectUserId\":\"\",\"notConvertReasonsList\":[],\"intentionList\":[],\"userScoreList\":[],\"channelList\":[],\"changeCourseTotalCount\":0,\"smsTemplateById\":{},\"smsTemplateIdsByClassId\":{}}","configure":"{\"totalCount\":0,\"weChatInfoIds\":[],\"weChatInfoById\":{},\"wechatRuleListIds\":[],\"wechatRuleListById\":{}}","exercises":"{\"exerciseListById\":{},\"userFinishByUserId\":{},\"goalListByCourseId\":{},\"courseListByCourseId\":{},\"userIdsByCourseId\":{},\"exerciseStates\":[{\"key\":\"uncommitted\",\"value\":\"未提交\"},{\"key\":\"notCorrected\",\"value\":\"未批改\"},{\"key\":\"corrected\",\"value\":\"已批改\"}],\"exerciseScores\":[{\"key\":\"5\",\"value\":\"优秀\"}],\"selCourseId\":\"\",\"selUserId\":\"\",\"selExerciseId\":\"\",\"selTopicId\":\"\",\"exerciseCount\":0,\"focusGoal\":false}","global":"{\"collapsed\":true,\"notices\":[]}","login":"{}","materials":"{\"totalCount\":0,\"materialsIds\":[],\"materialInfoById\":{}}","resources":"{\"bannerListById\":{},\"bannerIds\":[],\"popupListById\":{},\"popupIds\":[]}","settings":"{\"navTheme\":\"dark\",\"primaryColor\":\"#1890FF\",\"layout\":\"sidemenu\",\"contentWidth\":\"Fluid\",\"fixedHeader\":false,\"autoHideHeader\":false,\"fixSiderbar\":false,\"colorWeak\":false,\"menu\":{\"locale\":true},\"title\":\"洋葱数学-小学\",\"pwa\":false,\"iconfontUrl\":\"\"}","user":"{\"id\":\"5de4cd80330ca184edd04ee9\",\"name\":\"王刚\",\"mail\":\"wanggang_test@guanghe.tv\",\"username\":\"wanggang_test\",\"roles\":[\"shadow_primarySchool_course_all\",\"shadow_primarySchool_class_searchAll\",\"shadow_primarySchool_class_searchPersonal\",\"shadow_primarySchool_activationCode_all\",\"shadow_primarySchool_customMenu_all\",\"shadow_primarySchool_autoResponseServiceNum_all\",\"shadow_primarySchool_customTemplate_all\",\"shadow_primarySchool_config_manager\",\"shadow_primarySchool_questionnaire_investigation\",\"shadow_primarySchool_referral_activities\",\"shadow_primarySchool_custom_template\",\"shadow_primarySchool_customerService_message\",\"shadow_primarySchool_search_allClasses\",\"shadow_primarySchool_search_ownClasses\",\"shadow_primarySchool_primarySchoolAllPage_all\",\"shadow_primarySchool_coupon_all\",\"shadow_primarySchool_operate_management\",\"shadow_primarySchool_sponsored_links\",\"shadow_primarySchool_origin_links\",\"shadow_primarySchool_code_management\",\"shadow_primarySchool_channel_management\",\"shadow_primarySchool_banner_management\",\"shadow_primarySchool_send_groupMessage\",\"shadow_primarySchool_find_verificationCode\",\"shadow_primarySchool_configCenter_customerServiceMessage\",\"shadow_primarySchool_good_all\",\"shadow_primarySchool_order_all\"]}","loading":"{\"global\":false,\"models\":{\"user\":false,\"login\":false,\"classManage\":false},\"effects\":{\"user/login\":false,\"login/logout\":false,\"classManage/getVolumeAndPublishListEffect\":false,\"classManage/getWxListAndInfoEffect\":false,\"classManage/fetchTypeAndGrade\":false}}","_persist":"{\"version\":-1,\"rehydrated\":true}"}'

antd_pro_authority = r'["shadow_primarySchool_course_all","shadow_primarySchool_class_searchAll","shadow_primarySchool_class_searchPersonal","shadow_primarySchool_activationCode_all","shadow_primarySchool_customMenu_all","shadow_primarySchool_autoResponseServiceNum_all","shadow_primarySchool_customTemplate_all","shadow_primarySchool_config_manager","shadow_primarySchool_questionnaire_investigation","shadow_primarySchool_referral_activities","shadow_primarySchool_custom_template","shadow_primarySchool_customerService_message","shadow_primarySchool_search_allClasses","shadow_primarySchool_search_ownClasses","shadow_primarySchool_primarySchoolAllPage_all","shadow_primarySchool_coupon_all","shadow_primarySchool_operate_management","shadow_primarySchool_sponsored_links","shadow_primarySchool_origin_links","shadow_primarySchool_code_management","shadow_primarySchool_channel_management","shadow_primarySchool_banner_management","shadow_primarySchool_send_groupMessage","shadow_primarySchool_find_verificationCode","shadow_primarySchool_configCenter_customerServiceMessage","shadow_primarySchool_good_all","shadow_primarySchool_order_all"]'

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

'''ADNROID的配置'''
android_case_path = os.path.dirname(__file__) + '/test_case_android'

android_log_path = os.path.dirname(__file__) + '/log'

android_cases_path = glob.glob(android_case_path + '/air*.py')

android_address = ["Android://127.0.0.1:5037", ]
