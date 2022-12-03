# -*- coding: utf8 -*-

class ApiError(object):

    def __init__(self, name, code, msg):
        self.name = name
        self.errno = code
        self.errmsg = msg

    def __call__(self, msg):
        self.errmsg = msg
        return self

    def __str__(self):
        return "%s(%d): %s" % (self.name, self.errno, self.errmsg)

NormalError = ApiError("NormalError", -9999, "操作失败")
RedisFailed = ApiError("RedisFailed", -10000, "缓存操作失败")
InvalidArguments = ApiError("InvalidArguments", -10001, "参数错误")
MissArguments = ApiError("MissArguments", -10002, "缺少参数")
InvalidContent = ApiError("InvalidContent", -10003, "您输入的内容违规")
UserExists = ApiError("UserExists", -10004, "该用户已存在")
UserNotExist = ApiError("UserNotExist", -10005, "该用户不存在")
LoginFailed = ApiError("LoginFailed", -10006, "用户名或密码错误")
SessionExpired = ApiError("SessionExpired", -10007, "用户登录过期")
AuthFailed = ApiError("AuthFailed", -10008, "用户无权限")
AuthRequired = ApiError("AuthRequired", -10009, "需要授权")
GameNotExist = ApiError("GameNotExist", -10010, "该游戏不存在")
VideoNotExist = ApiError("VideoNotExist", -10011, "该视频不存在")
CommentNotExist = ApiError("CommentNotExist", -10012, "该评论不存在")
SendCodeFailed = ApiError("SendCodeFailed", -10013, "发送失败，请稍后再试")
VerifyCodeFailed = ApiError("VerifyCodeFailed", -10014, "短信验证码错误")
RegisterFailed = ApiError("RegisterFailed", -10015, "注册失败，请重试")
UpdatePwdFailed = ApiError("UpdatePwdFailed", -10016, "修改密码失败，请重试")
ResetPwdFailed = ApiError("ResetPwdFailed", -10017, "重置密码失败，请重试")
PasswordFailed = ApiError("PasswordFailed", -10018, "密码错误")
UploadFailed = ApiError("UploadFailed", -10019, "文件上传失败")
NicknameExists = ApiError("NicknameExists", -10020, "昵称已被占用")
NicknameInvalid = ApiError("NicknameInvalid", -10021, "昵称长度不超过4-20个字符，支持汉字、字母、数字的组合")
Md5EncryptInvalid = ApiError("Md5EncryptInvalid", -10022, "Md5加密错误")
UserTrafficInvalid = ApiError("UserTrafficInvalid", -10023, "分享的不是自己的视频, 分享无效")
GameDownloadFailed = ApiError("GameDownloadFailed", -10024, "游戏下载失败")
QuestionNotExists = ApiError('QuestionNotExists', -10025, "该问题不存在")
UserTrafficExists = ApiError("UserTrafficExists", -10026, "已经分享成功, 再次分享无效")
FollowFailed = ApiError("FollowFailed", -10027, "关注失败，请稍后再试")
SubForecastFailed = ApiError("SubForecastFailed", -10028, "订阅失败，请稍后再试")
LikeCommentFailed = ApiError("LikeCommentFailed", -10029, "点赞失败，请稍后再试")
FavorVideoFailed = ApiError("FavorVideoFailed", -10030, "收藏视频失败，请稍后再试")
LikeVideoFailed = ApiError("LikeVideoFailed", -10031, "点赞失败，请稍后再试")
TrafficSendFail = ApiError("TrafficSendFail ", -10032, "流量充值失败，请稍后再试")
InvalidRequest = ApiError("InValidRequest", -10033, "非法操作")
ReplyNotExist = ApiError("ReplyNotExist", -10034, "评论回复不存在")
TrafficExists = ApiError("TrafficExists", -10035, "账号已领取过, 不能重复领取")
MiguError = ApiError("MiguError", -10036, "咪咕错误")
LiveError = ApiError("LiveError", -10037, "直播错误")
TaskError = ApiError("TaskError", -10039, "任务错误")
GiftError = ApiError("GiftError", -10040, "礼物错误")
ActivityNotExist = ApiError("ActivityNotExist", -10042, "该活动不存在")
ActivityVideoNotExist = ApiError("ActivityVideoNotExist", -10043, "该活动参赛视频不存在")
ActivityVideoExist = ApiError("ActivityVideoExist", -10044, "该活动参赛视频已存在")
StoreError = ApiError("StoreError", -10045, "交易错误")
MarketingError = ApiError("MarketingError", -10046, "营销平台错误")
CategoryNotExist = ApiError("CategoryNotExist", -10047, "该分类不存在")
TopicNonExist = ApiError("TopicNonExist", -10048, "该话题不存在")
UpperGold = ApiError("UpperGold", -10049, "今日领取积分已经到上限")
QuestionVideoExists = ApiError('QuestionVideoExists', -10050, "该问题已经加入到了直播中")
FollowIngInvalid = ApiError("FollowFailed", -10051, "正在等待主播确认，请稍后再试")
AnswerExists = ApiError("AnswerExists", -10052, "您已回答过此问题")
TeamNameExists = ApiError("TeamNameExists", -10053, "团队名称已被占用")
TeamNameInvalid = ApiError("TeamNameInvalid", -10054, "名称长度不超过4-20个字符，支持汉字、字母、数字的组合")
TeamExists = ApiError("TeamExists", -10055, "团队已存在")
TeamNotExists = ApiError("TeamNotExists", -10056, "团队不存在")
FolderNotExists = ApiError("FolderNotExists", -10057, "文件夹不存在")
QrCodeNotExists = ApiError("QrCodeNotExists", -10058, "二维码已失效请重新获取")
QuestionnaireNotExists = ApiError("QuestionnaireNotExists", -10059, "问卷不存在")
VideoCourseNotExists = ApiError("VideoCourseNotExists", -10060, "课程不存在")
VideoVoteExists = ApiError("VideoVoteExists", -10061, "已经投过票")
VideoVoteNotExists = ApiError("VideoVoteNotExists", -10062, "投票不存在")
VideoCourseAuthFailed = ApiError("VideoCourseAuthFailed", -10063, "课程观看授权失败")
VideoCoursePasswordError = ApiError("VideoCourseAuthFailed", -10064, "课程密码错误")

