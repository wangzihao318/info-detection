#Mr wang
import hashlib,time,requests,os
import random,ssl,getopt
import threading,queue,datetime
import sys,re,sqlite3,lxml
from bs4 import BeautifulSoup as BS




lock = threading.Lock()

pwd = os.getcwd()

# Ignore warning
requests.packages.urllib3.disable_warnings()
# Ignore ssl warning info.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

header_task = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Cookie': 'thinkphp_show_page_trace=0|0; thinkphp_show_page_trace=0|0; think_var=zh-cn; PHPSESSID=gljsd5c3ei5n813roo4878q203',
               'X-Requested-With': 'XMLHttpRequest'
               }


cms_finger_list =['08cms', '1039_jxt', '1039家校通', '3gmeeting', '3gmeeting视讯系统', '51fax传真系统', '53kf', '5ucms', '686_weixin', '6kbbs', '74cms', '86cms', 'afterlogicwebmail系统', 'appcms', 'aspcms', 'b2bbuilder', 'beescms', 'bookingecms酒店系统', 'cactiez插件', 'chinacreator', 'cxcms', 'dk动科cms', 'doyo通用建站系统', 'dtcms', 'dvrdvs-webs', 'datalifeengine', 'dayucms', 'dedecms', 'destoon', 'digital campus2.0', 'digitalcampus2.0', 'discuz', 'discuz7.2', 'drupal', 'dswjcms', 'duomicms', 'dvbbs', 'dzzoffice', 'ecshop', 'ec_word企业管理系统', 'emlog', 'easysite内容管理', 'edusoho', 'empirecms', 'epaper报刊系统', 'epoint', 'espcms', 'fengcms', 'foosuncms', 'gentlecms', 'gever', 'glassfish', 'h5酒店管理系统', 'hdwiki', 'hjcms企业网站管理系统', 'himail', 'hishop商城系统', 'hituxcms', 'ilas图书系统', 'iloanp2p借贷系统', 'imo云办公室系统', 'insightsoft', 'iwebshop', 'iwmscms', 'jboos', 'jishigou', 'jeecms', 'jingyi', 'joomla', 'kangle虚拟主机', 'kesioncms', 'kessioncms', 'kingcms', 'lebishop网上商城', 'live800', 'live800插件', 'ljcms', 'mlecms', 'mailgard', 'majexpress', 'mallbuilder', 'maticsoftsns', 'minyoocms', 'mvmmall', 'mymps蚂蚁分类信息', 'n点虚拟主机', 'opensns', 'ourphp', 'php168', 'phpcms', 'phpwind', 'phpok', 'piw内容管理系统', 'phpmyadmin', 'phpwind网站程序', 'pigcms', 'powercreator在线教学系统', 'powereasy', 'sapnetweaver', 'shopex', 'shop7z', 'shopnc商城系统', 'shopnum', 'siteserver', 'soullon', 'southidc', 'supesite', 't-site建站系统', 'theol网络教学综合平台', 'trs身份认证系统', 'tipask问答系统', 'tomcat', 'trsids', 'trunkey', 'turbomail邮箱系统', 'v2视频会议系统', 'v5shop', 'venshop2010凡人网络购物系统', 'vos3000', 'veryide', 'wcm系统v6', 'wordpress', 'ws2004校园管理系统', 'wangzt', 'weblogic', 'webmail', 'weboffice', 'webnet cms', 'webnetcms', 'wilmaroa系统', 'winmail server', 'winmailserver', 'wizbank', 'xplus报社系统', 'xpshop', 'yidacms', 'yongyou', 'z-blog', 'zabbix', 'zoomla', 'abcms', 'able_g2s', 'acsno', 'acsoft', 'actcms', 'adtsec_gateway', 'akcms', 'anleye', 'anmai', 'anmai安脉教务管理系统', 'anymacromail', 'apabi_tasi', 'asiastar_sm', 'aten_kvm', 'atripower', 'avcon6', 'axis2', 'ayacms', 'b2cgroup', 'baiaozhi', 'beidou', 'bluecms', 'boblog', 'bocweb', 'bohoog', 'bytevalue_router', 'canon', 'chamilo-lms', 'ckfinder', 'cmseasy', 'cmstop', 'cnoa', 'codeigniter', 'comexe_ras', 'cscms', 'cutecms', 'd-link', 'dahua_dss', 'daiqile_p2p', 'dalianqianhao', 'damall', 'damicms', 'dfe_scada', 'dianyips', 'diguocms帝国', 'dircms', 'dkcms', 'dossm', 'douphp', 'dreamgallery', 'dubbo', 'eshangbao易商宝', 'easethink', 'easy7视频监控平台', 'ecweb_shop', 'edayshop', 'edjoy', 'eduplate', 'edusohocms', 'eims', 'eimscms', 'electric_monitor', 'empire_cms', 'enableq', 'enjie_soft', 'es-cloud', 'esafenet_dlp', 'esccms', 'ewebs', 'expocms', 'extmail', 'eyou', 'e创站', 'fang5173', 'fangwei', 'fastmeeting', 'fcms', 'fcms梦想建站', 'feifeicms', 'feiyuxing_router', 'finecms', 'fiyocms', 'foosun', 'foosun文章系统', 'fsmcms', 'gbcom_wlan', 'genixcms', 'gnuboard', 'gocdkey', 'gooine_sqjz', 'gowinsoft_jw', 'gxcms', 'hac_gateway', 'haitianoa', 'hanweb', 'haohan', 'heeroa', 'hf_firewall', 'hongzhi', 'horde_email', 'house5', 'hsort', 'huachuang_router', 'huanet', 'huashi_tv', 'humhub', 'idvr', 'ipowercms', 'iceflow_vpn_router', 'ideacms', 'ieadcms', 'iflytek_soft', 'igenus', 'ikuai', 'insight', 'jenkins', 'jienuohan', 'jieqicms', 'jindun_gateway', 'jingci_printer', 'jinpan', 'jinqiangui_p2p', 'jishitongxun', 'joomle', 'jumbotcms', 'juniper_vpn', 'kill_firewall', 'kingdee_eas', 'kingdee_oa', 'kinggate', 'kingosoft_xsweb', 'kj65n_monitor', 'klemanndesign', 'kuwebs', 'kxmail', 'landray', 'lebishop', 'lezhixing_datacenter', 'lianbangsoft', 'liangjing', 'libsys', 'linksys', 'looyu_live', 'ltpower', 'luepacific', 'luzhucms', 'lvmaque', 'maccms', 'magento', 'mailgard-webmail', 'mainone_b2b', 'maopoa', 'maxcms', 'mbbcms', 'metinfo', 'mikrotik_router', 'moxa_nport_router', 'mpsec', 'myweb', 'nanjing_shiyou', 'natshell', 'nbcms', 'net110', 'netcore', 'netgather', 'netoray_nsg', 'netpower', 'newvane_onlineexam', 'nitc', 'nitc定海神真', 'niubicms', 'ns-asg', 'otcms', 'pageadmin', 'panabit', 'phpb2b', 'phpcmsv9', 'phpdisk', 'phpmaps', 'phpmps', 'phpmywind', 'phpshe', 'phpshop', 'phpvibe', 'phpweb', 'phpwiki', 'phpyun', 'piaoyou', 'pkpmbs', 'plc_router', 'powercreator', 'qht_study', 'qianbocms', 'qibosoft', 'qiuxue', 'qizhitong_manager', 'qzdatasoft强智教务管理系统', 'rockoa', 'rockontrol', 'ruijie_router', 'ruvar_oa', 'ruvarhrm', 's8000', 'santang', 'sdcms', 'seagate_nas', 'seawind', 'seentech_uccenter', 'sgc8000', 'shadows-it', 'shenlan_jiandu', 'shlcms', 'shopnum1', 'shopxp', 'shuangyang_oa', 'siteengine', 'sitefactory', 'skypost', 'skytech', 'smart_oa', 'soffice', 'soullon_edu', 'srun_gateway', 'star-net', 'startbbs', 'strongsoft', 'subeicms', 'syncthru_web_service', 'synjones_school', 'syxxjs', 'sztaiji_zw', 'taocms', 'taodi', 'terramaster', 'thinkox', 'thinkphp', 'thinksns', 'tianbo_train', 'tianrui_lib', 'tipask', 'tongdaoa', 'topsec', 'totalsoft_lib', 'tp-link', 'trs_ids', 'trs_inforadar', 'trs_lunwen', 'trs_wcm', 'typecho', 'umail', 'uniflows', 'unis_gateway', 'uniwin_gov', 'urp', 'v2_conference', 'vbulletin', 'vicworl', 'visionsoft_velcro', 'wangqushop', 'wdcp', 'wdscms', 'weaver_oa', 'websitebaker', 'wecenter', 'weixinpl', 'weway_soft', 'wisedu_elcs', 'workyisystem', 'workyi_system', 'wygxcms', 'xdcms', 'xiaowuyou_cms', 'xikecms', 'xinhaisoft', 'xinyang', 'xinzuobiao', 'xplus', 'xr_gatewayplatform', 'xuezi_ceping', 'xycms', 'ynedut_campus', 'yongyou_a8', 'yongyou_crm', 'yongyou_ehr', 'yongyou_fe', 'yongyou_icc', 'yongyou_nc', 'yongyou_u8', 'yongyou_zhiyuan_a6', 'yuanwei_gateway', 'yxlink', 'zblog', 'zcncms', 'zdsoft_cnet', 'zentao', 'zeroboard', 'zf_cms', 'zfsoft', 'zhongdongli_school', 'zhonghaida_vnet', 'zhongqidonglicms', 'zhongruan_firewall', 'zhoupu', 'zhuangxiu', 'zhuhaigaoling_huanjingzaosheng', 'zmcms', 'zmcms建站', 'zte', 'zuitu', 'zzcms', '万众电子期刊cms', '万博网站管理系统2006', '万博网站管理系统', '万户oa', '万欣高校管理系统', '三才期刊系统', '中企动力cms', '乐彼多网店', '亿邮email', '企智通系列上网行为管理系统', '众拓', '全程oa', '凡诺企业网站管理系统', '分类信息网bank.asp后门', '创捷驾校系统', '华夏创新appex系统', '南方数据', '口福科技', '味多美导航', '商奇cms', '商家信息管理系统', '四通政府网站管理系统', '大汉jcms', '天柏在线考试系统', '天融信panabit', '宁志学校网站', '宁志学校网站系统', '安乐业房产系统', '定海神真', '小计天空进销存管理系统', '尘月企业网站管理系统', '尘缘雅境图文系统', '建站之星', '微擎科技', '悟空crm', '悟空crm系统', '擎天政务系统', '新为软件e-learning管理系统', '新秀', '方维团购', '方维团购购物分享系统', '时代企业邮', '明腾cms', '易创思', '易创思教育建站系统', '易想cms', '智睿网站系统', '最土团购系统', '未知oem安防监控系统', '未知政府采购系统', '未知查询系统', '杭州博采cms', '杰奇小说连载系统', '桃源相册管理系统', '汇成企业建站cms', '汇文图书馆书目检索系统', '汉码高校毕业生就业信息系统', '泛微e-office', '泛微oa', '浪潮cms', '海康威视', '爱淘客', '爱装网', '用友fe协作办公平台', '用友fe管理系统', '用友turbcrm系统', '用友u8', '用友', '皓翰通用数字化校园平台', '省级农机构置补贴信息管理系统', '科信邮件系统', '科迈ras', '程氏舞曲cms', '绿麻雀借贷系统', '网趣商城', '网钛文章管理系统', '老y文章管理系统', '联众mediinfo医院综合管理平台', '自动发卡平台', '良精南方', '艺帆cms', '菲斯特诺期刊系统', '蓝凌eis智慧协同平台', '蓝科cms', '薄冰时期网站管理系统', '讯时网站管理系统cms', '记事狗', '贷齐乐系统', '通达oa系统', '速贝cms', '金色校园', '金蝶oa', '金蝶协作办公系统', '金钱柜p2p', '集时通讯程序', '露珠文章管理系统', '青云客cms', '青峰网络智能网站管理系统', '青果学生系统', '青果学生综合系统', '青果教务系统', '青果软件教务系统', '非凡建站']
def requests_proxies():
    '''
    Proxies for every requests
    '''
    proxies = {
    'http':'',#127.0.0.1:1080 shadowsocks
    'https':''#127.0.0.1:8080 BurpSuite
    }
    return proxies