CreateChargeFailed = ApiError("CreateChargeFailed", -20001, "创建支付订单失败")
CheckChargeFailed = ApiError("CheckChargeFailed", -20001, "查询支付订单信息失败")
CreateRefundsFailed = ApiError("CreateRefundsFailed", -20003, "创建退款订单失败")
CheckRefundsFailed = ApiError("CreateRefundsFailed", -20004, "查询退款订单信息失败")
CreateTransferFailed = ApiError("CreateTransferFailed", -20005, "创建提现订单失败")
CheckTransferFailed = ApiError("CheckTransferFailed", -20006, "查询提现订单信息失败")
NoDrawAccount = ApiError("NoDrawAccount", -20007, "该平台未绑定提现账号")
NoEnoughCash = ApiError("NoEnoughCash", -20008, "钱包余额不足")
OrderPaid = ApiError("OrderPaid", -20009, "订单已支付")
OrderNotPaid = ApiError("OrderNotPaid", -20010, "订单未支付")
OrderExpired = ApiError("OrderExpired", -20011, "订单已过期")
TransferOrderNotExists = ApiError("TransferOrderNotExists", -20020, "提现订单不存在")
TransferOrderError = ApiError("TransferOrderError", -20021, "提现订单参数错误")
PaymentOrderNotExists = ApiError("PaymentOrderNotExist", -20022, "支付订单不存在")
ProductNotExists = ApiError("ProductNotExists", -20040, "产品不存在")
OrderExists = ApiError("OrderExists", -20040, "产品订单已存在")
EnrollFailed = ApiError("EnrollFailed", -20041, "课程报名失败")
EnrollDup = ApiError("EnrollDup", -20042, "课程已经报名")
NoEnoughScore = ApiError("NoEnoughScore", -20043, "课程剩余次数不足")
UnsupportedCourseAuth = ApiError("UnsupportedCourseAuth", -20044, "课程收费方式不支持")

PingppError = ApiError("PingppError", -20100, "订单查询失败")
PingppOrderNotExists = ApiError("PingppOrderNotExist", -20101, "订单不存在或已失效")
PingppApiError = ApiError("PingppApiError", -20102, "支付服务器异常")
PingppChannelError = ApiError("PingppChannelError", -20103, "第三方支付渠道错误")
WxpubOpenIdError = ApiError("WxpubOpenIdError", -20104, "获取微信公众号用户OpenID失败")