def requests_headers():
    user_agent = ['Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre',
    'Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60','Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4062; en; U; ssr)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']
    UA = random.choice(user_agent)
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent':UA,
    'Upgrade-Insecure-Requests':'1','Connection':'keep-alive','Cache-Control':'max-age=0',
    'Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8',
    "Referer": "http://www.baidu.com/link?url=www.so.com&url=www.soso.com&&url=www.sogou.com",
    'Cookie':"PHPSESSID=gljsd5c3ei5n813roo4878q203"}
    return headers




# Use-Agent
agent = {'UserAgent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))'}

# re
rtitle = re.compile(r'title="(.*)"')
rheader = re.compile(r'header="(.*)"')
rbody = re.compile(r'body="(.*)"')
rbracket = re.compile(r'\((.*)\)')


def check(_id):
    with sqlite3.connect(pwd + '/cms_finger.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute('SELECT name, keys FROM `fofa` WHERE id=\'{}\''.format(_id))
        for row in result:
            return row[0], row[1]


def count():
    with sqlite3.connect(pwd + '/cms_finger.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute('SELECT COUNT(id) FROM `fofa`')
        for row in result:
            return row[0]


class Cmsscanner(object):
    def __init__(self, target):
        self.target = target
        self.start = time.time()
        self.finger = []

    def get_info(self):
        """获取web的信息"""
        try:
            r = requests.get(url=self.target, headers=agent,
                             timeout=request_timeout, verify=False)
            content = r.text
            try:
                title = BS(content, 'lxml').title.text.strip()
                return str(r.headers), content, title.strip('\n')
            except:
                return str(r.headers), content, ''
        except Exception as e:
            pass

    def check_rule(self, key, header, body, title):
        """指纹识别"""
        try:
            if 'title="' in key:
                if re.findall(rtitle, key)[0].lower() in title.lower():
                    return True
            elif 'body="' in key:
                if re.findall(rbody, key)[0] in body: return True
            else:
                if re.findall(rheader, key)[0] in header: return True
        except Exception as e:
            pass

    def handle(self, _id, header, body, title):
        """取出数据库的key进行匹配"""
        name, key = check(_id)
        # 满足一个条件即可的情况
        if '||' in key and '&&' not in key and '(' not in key:
            for rule in key.split('||'):
                if self.check_rule(rule, header, body, title):
                    self.finger.append(name)
                    # print '%s[+] %s   %s%s' % (G, self.target, name, W)
                    break
        # 只有一个条件的情况
        elif '||' not in key and '&&' not in key and '(' not in key:
            if self.check_rule(key, header, body, title):
                self.finger.append(name)
                # print '%s[+] %s   %s%s' % (G, self.target, name, W)
        # 需要同时满足条件的情况
        elif '&&' in key and '||' not in key and '(' not in key:
            num = 0
            for rule in key.split('&&'):
                if self.check_rule(rule, header, body, title):
                    num += 1
            if num == len(key.split('&&')):
                self.finger.append(name)
                # print '%s[+] %s   %s%s' % (G, self.target, name, W)
        else:
            # 与条件下存在并条件: 1||2||(3&&4)
            if '&&' in re.findall(rbracket, key)[0]:
                for rule in key.split('||'):
                    if '&&' in rule:
                        num = 0
                        for _rule in rule.split('&&'):
                            if self.check_rule(_rule, header, body, title):
                                num += 1
                        if num == len(rule.split('&&')):
                            self.finger.append(name)
                            # print '%s[+] %s   %s%s' % (G, self.target, name, W)
                            break
                    else:
                        if self.check_rule(rule, header, body, title):
                            self.finger.append(name)
                            # print '%s[+] %s   %s%s' % (G, self.target, name, W)
                            break
            else:
                # 并条件下存在与条件： 1&&2&&(3||4)
                for rule in key.split('&&'):
                    num = 0
                    if '||' in rule:
                        for _rule in rule.split('||'):
                            if self.check_rule(_rule, title, body, header):
                                num += 1
                                break
                    else:
                        if self.check_rule(rule, title, body, header):
                            num += 1
                if num == len(key.split('&&')):
                    self.finger.append(name)
                    # print '%s[+] %s   %s%s' % (G, self.target, name, W)

    def run(self):
        try:
            header, body, title = self.get_info()
            for _id in range(1, int(count())):
                try:
                    self.handle(_id, header, body, title)
                except Exception as e:
                    pass
        except Exception as e:
            print(e)
        finally:
            return self.finger

def getMD5(c):
    if type(c)==str:
        c=c.encode('utf-8')
    m = hashlib.md5()
    m.update(c)
    psw = m.hexdigest()
    return psw


class Worker(threading.Thread):  # 处理工作请求
    def __init__(self, workQueue, resultQueue, **kwds):
        threading.Thread.__init__(self, **kwds)
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while 1:
            try:
                callable, args, kwds = self.workQueue.get(False)  # get task
                res = callable(*args, **kwds)
                self.resultQueue.put(res)  # put result
            except queue.Empty:
                break

class WorkManager:  # 线程池管理,创建
    def __init__(self, num_of_workers=10,time_waite = 10):
        self.workQueue = queue.Queue()  # 请求队列
        self.resultQueue = queue.Queue()  # 输出结果的队列
        self.workers = []
        self.time_waite = time_waite
        self._recruitThreads(num_of_workers)

    def _recruitThreads(self, num_of_workers):
        for i in range(num_of_workers):
            worker = Worker(self.workQueue, self.resultQueue)  # 创建工作线程
            self.workers.append(worker)  # 加入到线程队列

    def start(self):
        for w in self.workers:
            w.start()

    def wait_for_complete(self):
        while len(self.workers):
            worker = self.workers.pop()  # 从池中取出一个线程处理请求
            worker.join(self.time_waite)
            if worker.is_alive() and not self.workQueue.empty():
                self.workers.append(worker)  # 重新加入线程池中

    def add_job(self, callable, *args, **kwds):
        self.workQueue.put((callable, args, kwds))  # 向工作队列中加入请求

    def get_result(self, *args, **kwds):
        return self.resultQueue.get(*args, **kwds)

class WhatCms:
    def __init__(self,target,file_path):
        self.cms=[]
        self.diction={}
        self.is_finish=False
        self.g_index=0
        self.threads=[]
        self.lock=threading.Lock()
        self.thread_num = 100
        self.target=WhatCms.normalize_target(target)
        self.info={}
        self.file_path=file_path

    @staticmethod
    def request_url(url):
        try:
            if use_proxy:
                proxy = random.choice(proxy_list)
                web_proxy = {"http": proxy.replace("\n","")}
                print ("web_proxy",web_proxy)
            else:
                web_proxy = {"http":''}

            headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
            }

            r = requests.get(url=url, headers=requests_headers(),timeout=request_timeout,verify=False,proxies = web_proxy)
            r.encoding = 'utf-8'
            if r.status_code==200:
                return r.text,r.content
            else:
                return '',''
        except Exception as e:
            # print e
            return '',''

    @staticmethod
    def normalize_target(target):
        if target.endswith('/'):
            target = target[:-1]
        if target.startswith('http'):
            pass
        else:
            target = 'http://' + target
        return target

    def find_powered_by(self):
        '''
        根据powered by获取cms
        :return:
        '''
        html,content = WhatCms.request_url(self.target)
        match = re.search('Powered by (.*)', html, re.I)
        if match:
            clear_html_cms = re.sub('<.*?>', '', match.group(1))
            cms_name = clear_html_cms.split(' ')[0]
            self.info['cms_name'] =  cms_name
            self.info['path'] = '/'
            self.info['match_pattern'] = "powered by "+cms_name
            self.is_finish=True
            return True
        else:
            return False

    def find_cms_with_file(self):
        '''
        根据cms.txt检测cms
        :return:
        '''
        while True:
            if self.is_finish:
                break
            if self.g_index >= len(self.cms):
                self.lock.acquire()
                self.is_finish = True
                self.info['cms_name'] = "Not Found"
                self.info['path'] = "nothing"
                self.info['match_pattern'] = "nothing"
                self.lock.release()
                break
            self.lock.acquire()
            try:
                eachline = self.cms[self.g_index]
            except Exception as e:
                break
            self.g_index += 1
            self.lock.release()

            finger_id,cms_name,path,match_pattern,options,hit = eachline[0],eachline[1],eachline[2],eachline[3],eachline[4],eachline[5]

            url = self.target + path
            # print self.g_index,url
            response_html,response_content = WhatCms.request_url(url)

            if options == "md5":
                if match_pattern == getMD5(response_content):
                    self.lock.acquire()
                    self.is_finish = True
                    self.info['finger_id']= finger_id
                    self.info['cms_name']=cms_name
                    self.info['path'] = path
                    self.info['match_pattern']=match_pattern
                    self.info['options']=options
                    self.info['hit']=hit
                    self.lock.release()
                    break

            elif options == "keyword":
                if match_pattern.lower() in response_html.lower():
                    self.lock.acquire()
                    self.is_finish = True
                    self.info['finger_id']= finger_id
                    self.info['cms_name']=cms_name
                    self.info['path'] = path
                    self.info['match_pattern']=match_pattern
                    self.info['options']=options
                    self.info['hit']=hit
                    self.lock.release()
                    break
            elif options == "regx":
                r = re.search(match_pattern, response_html)
                if r:
                    self.lock.acquire()
                    self.is_finish = True
                    self.info['finger_id']= finger_id
                    self.info['cms_name']=cms_name
                    self.info['path'] = path
                    self.info['match_pattern']=match_pattern
                    self.info['options']=options
                    self.info['hit']=hit
                    self.lock.release()
                    break

    def start_threads(self):

        wm_domain_task = WorkManager(self.thread_num,5)
        for i in range(self.thread_num):
            wm_domain_task.add_job(self.find_cms_with_file)
        wm_domain_task.start()
        wm_domain_task.wait_for_complete()


    def run(self):
        # info=self.find_powered_by()
        info = False
        if not info:
            sqlconn1=sqlite3.connect(self.file_path)
            sqlcursor1=sqlconn1.cursor()
            sqlcursor1.execute('select * from cms order by hit')
            self.cms = sqlcursor1.fetchall()
            # print self.cms[1]
            sqlcursor1.close()
            sqlconn1.close()
            self.start_threads()


    def get_result(self):
        while True:
            if self.is_finish:
                # print "self.info:",self.info
                if self.info['cms_name'] != 'Not Found':
                    try:
                        lock.acquire()
                        sqlconn=sqlite3.connect(self.file_path)
                        sqlcursor=sqlconn.cursor()
                        sqlcursor.execute('update cms set hit =? where finger_id = ?',(self.info['hit']+1,self.info['finger_id']))
                        sqlcursor.close()
                        sqlconn.commit()
                        sqlconn.close()
                        lock.release()
                    except Exception as e:
                        return False
                return self.info
            else:
                return False

def finger_query(url):
    whatcms=WhatCms(url,'cms_finger.db')
    whatcms.run()
    finger_dic = whatcms.get_result()
    return finger_dic

# exit(0)

def weppalyzer(url):
    try:
        from Wappalyzer import Wappalyzer, WebPage
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url('https://www.hupu.com')
        return wappalyzer.analyze(webpage)
    except:
        print("pip install python-Wappalyzer")
        quit()



if __name__ == "__main__":
    try:
        use_proxy = False
        check_thunder = 100
        request_timeout = 5
        ip = ''
        target_url='https://www.hupu.com'
        ping = True
        start =datetime.datetime.now()
        if use_proxy:
            proxy_list = []
            if os.path.exists('proxys_ips.txt'):
                for porxy_tmp in open('proxys_ips.txt'):
                    proxy_list.append(porxy_tmp.strip())
            else:
                print ("读取代理列表出错，请确保代理文件名为proxys_ips.txt,每行一条代理，格式如: 124.225.223.101:80")

        if re.match(r'^https?:/{2}\w.+$', target_url):
            print ('\n')
            print ("Current Task: ",target_url)
            daytime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            cms = Cmsscanner(target_url)
            fofa_finger = cms.run()
            weppalyzer_finger=weppalyzer(target_url)
            print( "-"*50)
            fofa_banner = ''
            cms_name = ''
            cms_name_flag = 0
            for finger in weppalyzer_finger:
                if finger.lower() not in fofa_finger:
                    fofa_finger.append(finger)
            for fofa_finger_tmp in fofa_finger:
                fofa_banner= fofa_banner + ' '+fofa_finger_tmp
                if fofa_finger_tmp.lower() in cms_finger_list:
                    cms_name = fofa_finger_tmp
                    cms_name_flag = 1
            if fofa_banner.startswith(' '):
                fofa_banner = fofa_banner[1:]
            if fofa_banner:
                print ("fofa_banner:%s"%fofa_banner)
            if not cms_name_flag:
                cms_name_tmp = finger_query(target_url)
                if cms_name_tmp:
                    cms_name = cms_name_tmp['cms_name']
            print ("CMS__finger:%s"%cms_name)
            end =datetime.datetime.now()
            print("-"*50)
            print ("Time Used:",(end - start).seconds,'秒')
        else:
            print ("URL地址错误")

    except Exception as e:
        print (str(time.strftime('%Y-%m-%d %X', time.localtime(time.time())))+"  Info  "+str(e))
        pass
