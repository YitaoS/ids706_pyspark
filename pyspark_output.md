The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is describe data

The truncated output is: 

|    | summary   |    rank | city                |       avg |       jan |       feb |       mar |       apr |       may |       jun |       jul |       aug |       sep |       oct |       nov |       dec |
|---:|:----------|--------:|:--------------------|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|
|  0 | count     | 5377    | 5377                | 5377      | 4835      | 4833      | 4875      | 4840      | 4825      | 4784      | 4754      | 4739      | 4637      | 4699      | 5364      | 5373      |
|  1 | mean      | 2689    |                     |   32.1717 |   44.6443 |   42.767  |   40.3586 |   38.706  |   33.1822 |   32.5677 |   27.9424 |   28.4851 |   27.9672 |   31.4741 |   35.8331 |   39.566  |
|  2 | stddev    | 1552.35 |                     |   27.0752 |   52.1882 |   41.2054 |   37.3938 |   34.2302 |   22.6295 |   21.2726 |   19.1713 |   21.9076 |   19.2934 |   27.4785 |   39.9561 |   43.7187 |
|  3 | min       |    1    | A Coruna, Spain     |    1      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |
|  4 | max       | 5377    | Zwolle, Netherlands |  223      |  418      |  344      |  534      |  412      |  306      |  338      |  286      |  545      |  463      |  357      |  405      |  406      |

The operation is query data

The query is 
        SELECT city, ROUND((jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + dec) / 12, 2) AS yearly_avg 
        FROM city_temperatures
        ORDER BY yearly_avg DESC
        

The truncated output is: 

|      | city                                          |   yearly_avg |
|-----:|:----------------------------------------------|-------------:|
|    0 | Begusarai, India                              |       223.25 |
|    1 | Patna, India                                  |       211.58 |
|    2 | Saharsa, India                                |       207.42 |
|    3 | New Delhi, India                              |       204.5  |
|    4 | Noida, India                                  |       201.42 |
|    5 | Kashgar, China                                |       196.67 |
|    6 | Ghaziabad, India                              |       190    |
|    7 | Faridabad, India                              |       185.5  |
|    8 | Aksu, China                                   |       184.75 |
|    9 | Purnea, India                                 |       181.67 |
|   10 | Meerut, India                                 |       180    |
|   11 | Bhagalpur, India                              |       179.17 |
|   12 | Muzaffarpur, India                            |       178.83 |
|   13 | Sonipat, India                                |       178.5  |
|   14 | Birganj, Nepal                                |       171.08 |
|   15 | Rajmahal, India                               |       164.58 |
|   16 | Muzaffarnagar, India                          |       162.5  |
|   17 | Balurghat, India                              |       160.83 |
|   18 | Dhaka, Bangladesh                             |       160.75 |
|   19 | Bhiwadi, India                                |       157    |
|   20 | Ingraj Bazar, India                           |       154.67 |
|   21 | Rohtak, India                                 |       153.08 |
|   22 | Raiganj, India                                |       152.5  |
|   23 | Agartala, India                               |       150.17 |
|   24 | Bulandshahr, India                            |       140.67 |
|   25 | Zahedan, Iran                                 |       140.67 |
|   26 | Peshawar, Pakistan                            |       138.5  |
|   27 | Lucknow, India                                |       138    |
|   28 | Mahadipur, India                              |       136.92 |
|   29 | Saharanpur, India                             |       136.33 |
|   30 | Bhiwani, India                                |       136    |
|   31 | Hisar, India                                  |       135.92 |
|   32 | Turpan, China                                 |       135.83 |
|   33 | Kairana, India                                |       135.58 |
|   34 | Rajgir, India                                 |       135.58 |
|   35 | Hapur, India                                  |       135.5  |
|   36 | Vapi, India                                   |       129.75 |
|   37 | Lahore, Pakistan                              |       125.92 |
|   38 | Gorakhpur, India                              |       124.67 |
|   39 | Jodhpur, India                                |       124.58 |
|   40 | Bali, India                                   |       124.5  |
|   41 | Gaya, India                                   |       124.33 |
|   42 | Guwahati, India                               |       124.33 |
|   43 | Panipat, India                                |       124.25 |
|   44 | Kamarhati, India                              |       123.17 |
|   45 | Yanan Beilu, China                            |       121.83 |
|   46 | Dengtalu, China                               |       121.58 |
|   47 | Rishra, India                                 |       121.5  |
|   48 | Titagarh, India                               |       121.08 |
|   49 | Panihati, India                               |       120.92 |
|   50 | Shrirampur, India                             |       120.83 |
|   51 | Chandigarh, India                             |       120.58 |
|   52 | Khardah, India                                |       120.58 |
|   53 | Mauli, India                                  |       120.17 |
|   54 | Zabol, Iran                                   |       119.92 |
|   55 | Shuangqiao, China                             |       119.83 |
|   56 | Dispur, India                                 |       119.25 |
|   57 | Champdani, India                              |       119.17 |
|   58 | Xianyang, China                               |       118.92 |
|   59 | Bhadreswar, India                             |       118.58 |
|   60 | Chandannagar, India                           |       118.58 |
|   61 | Habra, India                                  |       118.58 |
|   62 | Karnal, India                                 |       118.58 |
|   63 | Linfen, China                                 |       118.5  |
|   64 | Silvassa, India                               |       118.33 |
|   65 | Bhatpara, India                               |       118.25 |
|   66 | Hugli, India                                  |       118.25 |
|   67 | Naihati, India                                |       118.25 |
|   68 | Wujiaqu, China                                |       118.08 |
|   69 | Halisahar, India                              |       117.83 |
|   70 | Madhyamgram, India                            |       117.75 |
|   71 | Yuncheng, China                               |       117.58 |
|   72 | Kalyani, India                                |       117.5  |
|   73 | Kanchrapara, India                            |       117.5  |
|   74 | Shantipur, India                              |       117.08 |
|   75 | Navadwip, India                               |       117    |
|   76 | Krishnanagar, India                           |       116.92 |
|   77 | Bikaner, India                                |       116.5  |
|   78 | Deo, India                                    |       116.42 |
|   79 | Kota, India                                   |       116.42 |
|   80 | Bansbaria, India                              |       116.17 |
|   81 | Asansol, India                                |       115.92 |
|   82 | Rampur, India                                 |       115.58 |
|   83 | Vrindavan, India                              |       115.42 |
|   84 | Thane, India                                  |       115.33 |
|   85 | Mumbai, India                                 |       114.83 |
|   86 | Fatehpur, India                               |       114.67 |
|   87 | Kolkata, India                                |       114.5  |
|   88 | Uluberiya, India                              |       114.5  |
|   89 | Alwar, India                                  |       114.42 |
|   90 | Valsad, India                                 |       114.33 |
|   91 | Bankura, India                                |       114.08 |
|   92 | Kanpur, India                                 |       113.58 |
|   93 | Kalyan, India                                 |       113.5  |
|   94 | Amritsar, India                               |       113.17 |
|   95 | Jamuria, India                                |       113.08 |
|   96 | Kulti, India                                  |       113.08 |
|   97 | Sirsa, India                                  |       113.08 |
|   98 | Bangaon, India                                |       112.83 |
|   99 | Daman, India                                  |       112.83 |
|  100 | Howrah, India                                 |       112.42 |
|  101 | Durgapur, India                               |       112.17 |
|  102 | Amudalavalasa, India                          |       111.83 |
|  103 | Anakapalle, India                             |       111.83 |
|  104 | Sitalpur, India                               |       111.75 |
|  105 | Pali, India                                   |       111.58 |
|  106 | Sambhal, India                                |       111.58 |
|  107 | Weinan, China                                 |       111.5  |
|  108 | Moradabad, India                              |       111.08 |
|  109 | Huanglongsi, China                            |       111    |
|  110 | Basirhat, India                               |       110.92 |
|  111 | Dhanbad, India                                |       110.83 |
|  112 | Shihezi, China                                |       110.75 |
|  113 | Xibeijie, China                               |       110.75 |
|  114 | Ponduru, India                                |       110.58 |
|  115 | Narasannapeta, India                          |       110.5  |
|  116 | Al Jahra, Kuwait                              |       110.25 |
|  117 | Dzuunharaa, Mongolia                          |       110.25 |
|  118 | Heze, China                                   |       110.08 |
|  119 | Bhimunipatnam, India                          |       110    |
|  120 | Chicacole, India                              |       110    |
|  121 | Chipurupalle, India                           |       109.92 |
|  122 | Gauripur, India                               |       109.92 |
|  123 | Donghua, China                                |       109.92 |
|  124 | Tula, Russia                                  |       109.83 |
|  125 | Hathras, India                                |       109.42 |
|  126 | Dam Dam, India                                |       109.25 |
|  127 | Aligarh, India                                |       109.17 |
|  128 | Ludhiana, India                               |       109.08 |
|  129 | Liaocheng, China                              |       109.08 |
|  130 | Wuwei, China                                  |       109.08 |
|  131 | Vishakhapatnam, India                         |       108.92 |
|  132 | Panauti, Nepal                                |       108.75 |
|  133 | Zijinglu, China                               |       108.75 |
|  134 | Tonk, India                                   |       108.67 |
|  135 | Puyang, China                                 |       108.67 |
|  136 | Chikhli, India                                |       108.58 |
|  137 | Bobbili, India                                |       108.5  |
|  138 | Hebi, China                                   |       108.42 |
|  139 | Xingtai, China                                |       108.33 |
|  140 | Bhiwandi, India                               |       108.25 |
|  141 | Sizhan, China                                 |       108.08 |
|  142 | Handan, China                                 |       108    |
|  143 | Jaipur, India                                 |       108    |
|  144 | Vizianagaram, India                           |       108    |
|  145 | Xian, China                                   |       107.67 |
|  146 | Khujand, Tajikistan                           |       107.67 |
|  147 | Jalandhar, India                              |       107.58 |
|  148 | Dholka, India                                 |       106.92 |
|  149 | Jaisalmer, India                              |       106.75 |
|  150 | Shancheng, China                              |       106.75 |
|  151 | Chernogorsk, Russia                           |       106.75 |
|  152 | Dushanbe, Tajikistan                          |       106.75 |
|  153 | Yucheng, China                                |       106.25 |
|  154 | Pune, India                                   |       105.92 |
|  155 | Bhayandar, India                              |       105.75 |
|  156 | Kathmandu, Nepal                              |       105.5  |
|  157 | Qingnian, China                               |       105.5  |
|  158 | Zhoukou, China                                |       105.42 |
|  159 | Dezhou, China                                 |       105.33 |
|  160 | Navsari, India                                |       105.33 |
|  161 | Pingdingshan, China                           |       105.08 |
|  162 | Luohe, China                                  |       105    |
|  163 | Jiangguanchi, China                           |       104.92 |
|  164 | Zhengzhou, China                              |       104.67 |
|  165 | Shizuishan, China                             |       104.58 |
|  166 | Tanbei, China                                 |       104.58 |
|  167 | Yuci, China                                   |       104.58 |
|  168 | Luoyang, China                                |       104.5  |
|  169 | Baoding, China                                |       103.92 |
|  170 | Louangphabang, Laos                           |       103.67 |
|  171 | Taiyuan, China                                |       103.58 |
|  172 | Barasat, India                                |       102.75 |
|  173 | Leling, China                                 |       102.58 |
|  174 | Wuhai, China                                  |       102.58 |
|  175 | Yakou, China                                  |       102.58 |
|  176 | Mathura, India                                |       102.5  |
|  177 | Binzhou, China                                |       102.25 |
|  178 | Shijiazhuang, China                           |       102.25 |
|  179 | Zaozhuang, China                              |       102.25 |
|  180 | Gwalior, India                                |       102.17 |
|  181 | Hengshui, China                               |       102.08 |
|  182 | Nangandao, China                              |       102.08 |
|  183 | Dongta, China                                 |       102    |
|  184 | Xiangyang, China                              |       101.92 |
|  185 | Fyzabad, India                                |       101.83 |
|  186 | Ulaanbaatar, Mongolia                         |       101.58 |
|  187 | Feicheng, China                               |       101.5  |
|  188 | Sanmenxia, China                              |       101.5  |
|  189 | Jiaozuo, China                                |       101    |
|  190 | Jiayuguan, China                              |       101    |
|  191 | Zibo, China                                   |       100.75 |
|  192 | Ankleshwar, India                             |       100.75 |
|  193 | Shangqiu, China                               |       100.5  |
|  194 | Cangzhou, China                               |       100.33 |
|  195 | Lanzhou, China                                |       100.25 |
|  196 | Qufu, China                                   |       100.25 |
|  197 | Allahabad, India                              |       100.17 |
|  198 | Ghandinagar, India                            |       100.08 |
|  199 | Yangquan, China                               |       100.08 |
|  200 | Cuttack, India                                |        99.75 |
|  201 | Zouping, China                                |        99.58 |
|  202 | Diu, India                                    |        99.5  |
|  203 | Jining, China                                 |        99.42 |
|  204 | Shouguang, China                              |        99.42 |
|  205 | Bharatpur, India                              |        99.33 |
|  206 | Tongchuan, China                              |        99.17 |
|  207 | Chengtangcun, China                           |        99.08 |
|  208 | Pingyi, China                                 |        99    |
|  209 | Tongshan, China                               |        98.67 |
|  210 | Yinchuan, China                               |        98.58 |
|  211 | Chkalov, Tajikistan                           |        98.58 |
|  212 | Ahmedabad, India                              |        98.42 |
|  213 | Barehra, India                                |        98.42 |
|  214 | Jiangjiafan, China                            |        98.33 |
|  215 | Surat, India                                  |        98.08 |
|  216 | Ujjain, India                                 |        97.75 |
|  217 | Yishui, China                                 |        97.75 |
|  218 | Tianjin, China                                |        97.42 |
|  219 | Linyi, China                                  |        97.33 |
|  220 | Kumul, China                                  |        97.25 |
|  221 | Baojishi, China                               |        97.08 |
|  222 | Shuozhou, China                               |        97.08 |
|  223 | Taian, China                                  |        97.08 |
|  224 | Jhansi, India                                 |        96.83 |
|  225 | Mahesana, India                               |        96.83 |
|  226 | Bozhou, China                                 |        96.75 |
|  227 | Urumqi, China                                 |        96.75 |
|  228 | Bhilwara, India                               |        96.75 |
|  229 | Patiala, India                                |        96.67 |
|  230 | Xintai, China                                 |        96.5  |
|  231 | Xinzhou, China                                |        96.42 |
|  232 | Jinan, China                                  |        96.33 |
|  233 | Nagpur, India                                 |        96.25 |
|  234 | Fenyang, China                                |        96.25 |
|  235 | Orchha, India                                 |        96.17 |
|  236 | Huayin, China                                 |        96.17 |
|  237 | Haldia, India                                 |        96.08 |
|  238 | Huaibei, China                                |        96    |
|  239 | Jinzhou, China                                |        95.67 |
|  240 | Kothapet, India                               |        95.17 |
|  241 | Ajmer, India                                  |        94.92 |
|  242 | Bam, Iran                                     |        94.67 |
|  243 | Kuiju, China                                  |        94.42 |
|  244 | Bloemfontein, South Africa                    |        94.33 |
|  245 | Ambala, India                                 |        94.17 |
|  246 | Khed, India                                   |        94.17 |
|  247 | Dali, China                                   |        94.17 |
|  248 | Anqiu, China                                  |        93.83 |
|  249 | Huludao, China                                |        93.83 |
|  250 | Wuyuan, China                                 |        93.83 |
|  251 | Brahmapur, India                              |        93.75 |
|  252 | Betma, India                                  |        93.67 |
|  253 | Indore, India                                 |        93.5  |
|  254 | Igdir, Turkey                                 |        93.42 |
|  255 | Xinan, China                                  |        93.42 |
|  256 | Laiwu, China                                  |        92.92 |
|  257 | Belampalli, India                             |        92.83 |
|  258 | Jincheng, China                               |        92.75 |
|  259 | Lianshan, China                               |        92.67 |
|  260 | Bhavnagar, India                              |        92.5  |
|  261 | Shashi, China                                 |        92.5  |
|  262 | Qingzhou, China                               |        92.25 |
|  263 | Hangu, China                                  |        91.92 |
|  264 | Kirtipur, Nepal                               |        91.92 |
|  265 | Gaomi, China                                  |        91.58 |
|  266 | Budaun, India                                 |        91.42 |
|  267 | Bareilly, India                               |        91.08 |
|  268 | Chanda, India                                 |        91.08 |
|  269 | Deyang, China                                 |        91    |
|  270 | Shahjanpur, India                             |        90.92 |
|  271 | Adilabad, India                               |        90.75 |
|  272 | Nanyang, China                                |        90.67 |
|  273 | Weifang, China                                |        90.67 |
|  274 | Shengli, China                                |        90.5  |
|  275 | Jabalpur, India                               |        90.42 |
|  276 | Jatani, India                                 |        90.33 |
|  277 | Puri, India                                   |        90.17 |
|  278 | Sikar, India                                  |        90.17 |
|  279 | Binxian, China                                |        90.08 |
|  280 | Kharagpur, India                              |        89.92 |
|  281 | Pilibhit, India                               |        89.92 |
|  282 | Etawah, India                                 |        89.58 |
|  283 | Ramgundam, India                              |        89.5  |
|  284 | Kuwait City, Kuwait                           |        89.5  |
|  285 | Baotou, China                                 |        89.33 |
|  286 | Dorud, Iran                                   |        89.25 |
|  287 | Yibin, China                                  |        89.17 |
|  288 | Zigong, China                                 |        89.17 |
|  289 | Mancheral, India                              |        89.08 |
|  290 | Beijing, China                                |        89.08 |
|  291 | Luzhou, China                                 |        89.08 |
|  292 | Konarka, India                                |        89    |
|  293 | Jieshou, China                                |        89    |
|  294 | Chinchvad, India                              |        88.83 |
|  295 | Aurangabad, India                             |        88.75 |
|  296 | Ratlam, India                                 |        88.67 |
|  297 | Abu Dhabi, United Arab Emirates               |        88.5  |
|  298 | Firozabad, India                              |        88.25 |
|  299 | Haripur, India                                |        88.25 |
|  300 | Bhubaneshwar, India                           |        88.17 |
|  301 | Xiaoganzhan, China                            |        88.08 |
|  302 | Vientiane, Laos                               |        88.08 |
|  303 | Ailan Mubage, China                           |        87.92 |
|  304 | Huainan, China                                |        87.83 |
|  305 | Fatehpur Sikri, India                         |        87.83 |
|  306 | Umaria, India                                 |        87.75 |
|  307 | Baharampur, India                             |        87.58 |
|  308 | Suqian, China                                 |        87.5  |
|  309 | Ahmadnagar, India                             |        87.5  |
|  310 | Yiyang, China                                 |        87.42 |
|  311 | Fuxin, China                                  |        87.17 |
|  312 | Khajuraho, India                              |        87.08 |
|  313 | Mandamari, India                              |        87.08 |
|  314 | Bengbu, China                                 |        87.08 |
|  315 | Tieling, China                                |        87    |
|  316 | Bhopal, India                                 |        86.75 |
|  317 | Sihor, India                                  |        86.67 |
|  318 | Godhra, India                                 |        86    |
|  319 | Jamshedpur, India                             |        86    |
|  320 | Changzhi, China                               |        85.92 |
|  321 | Al Ahmadi, Kuwait                             |        85.92 |
|  322 | Bahraich, India                               |        85.83 |
|  323 | Khambhat, India                               |        85.75 |
|  324 | Yulinshi, China                               |        85.58 |
|  325 | Bojnurd, Iran                                 |        85.42 |
|  326 | Mandsaur, India                               |        85.25 |
|  327 | Abohar, India                                 |        85.17 |
|  328 | Fushun, China                                 |        85.17 |
|  329 | Ahvaz, Iran                                   |        84.92 |
|  330 | Xiping, China                                 |        84.83 |
|  331 | Yazd, Iran                                    |        84.75 |
|  332 | Burhanpur, India                              |        84.42 |
|  333 | Barddhaman, India                             |        84.33 |
|  334 | Laixi, China                                  |        84.17 |
|  335 | Mizhou, China                                 |        84.17 |
|  336 | Langfang, China                               |        84.08 |
|  337 | Neijiang, China                               |        83.92 |
|  338 | Mae Sai, Thailand                             |        83.92 |
|  339 | Ouagadougou, Burkina Faso                     |        83.83 |
|  340 | Harbin, China                                 |        83.75 |
|  341 | Liaoyang, China                               |        83.75 |
|  342 | Jasdan, India                                 |        83.75 |
|  343 | Baiyin, China                                 |        83.67 |
|  344 | Weichanglu, China                             |        83.67 |
|  345 | Pingdu, China                                 |        83.58 |
|  346 | Agra, India                                   |        83.58 |
|  347 | Shenmu, China                                 |        83.5  |
|  348 | Dogubayazit, Turkey                           |        83.42 |
|  349 | Thai Nguyen, Vietnam                          |        83.42 |
|  350 | Armur, India                                  |        83.42 |
|  351 | Ramhormoz, Iran                               |        83.17 |
|  352 | Chaoyang, China                               |        83.08 |
|  353 | Anshan, China                                 |        82.92 |
|  354 | Hohhot, China                                 |        82.67 |
|  355 | Kovvur, India                                 |        82.67 |
|  356 | Chittaurgarh, India                           |        82.5  |
|  357 | Karachi, Pakistan                             |        82.5  |
|  358 | Eslamshahr, Iran                              |        82.42 |
|  359 | Pingliang, China                              |        82.42 |
|  360 | Rajahmundry, India                            |        82.25 |
|  361 | Xinyang, China                                |        82.25 |
|  362 | Amarkantak, India                             |        82.17 |
|  363 | Leshan, China                                 |        82.17 |
|  364 | Nandod, India                                 |        82.08 |
|  365 | Huanggang, China                              |        82.08 |
|  366 | Tadepallegudem, India                         |        81.92 |
|  367 | Boralday, Kazakhstan                          |        81.92 |
|  368 | Changde, China                                |        81.75 |
|  369 | Tongchuanshi, China                           |        81.75 |
|  370 | Xinpu, China                                  |        81.75 |
|  371 | Jalpaiguri, India                             |        81.67 |
|  372 | Nidadavole, India                             |        81.67 |
|  373 | Suihua, China                                 |        81.58 |
|  374 | Yingkou, China                                |        81.58 |
|  375 | Huaian, China                                 |        81.42 |
|  376 | Guangshui, China                              |        81.17 |
|  377 | Huaiyin, China                                |        81    |
|  378 | Zhenjiang, China                              |        80.92 |
|  379 | Xiangtan, China                               |        80.58 |
|  380 | Alipur Duar, India                            |        80.5  |
|  381 | Mandapeta, India                              |        80.5  |
|  382 | Solan, India                                  |        80.33 |
|  383 | Sanhe, China                                  |        80.33 |
|  384 | Osmaniye, Turkey                              |        80.33 |
|  385 | JalAl Abad, Kyrgyzstan                        |        80.17 |
|  386 | Dwarka, India                                 |        80.08 |
|  387 | Jagtial, India                                |        80    |
|  388 | Ezhou, China                                  |        80    |
|  389 | Guangan, China                                |        79.92 |
|  390 | Huangshi, China                               |        79.92 |
|  391 | Alleppey, India                               |        79.83 |
|  392 | Bilaspur, India                               |        79.83 |
|  393 | Rizhao, China                                 |        79.75 |
|  394 | Chiang Mai, Thailand                          |        79.75 |
|  395 | Tanuku, India                                 |        79.67 |
|  396 | Benxi, China                                  |        79.67 |
|  397 | Dhulia, India                                 |        79.42 |
|  398 | Pushkar, India                                |        79.42 |
|  399 | Tuni, India                                   |        79.33 |
|  400 | Amravati, India                               |        79.25 |
|  401 | Kakinada, India                               |        79.25 |
|  402 | Jalgaon, India                                |        79.08 |
|  403 | Angamali, India                               |        79    |
|  404 | Pithapuram, India                             |        79    |
|  405 | Hefei, China                                  |        78.75 |
|  406 | Wuhu, China                                   |        78.58 |
|  407 | Qinhuangdao, China                            |        78.5  |
|  408 | Shenyang, China                               |        78.5  |
|  409 | Maihar, India                                 |        78.5  |
|  410 | Samalkot, India                               |        78.5  |
|  411 | Shiliguri, India                              |        78.5  |
|  412 | Malard, Iran                                  |        78.25 |
|  413 | Chuzhou, China                                |        78.17 |
|  414 | Loudi, China                                  |        77.92 |
|  415 | Gaziantep, Turkey                             |        77.75 |
|  416 | Shaoyang, China                               |        77.67 |
|  417 | Gaoping, China                                |        77.5  |
|  418 | Jiaozhou, China                               |        77.5  |
|  419 | Xiaoxita, China                               |        77.5  |
|  420 | Meishan, China                                |        77.42 |
|  421 | Yanjiang, China                               |        77.42 |
|  422 | Amalapuram, India                             |        77.42 |
|  423 | Malaut, India                                 |        77.42 |
|  424 | Mianyang, China                               |        77.33 |
|  425 | Dezful, Iran                                  |        77.33 |
|  426 | Madan, Iran                                   |        77.33 |
|  427 | Hancheng, China                               |        77.25 |
|  428 | Draksharama, India                            |        77.25 |
|  429 | Kochi, India                                  |        77.25 |
|  430 | Malegaon, India                               |        77.25 |
|  431 | Siping, China                                 |        77.17 |
|  432 | Zhuzhou, China                                |        76.83 |
|  433 | Taft, Iran                                    |        76.75 |
|  434 | Wusong, China                                 |        76.67 |
|  435 | Zhuozhou, China                               |        76.58 |
|  436 | Jamnagar, India                               |        76.58 |
|  437 | Tezpur, India                                 |        76.5  |
|  438 | Changchun, China                              |        76.42 |
|  439 | Vadodara, India                               |        76.33 |
|  440 | Seven Pagodas, India                          |        76.25 |
|  441 | Shushtar, Iran                                |        76.25 |
|  442 | Rongjiawan, China                             |        76.25 |
|  443 | Bhilai, India                                 |        76    |
|  444 | Islamabad, Pakistan                           |        76    |
|  445 | Changsha, China                               |        75.92 |
|  446 | Narasapur, India                              |        75.83 |
|  447 | Porbandar, India                              |        75.83 |
|  448 | Yan'an, China                                 |        75.83 |
|  449 | Al Ayn, United Arab Emirates                  |        75.83 |
|  450 | Yangzhou, China                               |        75.67 |
|  451 | Pljevlja, Montenegro                          |        75.5  |
|  452 | Chengdu, China                                |        75.5  |
|  453 | Hengyang, China                               |        75.5  |
|  454 | Yingzhong, China                              |        75.5  |
|  455 | Nanchong, China                               |        75.42 |
|  456 | Akola, India                                  |        75.33 |
|  457 | Ahram, Iran                                   |        75.33 |
|  458 | Qinbaling, China                              |        75.25 |
|  459 | Bandar E Mahshahr, Iran                       |        75.25 |
|  460 | Meghraj, India                                |        75.17 |
|  461 | Metpalli, India                               |        75.17 |
|  462 | Fuyu, China                                   |        75    |
|  463 | Koratla, India                                |        75    |
|  464 | Abuja, Nigeria                                |        74.92 |
|  465 | Beining, China                                |        74.83 |
|  466 | Palakollu, India                              |        74.83 |
|  467 | Kuytun, China                                 |        74.75 |
|  468 | Luofeng, China                                |        74.5  |
|  469 | Changping, China                              |        74.33 |
|  470 | Bhusaval, India                               |        74.25 |
|  471 | Conjeeveram, India                            |        74.25 |
|  472 | Kigali, Rwanda                                |        74.17 |
|  473 | Qingdao, China                                |        74.08 |
|  474 | Sambalpur, India                              |        73.92 |
|  475 | Laiyang, China                                |        73.92 |
|  476 | Luan, China                                   |        73.92 |
|  477 | Madaba, Jordan                                |        73.83 |
|  478 | Anda, China                                   |        73.83 |
|  479 | Bhainsa, India                                |        73.75 |
|  480 | Bodupal, India                                |        73.75 |
|  481 | Jilin, China                                  |        73.67 |
|  482 | Karimnagar, India                             |        73.5  |
|  483 | Qarchak, Iran                                 |        73.33 |
|  484 | Anqing, China                                 |        73.25 |
|  485 | Beyram, Iran                                  |        73.25 |
|  486 | Jaunpur, India                                |        73.17 |
|  487 | Khem Karan, India                             |        73.17 |
|  488 | Zarand, Iran                                  |        72.75 |
|  489 | Gulbarga, India                               |        72.67 |
|  490 | Rajkot, India                                 |        72.67 |
|  491 | Chongqing, China                              |        72.5  |
|  492 | Jine, China                                   |        72.5  |
|  493 | Maanshan, China                               |        72.5  |
|  494 | Mahbubnagar, India                            |        72.42 |
|  495 | Changzhou, China                              |        72.42 |
|  496 | Zhuangyuan, China                             |        72.42 |
|  497 | Arvayheer, Mongolia                           |        72.33 |
|  498 | Palghat, India                                |        72.17 |
|  499 | Tangshan, China                               |        72.08 |
|  500 | Hanoi, Vietnam                                |        72.08 |
|  501 | Curchorem, India                              |        71.67 |
|  502 | Panaji, India                                 |        71.5  |
|  503 | Chizhou, China                                |        71.5  |
|  504 | Ban Houayxay, Laos                            |        71.33 |
|  505 | Trichur, India                                |        71.25 |
|  506 | Chennai, India                                |        71.17 |
|  507 | Hanzhong, China                               |        71.17 |
|  508 | Alberton, South Africa                        |        71.08 |
|  509 | Bhimavaram, India                             |        70.83 |
|  510 | Loutolim, India                               |        70.83 |
|  511 | Suining, China                                |        70.75 |
|  512 | Ciudad Apodaca, Mexico                        |        70.5  |
|  513 | Mundra, India                                 |        70.33 |
|  514 | Vidisha, India                                |        70.17 |
|  515 | Qaraghandy, Kazakhstan                        |        70.17 |
|  516 | Tonala, Mexico                                |        70.17 |
|  517 | Tongliao, China                               |        69.92 |
|  518 | Nainital, India                               |        69.92 |
|  519 | Udaipur, India                                |        69.92 |
|  520 | Panchgani, India                              |        69.83 |
|  521 | Phayao, Thailand                              |        69.67 |
|  522 | Varanasi, India                               |        69.58 |
|  523 | Ozgon, Kyrgyzstan                             |        69.25 |
|  524 | Xaignabouli, Laos                             |        69.25 |
|  525 | Coyhaique, Chile                              |        69.17 |
|  526 | Dehra Dun, India                              |        69    |
|  527 | Yavatmal, India                               |        68.83 |
|  528 | Sinuiju, North Korea                          |        68.67 |
|  529 | Medinipur, India                              |        68.58 |
|  530 | Chiang Rai, Thailand                          |        68.5  |
|  531 | Yongzhou, China                               |        68.5  |
|  532 | Naliya, India                                 |        68.42 |
|  533 | Ban Mae Cho, Thailand                         |        68.33 |
|  534 | Bodhan, India                                 |        68.25 |
|  535 | Andimeshk, Iran                               |        68.25 |
|  536 | Hovd, Mongolia                                |        68.25 |
|  537 | Shangzhou, China                              |        68.25 |
|  538 | Raichur, India                                |        68.08 |
|  539 | Dalian, China                                 |        68.08 |
|  540 | Quilon, India                                 |        68    |
|  541 | Xining, China                                 |        68    |
|  542 | Nanchang, China                               |        67.83 |
|  543 | Ciudad Benito Juarez, Mexico                  |        67.75 |
|  544 | Pingxiang, China                              |        67.75 |
|  545 | Chengde, China                                |        67.67 |
|  546 | Dazhou, China                                 |        67.42 |
|  547 | Nanded, India                                 |        67.42 |
|  548 | Pathanamthitta, India                         |        67.17 |
|  549 | Raurkela, India                               |        67.17 |
|  550 | Bac Giang, Vietnam                            |        67.08 |
|  551 | Changan, China                                |        66.92 |
|  552 | Linghai, China                                |        66.92 |
|  553 | Jakarta, Indonesia                            |        66.83 |
|  554 | Lamphun, Thailand                             |        66.83 |
|  555 | Narasaraopet, India                           |        66.75 |
|  556 | Tuyen Quang, Vietnam                          |        66.67 |
|  557 | Yantai, China                                 |        66.58 |
|  558 | Pakxan, Laos                                  |        66.58 |
|  559 | Cholula De Rivadabia, Mexico                  |        66.42 |
|  560 | Huzhou, China                                 |        66.33 |
|  561 | Ash Shihaniyah, Qatar                         |        66.25 |
|  562 | Behbahan, Iran                                |        66.25 |
|  563 | Hyderabad, India                              |        66.08 |
|  564 | Medan, Indonesia                              |        66    |
|  565 | Kicevo, Macedonia                             |        65.92 |
|  566 | Mirzapur, India                               |        65.83 |
|  567 | Yushan, China                                 |        65.83 |
|  568 | Gangtok, India                                |        65.75 |
|  569 | Vinukonda, India                              |        65.75 |
|  570 | Palembang, Indonesia                          |        65.75 |
|  571 | Strumica, Macedonia                           |        65.75 |
|  572 | Chengxiang, China                             |        65.67 |
|  573 | Puqi, China                                   |        65.67 |
|  574 | Bayan Hot, China                              |        65.33 |
|  575 | Jiujiang, China                               |        65.17 |
|  576 | Jaggayyapeta, India                           |        65.08 |
|  577 | Madinat Zayid, United Arab Emirates           |        65.08 |
|  578 | Baidyabati, India                             |        64.92 |
|  579 | Chilakalurupet, India                         |        64.92 |
|  580 | Daqing, China                                 |        64.83 |
|  581 | Xuanzhou, China                               |        64.83 |
|  582 | Addanki, India                                |        64.83 |
|  583 | Tiruppur, India                               |        64.83 |
|  584 | Cuddalore, India                              |        64.75 |
|  585 | Junnar, India                                 |        64.67 |
|  586 | Sattenapalle, India                           |        64.58 |
|  587 | Bijelo Polje, Montenegro                      |        64.5  |
|  588 | Erode, India                                  |        64.42 |
|  589 | Ongole, India                                 |        64.33 |
|  590 | Puducherry, India                             |        64.33 |
|  591 | Mangur, India                                 |        64.25 |
|  592 | Kandukur, India                               |        64.17 |
|  593 | Kavali, India                                 |        64.17 |
|  594 | Khammam, India                                |        64.17 |
|  595 | Suzhou, China                                 |        64.17 |
|  596 | Niala Kondapalle, India                       |        64.08 |
|  597 | Dubai, United Arab Emirates                   |        64    |
|  598 | Chimakurti, India                             |        63.83 |
|  599 | Chirala, India                                |        63.83 |
|  600 | Machilipatnam, India                          |        63.75 |
|  601 | Pedda Nandipadu, India                        |        63.75 |
|  602 | Chakradharpur, India                          |        63.67 |
|  603 | Mangalore, India                              |        63.67 |
|  604 | Secunderabad, India                           |        63.67 |
|  605 | Mangalagiri, India                            |        63.5  |
|  606 | Vikarabad, India                              |        63.5  |
|  607 | Malayer, Iran                                 |        63.5  |
|  608 | Macherla, India                               |        63.42 |
|  609 | Qazvin, Iran                                  |        63.42 |
|  610 | Rafsanjan, Iran                               |        63.42 |
|  611 | Mudanjiang, China                             |        63.42 |
|  612 | Kottagudem, India                             |        63.25 |
|  613 | Negapatam, India                              |        63.25 |
|  614 | Tiruvannamalai, India                         |        63.25 |
|  615 | Alamedin, Kyrgyzstan                          |        63.25 |
|  616 | Tuzla, Bosnia And Herzegovina                 |        63.25 |
|  617 | Nizamabad, India                              |        63.17 |
|  618 | Baishan, China                                |        63.17 |
|  619 | Nanjing, China                                |        63.17 |
|  620 | Jinhua, China                                 |        63.08 |
|  621 | Bac Ninh, Vietnam                             |        63    |
|  622 | Phitsanulok, Thailand                         |        62.92 |
|  623 | Nong Khai, Thailand                           |        62.83 |
|  624 | Yancheng, China                               |        62.83 |
|  625 | Liaoyuan, China                               |        62.75 |
|  626 | Dindigul, India                               |        62.67 |
|  627 | Repalle, India                                |        62.67 |
|  628 | Cadereyta Jimenez, Mexico                     |        62.67 |
|  629 | Kampala, Uganda                               |        62.67 |
|  630 | San Bernardo, Chile                           |        62.67 |
|  631 | Malatya, Turkey                               |        62.5  |
|  632 | Ponnuru, India                                |        62.42 |
|  633 | Ban Om Noi, Thailand                          |        62.42 |
|  634 | Bapatla, India                                |        62.33 |
|  635 | Nasik, India                                  |        62.33 |
|  636 | Chittoor, India                               |        62.25 |
|  637 | Atitalaquia, Mexico                           |        62.25 |
|  638 | Jangaon, India                                |        62.17 |
|  639 | Nagari, India                                 |        62.17 |
|  640 | Toluca, Mexico                                |        62.17 |
|  641 | Karamay, China                                |        62.08 |
|  642 | Longba, China                                 |        62.08 |
|  643 | Bezwada, India                                |        62.08 |
|  644 | Ellore, India                                 |        62    |
|  645 | Tlaquepaque, Mexico                           |        62    |
|  646 | Pedana, India                                 |        61.67 |
|  647 | Sirsilla, India                               |        61.58 |
|  648 | Samut Sakhon, Thailand                        |        61.5  |
|  649 | Sanzhou, China                                |        61.42 |
|  650 | Xinyu, China                                  |        61.42 |
|  651 | Ciudad Santa Catarina, Mexico                 |        61.33 |
|  652 | Nantong, China                                |        61.33 |
|  653 | Tanjore, India                                |        61.25 |
|  654 | Pudong, China                                 |        61.25 |
|  655 | Shanghai, China                               |        61.25 |
|  656 | Iskenderun, Turkey                            |        61.17 |
|  657 | Tenali, India                                 |        61.17 |
|  658 | Tetovo, Macedonia                             |        61.17 |
|  659 | Mus, Turkey                                   |        61.08 |
|  660 | Jalor, India                                  |        61.08 |
|  661 | Birjand, Iran                                 |        61.08 |
|  662 | Turgutlu, Turkey                              |        61    |
|  663 | Kahramanmaras, Turkey                         |        60.92 |
|  664 | Salihli, Turkey                               |        60.92 |
|  665 | Guntur, India                                 |        60.92 |
|  666 | Zhangjiajie, China                            |        60.75 |
|  667 | Loei, Thailand                                |        60.67 |
|  668 | Chifeng, China                                |        60.58 |
|  669 | Wuxi, China                                   |        60.5  |
|  670 | Yellandu, India                               |        60.42 |
|  671 | Bandar Lampung, Indonesia                     |        60.42 |
|  672 | Konya, Turkey                                 |        60.42 |
|  673 | Shaoxing, China                               |        60.42 |
|  674 | Shiyan, China                                 |        60.42 |
|  675 | Karur, India                                  |        60.25 |
|  676 | Trichinopoly, India                           |        60.25 |
|  677 | Sarajevo, Bosnia And Herzegovina              |        60.25 |
|  678 | Metepec, Mexico                               |        60.08 |
|  679 | Rancagua, Chile                               |        60.08 |
|  680 | Jiaxing, China                                |        60.08 |
|  681 | San Pedro Garza Garcia, Mexico                |        59.92 |
|  682 | Thoen, Thailand                               |        59.92 |
|  683 | Devarkonda, India                             |        59.83 |
|  684 | Hangzhou, China                               |        59.83 |
|  685 | Weihai, China                                 |        59.83 |
|  686 | Puttur, India                                 |        59.67 |
|  687 | Aydin, Turkey                                 |        59.67 |
|  688 | Inegol, Turkey                                |        59.67 |
|  689 | Guilin, China                                 |        59.58 |
|  690 | Karaj, Iran                                   |        59.5  |
|  691 | Jablanica, Bosnia And Herzegovina             |        59.42 |
|  692 | Bandar e Bushehr, Iran                        |        59.42 |
|  693 | Benin City, Nigeria                           |        59.42 |
|  694 | Huaihua, China                                |        59.33 |
|  695 | Pinghu, China                                 |        59.33 |
|  696 | Gudivada, India                               |        59.33 |
|  697 | Zhangjiakou, China                            |        59.25 |
|  698 | Tashkent, Uzbekistan                          |        59.25 |
|  699 | Qiqihar, China                                |        59.17 |
|  700 | Bhuj, India                                   |        59.17 |
|  701 | Ranchi, India                                 |        59.08 |
|  702 | Hubli, India                                  |        59    |
|  703 | Baneh, Iran                                   |        58.83 |
|  704 | Bidar, India                                  |        58.75 |
|  705 | Tadepalle, India                              |        58.75 |
|  706 | Garcia, Mexico                                |        58.75 |
|  707 | Chenzhou, China                               |        58.67 |
|  708 | Guigang, China                                |        58.58 |
|  709 | Parbhani, India                               |        58.58 |
|  710 | Coimbatore, India                             |        58.5  |
|  711 | Tirupati, India                               |        58.5  |
|  712 | Phanat Nikhom, Thailand                       |        58.42 |
|  713 | Suriapet, India                               |        58.42 |
|  714 | Venkatagiri, India                            |        58.42 |
|  715 | Roodepoort, South Africa                      |        58.33 |
|  716 | Lampang, Thailand                             |        58.33 |
|  717 | Gadwal, India                                 |        58.25 |
|  718 | Raipur, India                                 |        58.25 |
|  719 | Nalgonda, India                               |        58.17 |
|  720 | Shahriar, Iran                                |        58.08 |
|  721 | Tehran, Iran                                  |        58.08 |
|  722 | Baicheng, China                               |        58.08 |
|  723 | Dadukou, China                                |        58.08 |
|  724 | Liuzhou, China                                |        58.08 |
|  725 | Mersin, Turkey                                |        58    |
|  726 | Standerton, South Africa                      |        57.92 |
|  727 | Kamareddipet, India                           |        57.92 |
|  728 | Warangal, India                               |        57.92 |
|  729 | San Nicolas De Los Garza, Mexico              |        57.75 |
|  730 | Nellore, India                                |        57.67 |
|  731 | Shillong, India                               |        57.67 |
|  732 | Shuanghejiedao, China                         |        57.58 |
|  733 | Yichun, China                                 |        57.58 |
|  734 | Shaoshanzhan, China                           |        57.5  |
|  735 | Adoni, India                                  |        57.42 |
|  736 | Kavadarci, Macedonia                          |        57.42 |
|  737 | Latur, India                                  |        57.25 |
|  738 | Artashat, Armenia                             |        57.17 |
|  739 | Osh, Kyrgyzstan                               |        57.17 |
|  740 | Vellore, India                                |        57    |
|  741 | Nan, Thailand                                 |        57    |
|  742 | Lukavac, Bosnia And Herzegovina               |        56.92 |
|  743 | Dandong, China                                |        56.92 |
|  744 | Mashhad, Iran                                 |        56.92 |
|  745 | Tutin, Serbia                                 |        56.92 |
|  746 | Dharmavaram, India                            |        56.75 |
|  747 | Lo Miranda, Chile                             |        56.58 |
|  748 | Quzhou, China                                 |        56.58 |
|  749 | Guangyuan, China                              |        56.5  |
|  750 | Shahr E Qods, Iran                            |        56.5  |
|  751 | Wuzhou, China                                 |        56.42 |
|  752 | Sirnak, Turkey                                |        56.33 |
|  753 | Celaya, Mexico                                |        56.25 |
|  754 | Hakkari, Turkey                               |        56.17 |
|  755 | Anantapur, India                              |        56.17 |
|  756 | Kabudarahang, Iran                            |        56.17 |
|  757 | Shymkent, Kazakhstan                          |        56.17 |
|  758 | Kosjeric, Serbia                              |        55.92 |
|  759 | Bursa, Turkey                                 |        55.83 |
|  760 | Huilong, China                                |        55.83 |
|  761 | Jiamusi, China                                |        55.83 |
|  762 | Emmiganur, India                              |        55.67 |
|  763 | Shuangyashan, China                           |        55.67 |
|  764 | Calicut, India                                |        55.58 |
|  765 | Salem, India                                  |        55.5  |
|  766 | Pyeongtaek, South Korea                       |        55.33 |
|  767 | Ankang, China                                 |        55.25 |
|  768 | Yuyao, China                                  |        55    |
|  769 | Bishkek, Kyrgyzstan                           |        54.92 |
|  770 | Hamadan, Iran                                 |        54.83 |
|  771 | Almaty, Kazakhstan                            |        54.83 |
|  772 | Jieyang, China                                |        54.75 |
|  773 | Pakxe, Laos                                   |        54.75 |
|  774 | Jian, China                                   |        54.67 |
|  775 | Yulin, China                                  |        54.67 |
|  776 | Yatou, China                                  |        54.58 |
|  777 | Tangjin, South Korea                          |        54.58 |
|  778 | San Buenaventura, Mexico                      |        54.42 |
|  779 | Bangalore, India                              |        54.33 |
|  780 | Osmanabad, India                              |        54.33 |
|  781 | Xushan, China                                 |        54.33 |
|  782 | Doha, Qatar                                   |        54.17 |
|  783 | Davangere, India                              |        54.17 |
|  784 | Gostivar, Macedonia                           |        54.17 |
|  785 | Wanparti, India                               |        54.08 |
|  786 | Linxi, China                                  |        54    |
|  787 | Uzice, Serbia                                 |        53.92 |
|  788 | Beersheba, Israel                             |        53.92 |
|  789 | Phra Phutthabat, Thailand                     |        53.75 |
|  790 | Semarang, Indonesia                           |        53.75 |
|  791 | Ich'on, South Korea                           |        53.5  |
|  792 | Wenlan, China                                 |        53.5  |
|  793 | Breza, Bosnia And Herzegovina                 |        53.42 |
|  794 | Osorno, Chile                                 |        53.42 |
|  795 | Santiago, Chile                               |        53.42 |
|  796 | Arak, Iran                                    |        53.42 |
|  797 | Veles, Macedonia                              |        53.33 |
|  798 | Fuzhou, China                                 |        53.25 |
|  799 | Yingtan, China                                |        53.25 |
|  800 | Ch'onan, South Korea                          |        53.25 |
|  801 | Dok Kham Tai, Thailand                        |        53.17 |
|  802 | Leskovac, Serbia                              |        53.08 |
|  803 | Lianzhou, China                               |        53    |
|  804 | Addis Ababa, Ethiopia                         |        53    |
|  805 | Markapur, India                               |        52.92 |
|  806 | Ulanhot, China                                |        52.83 |
|  807 | Cuddapah, India                               |        52.83 |
|  808 | Springs, South Africa                         |        52.67 |
|  809 | Vereeniging, South Africa                     |        52.67 |
|  810 | Zenica, Bosnia And Herzegovina                |        52.58 |
|  811 | Puning, China                                 |        52.42 |
|  812 | Rajapalaiyam, India                           |        52.25 |
|  813 | Talas, Kyrgyzstan                             |        52.17 |
|  814 | Curico, Chile                                 |        52.17 |
|  815 | Sardasht, Iran                                |        52.08 |
|  816 | Jambi, Indonesia                              |        52    |
|  817 | Silao, Mexico                                 |        52    |
|  818 | Jorhat, India                                 |        51.92 |
|  819 | Madurai, India                                |        51.75 |
|  820 | Esfahan, Iran                                 |        51.67 |
|  821 | Shangrao, China                               |        51.67 |
|  822 | Itanagar, India                               |        51.58 |
|  823 | Iksan, South Korea                            |        51.5  |
|  824 | Chillan, Chile                                |        51.5  |
|  825 | Chongzuo, China                               |        51.5  |
|  826 | Kuaidamao, China                              |        51.5  |
|  827 | Udipi, India                                  |        51.33 |
|  828 | Pakdasht, Iran                                |        51.33 |
|  829 | Anseong, South Korea                          |        51.25 |
|  830 | Mae Hong Son, Thailand                        |        51.25 |
|  831 | Batman, Turkey                                |        51.25 |
|  832 | Ratchaburi, Thailand                          |        51.17 |
|  833 | Johannesburg, South Africa                    |        51.08 |
|  834 | Zepce, Bosnia And Herzegovina                 |        50.83 |
|  835 | Sihui, China                                  |        50.83 |
|  836 | Zhaotong, China                               |        50.83 |
|  837 | Palmaner, India                               |        50.83 |
|  838 | Pamidi, India                                 |        50.83 |
|  839 | Vanderbijlpark, South Africa                  |        50.83 |
|  840 | Brawley, United States                        |        50.83 |
|  841 | Varamin, Iran                                 |        50.75 |
|  842 | Hwasu Dong, South Korea                       |        50.75 |
|  843 | Hechi, China                                  |        50.67 |
|  844 | Kaihua, China                                 |        50.67 |
|  845 | Saalfelden am Steinernen Meer, Austria        |        50.58 |
|  846 | Yuxi, China                                   |        50.58 |
|  847 | Tengyue, China                                |        50.5  |
|  848 | Dibrugarh, India                              |        50.5  |
|  849 | Novi Pazar, Serbia                            |        50.5  |
|  850 | Saugor, India                                 |        50.42 |
|  851 | Jingdezhen, China                             |        50.42 |
|  852 | Ningbo, China                                 |        50.42 |
|  853 | Tuticorin, India                              |        50.33 |
|  854 | Linares, Chile                                |        50.33 |
|  855 | Wenzhou, China                                |        50.33 |
|  856 | Osan, South Korea                             |        50.25 |
|  857 | Qinzhou, China                                |        50.25 |
|  858 | Tongjin, South Korea                          |        50.17 |
|  859 | Shimla, India                                 |        50.17 |
|  860 | San Fernando, Chile                           |        50.17 |
|  861 | Paracin, Serbia                               |        50.08 |
|  862 | Kunsan, South Korea                           |        50.08 |
|  863 | Ashgabat, Turkmenistan                        |        50.08 |
|  864 | Jinghong, China                               |        49.92 |
|  865 | Nanning, China                                |        49.92 |
|  866 | Erzincan, Turkey                              |        49.83 |
|  867 | Lusaka, Zambia                                |        49.83 |
|  868 | Incheon, South Korea                          |        49.67 |
|  869 | Ganzhou, China                                |        49.67 |
|  870 | Talcahuano, Chile                             |        49.5  |
|  871 | Giddalur, India                               |        49.42 |
|  872 | Tinnevelly, India                             |        49.42 |
|  873 | Chihuahua, Mexico                             |        49.42 |
|  874 | Sandton, South Africa                         |        49.42 |
|  875 | Suphan Buri, Thailand                         |        49.33 |
|  876 | Duzce, Turkey                                 |        49.33 |
|  877 | Kilis, Turkey                                 |        49.33 |
|  878 | Los Angeles, Chile                            |        49.25 |
|  879 | Slavonski Brod, Croatia                       |        49.25 |
|  880 | Ansan, South Korea                            |        49.17 |
|  881 | Samut Songkhram, Thailand                     |        49.17 |
|  882 | Mardin, Turkey                                |        49.17 |
|  883 | Guankou, China                                |        49.17 |
|  884 | Kurnool, India                                |        49.08 |
|  885 | Salamanca, Mexico                             |        49.08 |
|  886 | Calexico, United States                       |        49.08 |
|  887 | Quanzhou, China                               |        49.08 |
|  888 | At Tafilah, Jordan                            |        49    |
|  889 | Pattani, Thailand                             |        49    |
|  890 | Drug, India                                   |        48.92 |
|  891 | Solapur, India                                |        48.92 |
|  892 | Vranje, Serbia                                |        48.92 |
|  893 | Gimpo, South Korea                            |        48.92 |
|  894 | Balikesir, Turkey                             |        48.92 |
|  895 | Kunpo, South Korea                            |        48.83 |
|  896 | Phra Nakhon Si Ayutthaya, Thailand            |        48.83 |
|  897 | Hosan, South Korea                            |        48.75 |
|  898 | Zunyi, China                                  |        48.75 |
|  899 | Jammalamadugu, India                          |        48.67 |
|  900 | Tadpatri, India                               |        48.67 |
|  901 | Goyang, South Korea                           |        48.67 |
|  902 | Nizip, Turkey                                 |        48.58 |
|  903 | Sakarya, Turkey                               |        48.58 |
|  904 | Soma, Turkey                                  |        48.58 |
|  905 | Huangshan, China                              |        48.58 |
|  906 | Beirut, Lebanon                               |        48.5  |
|  907 | Hongseong, South Korea                        |        48.5  |
|  908 | Proddatur, India                              |        48.42 |
|  909 | Batken, Kyrgyzstan                            |        48.42 |
|  910 | Changyon, North Korea                         |        48.33 |
|  911 | Nakhon Pathom, Thailand                       |        48.33 |
|  912 | Nandyal, India                                |        48.25 |
|  913 | Suwon, South Korea                            |        48.25 |
|  914 | Tha Bo, Thailand                              |        48.25 |
|  915 | Bellary, India                                |        48.17 |
|  916 | Sanliurfa, Turkey                             |        48.17 |
|  917 | Temuco, Chile                                 |        48.08 |
|  918 | Chaozhou, China                               |        48.08 |
|  919 | Guangzhou, China                              |        48.08 |
|  920 | Lincang, China                                |        48.08 |
|  921 | Skopje, Macedonia                             |        48.08 |
|  922 | Valle Alto, Mexico                            |        48.08 |
|  923 | Bucheon, South Korea                          |        48.08 |
|  924 | Hospet, India                                 |        48    |
|  925 | Tokmok, Kyrgyzstan                            |        48    |
|  926 | Shaoguan, China                               |        47.92 |
|  927 | Irapuato, Mexico                              |        47.92 |
|  928 | Anyang, South Korea                           |        47.92 |
|  929 | Sosan, South Korea                            |        47.92 |
|  930 | Yoju, South Korea                             |        47.92 |
|  931 | Phrae, Thailand                               |        47.92 |
|  932 | Guadalupe, Mexico                             |        47.83 |
|  933 | Kimje, South Korea                            |        47.83 |
|  934 | Guiyang, China                                |        47.75 |
|  935 | Gornji Milanovac, Serbia                      |        47.67 |
|  936 | Kilimli, Turkey                               |        47.67 |
|  937 | Tekirdag, Turkey                              |        47.58 |
|  938 | Linhai, China                                 |        47.5  |
|  939 | Kozani, Greece                                |        47.5  |
|  940 | Koilkuntla, India                             |        47.5  |
|  941 | Adana, Turkey                                 |        47.5  |
|  942 | Tizayuca, Mexico                              |        47.25 |
|  943 | Qingyuan, China                               |        47.25 |
|  944 | Foshan, China                                 |        47.17 |
|  945 | Asan, South Korea                             |        47.08 |
|  946 | Yongju, South Korea                           |        47.08 |
|  947 | Cheongju, South Korea                         |        47    |
|  948 | Eumseong, South Korea                         |        47    |
|  949 | Huatan, Taiwan                                |        47    |
|  950 | Taizhou, China                                |        46.92 |
|  951 | Prachin Buri, Thailand                        |        46.83 |
|  952 | Calipatria, United States                     |        46.83 |
|  953 | Cubatao, Brazil                               |        46.83 |
|  954 | Morelia, Mexico                               |        46.75 |
|  955 | Kaesong, North Korea                          |        46.58 |
|  956 | Ongjang, North Korea                          |        46.58 |
|  957 | Uttaradit, Thailand                           |        46.58 |
|  958 | Thiruvananthapuram, India                     |        46.58 |
|  959 | Sejong, South Korea                           |        46.5  |
|  960 | Saraburi, Thailand                            |        46.5  |
|  961 | Kolar, India                                  |        46.5  |
|  962 | Guntakal, India                               |        46.42 |
|  963 | Denizli, Turkey                               |        46.33 |
|  964 | Belgaum, India                                |        46.25 |
|  965 | Nagercoil, India                              |        46.17 |
|  966 | Chungju, South Korea                          |        46.17 |
|  967 | Hegang, China                                 |        46.17 |
|  968 | Chula Vista, United States                    |        46.08 |
|  969 | Ilam, Iran                                    |        46    |
|  970 | Heshan, China                                 |        45.92 |
|  971 | Kunming, China                                |        45.92 |
|  972 | Bishnupur, India                              |        45.83 |
|  973 | Hanford, United States                        |        45.83 |
|  974 | Zhaoqing, China                               |        45.83 |
|  975 | Jiaojiangcun, China                           |        45.67 |
|  976 | Gwacheon, South Korea                         |        45.58 |
|  977 | Rustenburg, South Africa                      |        45.5  |
|  978 | Jeonju, South Korea                           |        45.5  |
|  979 | Songnam, South Korea                          |        45.5  |
|  980 | Khed Brahma, India                            |        45.42 |
|  981 | Bitola, Macedonia                             |        45.42 |
|  982 | Pozarevac, Serbia                             |        45.42 |
|  983 | Boryeong, South Korea                         |        45.42 |
|  984 | Gwangmyeongni, South Korea                    |        45.42 |
|  985 | Bangkok, Thailand                             |        45.42 |
|  986 | Qianzhou, China                               |        45.25 |
|  987 | Valjevo, Serbia                               |        45.25 |
|  988 | Seoul, South Korea                            |        45.25 |
|  989 | Talca, Chile                                  |        45.17 |
|  990 | Beihai, China                                 |        45.17 |
|  991 | Lichuan, China                                |        45.17 |
|  992 | Putian, China                                 |        45.17 |
|  993 | Rameswaram, India                             |        45.17 |
|  994 | Uiwang, South Korea                           |        45.17 |
|  995 | Chiayi, Taiwan                                |        45.17 |
|  996 | Kaohsiung, Taiwan                             |        45.17 |
|  997 | Jiangmen, China                               |        45.08 |
|  998 | Qujing, China                                 |        45.08 |
|  999 | Chikkaballapur, India                         |        45.08 |
| 1000 | Yakacik, Turkey                               |        45.08 |
| 1001 | Shahr E Jadid E Hashtgerd, Iran               |        45    |
| 1002 | Sunland Park, United States                   |        45    |
| 1003 | Jeonghae, South Korea                         |        45    |
| 1004 | Sangju, South Korea                           |        45    |
| 1005 | Corum, Turkey                                 |        45    |
| 1006 | Hanam, South Korea                            |        44.92 |
| 1007 | Paju, South Korea                             |        44.92 |
| 1008 | Mae Sot, Thailand                             |        44.92 |
| 1009 | Lykovrysi, Greece                             |        44.83 |
| 1010 | Uijeongbu, South Korea                        |        44.75 |
| 1011 | Silchar, India                                |        44.67 |
| 1012 | Algodones, Mexico                             |        44.67 |
| 1013 | Guri, South Korea                             |        44.67 |
| 1014 | Kihung, South Korea                           |        44.67 |
| 1015 | Badvel, India                                 |        44.5  |
| 1016 | Yanggok, South Korea                          |        44.5  |
| 1017 | Havran, Turkey                                |        44.42 |
| 1018 | Antananarivo, Madagascar                      |        44.42 |
| 1019 | Yong'an, China                                |        44.42 |
| 1020 | Jicheon, South Korea                          |        44.33 |
| 1021 | Muan, South Korea                             |        44.25 |
| 1022 | Bang Kruai, Thailand                          |        44.25 |
| 1023 | Antalya, Turkey                               |        44.25 |
| 1024 | Kohima, India                                 |        44.25 |
| 1025 | Daejeon, South Korea                          |        44.17 |
| 1026 | Kumi, South Korea                             |        44.17 |
| 1027 | Puchuncavi, Chile                             |        44.17 |
| 1028 | Mayfair, United States                        |        44.17 |
| 1029 | Douliu, Taiwan                                |        44.08 |
| 1030 | Nagqu, China                                  |        44.08 |
| 1031 | Pohang, South Korea                           |        44    |
| 1032 | Leon De Los Aldama, Mexico                    |        44    |
| 1033 | Santa Gertrudes, Brazil                       |        43.92 |
| 1034 | Gyeongsan, South Korea                        |        43.83 |
| 1035 | Rustavi, Georgia                              |        43.83 |
| 1036 | Wonju, South Korea                            |        43.75 |
| 1037 | Nikaia, Greece                                |        43.75 |
| 1038 | Rayachoti, India                              |        43.67 |
| 1039 | Tecozautla, Mexico                            |        43.67 |
| 1040 | Huangyan, China                               |        43.67 |
| 1041 | Tainan, Taiwan                                |        43.58 |
| 1042 | Agri, Turkey                                  |        43.58 |
| 1043 | Ondorhaan, Mongolia                           |        43.58 |
| 1044 | Dongguan, China                               |        43.58 |
| 1045 | Socorro, United States                        |        43.58 |
| 1046 | Dzuunmod, Mongolia                            |        43.5  |
| 1047 | Ningde, China                                 |        43.5  |
| 1048 | San Salvador, El Salvador                     |        43.5  |
| 1049 | Mossel Bay, South Africa                      |        43.33 |
| 1050 | Tokat, Turkey                                 |        43.33 |
| 1051 | Qiryat Malakhi, Israel                        |        43.25 |
| 1052 | Lansdowne, India                              |        43.17 |
| 1053 | Pekanbaru, Indonesia                          |        43.17 |
| 1054 | Kirklareli, Turkey                            |        43.17 |
| 1055 | Pazar, Turkey                                 |        43.17 |
| 1056 | Golcuk, Turkey                                |        43.08 |
| 1057 | Gjilan, Kosovo                                |        43    |
| 1058 | Pristina, Kosovo                              |        43    |
| 1059 | Daegu, South Korea                            |        42.92 |
| 1060 | Naju, South Korea                             |        42.92 |
| 1061 | Samut Prakan, Thailand                        |        42.92 |
| 1062 | Rangoon, Burma                                |        42.92 |
| 1063 | Izmir, Turkey                                 |        42.75 |
| 1064 | Mokpo, South Korea                            |        42.67 |
| 1065 | Yuanchang, Taiwan                             |        42.67 |
| 1066 | Edirne, Turkey                                |        42.67 |
| 1067 | Sanming, China                                |        42.67 |
| 1068 | Shantou, China                                |        42.58 |
| 1069 | Chechon, South Korea                          |        42.5  |
| 1070 | Heyuan, China                                 |        42.5  |
| 1071 | Bucaramanga, Colombia                         |        42.5  |
| 1072 | Al Quds, Israel                               |        42.33 |
| 1073 | Zejtun, Malta                                 |        42.25 |
| 1074 | Bakjagol, South Korea                         |        42.25 |
| 1075 | Magong, Taiwan                                |        42.25 |
| 1076 | Yellowknife, Canada                           |        42.17 |
| 1077 | Yunfu, China                                  |        42.17 |
| 1078 | Choybalsan, Mongolia                          |        42.08 |
| 1079 | Pocheon, South Korea                          |        42.08 |
| 1080 | Ulchin, South Korea                           |        42.08 |
| 1081 | Lishui, China                                 |        42    |
| 1082 | Zhuhai, China                                 |        42    |
| 1083 | Guadalajara, Mexico                           |        42    |
| 1084 | Centurion, South Africa                       |        42    |
| 1085 | Pozi, Taiwan                                  |        42    |
| 1086 | Yangjiang, China                              |        41.92 |
| 1087 | Dongducheon, South Korea                      |        41.92 |
| 1088 | Aguascalientes, Mexico                        |        41.83 |
| 1089 | Zhanjiang, China                              |        41.75 |
| 1090 | Shahrud, Iran                                 |        41.75 |
| 1091 | Mungyong, South Korea                         |        41.75 |
| 1092 | Kayseri, Turkey                               |        41.75 |
| 1093 | Libertad, Argentina                           |        41.67 |
| 1094 | Taiping, China                                |        41.67 |
| 1095 | Xiamen, China                                 |        41.67 |
| 1096 | Yakeshi, China                                |        41.67 |
| 1097 | Ulsan, South Korea                            |        41.67 |
| 1098 | Taibao, Taiwan                                |        41.67 |
| 1099 | Doboj, Bosnia And Herzegovina                 |        41.58 |
| 1100 | Chuxiong, China                               |        41.58 |
| 1101 | Maoming, China                                |        41.58 |
| 1102 | Lagos, Nigeria                                |        41.58 |
| 1103 | Amasya, Turkey                                |        41.58 |
| 1104 | Zhongshan, China                              |        41.5  |
| 1105 | Kety, Poland                                  |        41.5  |
| 1106 | Samch'ok, South Korea                         |        41.5  |
| 1107 | Kanchanaburi, Thailand                        |        41.42 |
| 1108 | Changhua, Taiwan                              |        41.33 |
| 1109 | Jammu, India                                  |        41.33 |
| 1110 | Palangkaraya, Indonesia                       |        41.33 |
| 1111 | Gwangju, South Korea                          |        41.25 |
| 1112 | Jeju, South Korea                             |        41.25 |
| 1113 | Pathankot, India                              |        41.25 |
| 1114 | Ban Bang Kaeo, Thailand                       |        41.17 |
| 1115 | Kocaeli, Turkey                               |        41.08 |
| 1116 | Tacheng, China                                |        41.08 |
| 1117 | Peje, Kosovo                                  |        41    |
| 1118 | Miles City, United States                     |        40.92 |
| 1119 | Elefsina, Greece                              |        40.83 |
| 1120 | Robat Karim, Iran                             |        40.83 |
| 1121 | Ilinden, Macedonia                            |        40.83 |
| 1122 | Sokcho, South Korea                           |        40.75 |
| 1123 | Yeosu, South Korea                            |        40.75 |
| 1124 | Kranuan, Thailand                             |        40.75 |
| 1125 | Corlu, Turkey                                 |        40.75 |
| 1126 | Concepcion, Chile                             |        40.75 |
| 1127 | Coloane, China                                |        40.75 |
| 1128 | Aliaga, Turkey                                |        40.67 |
| 1129 | Tarsus, Turkey                                |        40.67 |
| 1130 | Corcoran, United States                       |        40.67 |
| 1131 | Seogwipo, South Korea                         |        40.58 |
| 1132 | Qiryat Bialik, Israel                         |        40.58 |
| 1133 | Andong, South Korea                           |        40.5  |
| 1134 | Copiapo, Chile                                |        40.5  |
| 1135 | Punganuru, India                              |        40.5  |
| 1136 | Huizhou, China                                |        40.42 |
| 1137 | Gwangyang, South Korea                        |        40.42 |
| 1138 | Kandy, Sri Lanka                              |        40.42 |
| 1139 | Semnan, Iran                                  |        40.33 |
| 1140 | Saqqez, Iran                                  |        40.25 |
| 1141 | Saveh, Iran                                   |        40.25 |
| 1142 | Zhongli, Taiwan                               |        40.17 |
| 1143 | Erzurum, Turkey                               |        40.17 |
| 1144 | Bengkulu, Indonesia                           |        40.08 |
| 1145 | Chuncheon, South Korea                        |        40.08 |
| 1146 | Cam Pha, Vietnam                              |        40.08 |
| 1147 | Gumushane, Turkey                             |        40    |
| 1148 | Ban Map Ta Phut, Thailand                     |        39.92 |
| 1149 | Tepic, Mexico                                 |        39.83 |
| 1150 | Masan, South Korea                            |        39.75 |
| 1151 | Stary Sacz, Poland                            |        39.67 |
| 1152 | Nangan, Taiwan                                |        39.67 |
| 1153 | Eregli, Turkey                                |        39.67 |
| 1154 | Cuernavaca, Mexico                            |        39.58 |
| 1155 | Busan, South Korea                            |        39.58 |
| 1156 | Ershui, Taiwan                                |        39.58 |
| 1157 | Ta Xbiex, Malta                               |        39.5  |
| 1158 | Lhasa, China                                  |        39.5  |
| 1159 | Zhoushan, China                               |        39.5  |
| 1160 | Negotin, Serbia                               |        39.5  |
| 1161 | Chalandri, Greece                             |        39.42 |
| 1162 | Niksic, Montenegro                            |        39.42 |
| 1163 | Podgorica, Montenegro                         |        39.42 |
| 1164 | Kyongju, South Korea                          |        39.42 |
| 1165 | Menderes, Turkey                              |        39.42 |
| 1166 | Davenport, United States                      |        39.42 |
| 1167 | Shimoga, India                                |        39.33 |
| 1168 | Givatayim, Israel                             |        39.33 |
| 1169 | Durango, Mexico                               |        39.33 |
| 1170 | Ch'ungmu, South Korea                         |        39.33 |
| 1171 | Kimhae, South Korea                           |        39.33 |
| 1172 | Kermanshah, Iran                              |        39.25 |
| 1173 | Meizhou, China                                |        39.17 |
| 1174 | Bokhtar, Tajikistan                           |        39.17 |
| 1175 | Bakersfield, United States                    |        39.17 |
| 1176 | Muscatine, United States                      |        39.08 |
| 1177 | Shenzhen, China                               |        39.08 |
| 1178 | Petrvald, Czechia                             |        39.08 |
| 1179 | San Luis Potosi, Mexico                       |        39.08 |
| 1180 | Mandalgovi, Mongolia                          |        39.08 |
| 1181 | South Valley, United States                   |        39    |
| 1182 | Taoyuan District, Taiwan                      |        39    |
| 1183 | Chinju, South Korea                           |        38.92 |
| 1184 | Victorville, United States                    |        38.83 |
| 1185 | Unye, Turkey                                  |        38.83 |
| 1186 | Luzhang, China                                |        38.75 |
| 1187 | Famagusta, Cyprus                             |        38.75 |
| 1188 | Taebaek, South Korea                          |        38.67 |
| 1189 | Hassan, India                                 |        38.58 |
| 1190 | Kolhapur, India                               |        38.58 |
| 1191 | Yogyakarta, Indonesia                         |        38.58 |
| 1192 | Sanandaj, Iran                                |        38.58 |
| 1193 | Yehud, Israel                                 |        38.58 |
| 1194 | Miryang, South Korea                          |        38.58 |
| 1195 | Bandung, Indonesia                            |        38.5  |
| 1196 | Gangneung, South Korea                        |        38.5  |
| 1197 | Tome, Chile                                   |        38.33 |
| 1198 | Thessaloniki, Greece                          |        38.33 |
| 1199 | Tautii Magherus, Romania                      |        38.25 |
| 1200 | Changwon, South Korea                         |        38.25 |
| 1201 | Kars, Turkey                                  |        38.25 |
| 1202 | Samsun, Turkey                                |        38.25 |
| 1203 | Arrecife, Spain                               |        38.17 |
| 1204 | Abu, India                                    |        38.17 |
| 1205 | Suncheon, South Korea                         |        38    |
| 1206 | Cayirova, Turkey                              |        38    |
| 1207 | Yalova, Turkey                                |        38    |
| 1208 | Alerce, Chile                                 |        38    |
| 1209 | Shanwei, China                                |        38    |
| 1210 | Jurupa Valley, United States                  |        38    |
| 1211 | Rock Island, United States                    |        38    |
| 1212 | Srinagar, India                               |        38    |
| 1213 | Yangsan, South Korea                          |        37.75 |
| 1214 | Khlong Luang, Thailand                        |        37.75 |
| 1215 | Phra Pradaeng, Thailand                       |        37.75 |
| 1216 | Sisak, Croatia                                |        37.75 |
| 1217 | Kadiri, India                                 |        37.75 |
| 1218 | Pachuca, Mexico                               |        37.75 |
| 1219 | Karakol, Kyrgyzstan                           |        37.67 |
| 1220 | Yangmei, Taiwan                               |        37.58 |
| 1221 | Longyan, China                                |        37.58 |
| 1222 | Qiryat Gat, Israel                            |        37.58 |
| 1223 | Klodzko, Poland                               |        37.58 |
| 1224 | Tak, Thailand                                 |        37.5  |
| 1225 | Harrisville, United States                    |        37.5  |
| 1226 | Nanping, China                                |        37.5  |
| 1227 | Larnaca, Cyprus                               |        37.5  |
| 1228 | Donegal, Ireland                              |        37.5  |
| 1229 | Akko, Israel                                  |        37.5  |
| 1230 | Prizren, Kosovo                               |        37.42 |
| 1231 | Rio Claro, Brazil                             |        37.42 |
| 1232 | Dongxing, China                               |        37.42 |
| 1233 | Libreville, Gabon                             |        37.42 |
| 1234 | Krakow, Poland                                |        37.42 |
| 1235 | Qiryat Mozqin, Israel                         |        37.33 |
| 1236 | Calama, Chile                                 |        37.33 |
| 1237 | La Union, Chile                               |        37.33 |
| 1238 | Novo Mesto, Slovenia                          |        37.33 |
| 1239 | Sa Chon, South Korea                          |        37.33 |
| 1240 | Taichung, Taiwan                              |        37.33 |
| 1241 | Kutahya, Turkey                               |        37.33 |
| 1242 | Ban Laem Chabang, Thailand                    |        37.25 |
| 1243 | Makassar, Indonesia                           |        37.08 |
| 1244 | Dalanzadgad, Mongolia                         |        37.08 |
| 1245 | Chicureo Abajo, Chile                         |        37.08 |
| 1246 | Madanapalle, India                            |        37    |
| 1247 | Shtime, Kosovo                                |        37    |
| 1248 | Rayong, Thailand                              |        37    |
| 1249 | Trabzon, Turkey                               |        37    |
| 1250 | Mysore, India                                 |        36.92 |
| 1251 | Gharb, Malta                                  |        36.92 |
| 1252 | Baoshan, China                                |        36.83 |
| 1253 | Las Palmas, Spain                             |        36.83 |
| 1254 | Rapid City, United States                     |        36.83 |
| 1255 | Zanjan, Iran                                  |        36.75 |
| 1256 | Curanilahue, Chile                            |        36.75 |
| 1257 | Lublin, Poland                                |        36.75 |
| 1258 | Turin, Italy                                  |        36.67 |
| 1259 | Wood Buffalo, Canada                          |        36.67 |
| 1260 | Coronel, Chile                                |        36.67 |
| 1261 | Jilove, Czechia                               |        36.67 |
| 1262 | Tarnow, Poland                                |        36.67 |
| 1263 | Pingtung, Taiwan                              |        36.67 |
| 1264 | Mandya, India                                 |        36.58 |
| 1265 | Ocatlan, Mexico                               |        36.58 |
| 1266 | Ruse, Bulgaria                                |        36.58 |
| 1267 | Celje, Slovenia                               |        36.58 |
| 1268 | Fresno, United States                         |        36.58 |
| 1269 | Kerman, Iran                                  |        36.5  |
| 1270 | Franco Da Rocha, Brazil                       |        36.42 |
| 1271 | Limeira, Brazil                               |        36.42 |
| 1272 | Shrirangapattana, India                       |        36.42 |
| 1273 | Mmabatho, South Africa                        |        36.42 |
| 1274 | Havirov, Czechia                              |        36.33 |
| 1275 | Puerto De La Cruz, Spain                      |        36.33 |
| 1276 | Manisa, Turkey                                |        36.33 |
| 1277 | Decin, Czechia                                |        36.25 |
| 1278 | Koper, Slovenia                               |        36.25 |
| 1279 | Canteras, Spain                               |        36.25 |
| 1280 | Pak Kret, Thailand                            |        36.25 |
| 1281 | Cleveland, United States                      |        36.25 |
| 1282 | Senov, Czechia                                |        36.17 |
| 1283 | Dharmsala, India                              |        36.17 |
| 1284 | Az Zarqa, Jordan                              |        36.17 |
| 1285 | Murcia, Spain                                 |        36.17 |
| 1286 | Parigi, India                                 |        36.08 |
| 1287 | Ashqelon, Israel                              |        36.08 |
| 1288 | Sederot, Israel                               |        36.08 |
| 1289 | La Laguna, Spain                              |        36.08 |
| 1290 | Aksaray, Turkey                               |        36.08 |
| 1291 | Bolu, Turkey                                  |        36.08 |
| 1292 | Da Nang, Vietnam                              |        36    |
| 1293 | Qiryat Ata, Israel                            |        36    |
| 1294 | Tbilisi, Georgia                              |        35.92 |
| 1295 | Ootacamund, India                             |        35.92 |
| 1296 | Juarez, Mexico                                |        35.92 |
| 1297 | Jelenia Gora, Poland                          |        35.92 |
| 1298 | Middelburg, South Africa                      |        35.92 |
| 1299 | Ubon Ratchathani, Thailand                    |        35.92 |
| 1300 | Istanbul, Turkey                              |        35.92 |
| 1301 | Baku, Azerbaijan                              |        35.83 |
| 1302 | Bihac, Bosnia And Herzegovina                 |        35.83 |
| 1303 | Ceska Lipa, Czechia                           |        35.83 |
| 1304 | Pulivendla, India                             |        35.83 |
| 1305 | Wloclawek, Poland                             |        35.83 |
| 1306 | Santa Cruz, Spain                             |        35.83 |
| 1307 | Sivas, Turkey                                 |        35.83 |
| 1308 | Aosta, Italy                                  |        35.75 |
| 1309 | Mizil, Romania                                |        35.75 |
| 1310 | Zonguldak, Turkey                             |        35.75 |
| 1311 | Chaparral, United States                      |        35.75 |
| 1312 | Nazarabad, Iran                               |        35.67 |
| 1313 | Tambov, Russia                                |        35.67 |
| 1314 | Luleburgaz, Turkey                            |        35.67 |
| 1315 | Catanduva, Brazil                             |        35.58 |
| 1316 | Ichalkaranji, India                           |        35.58 |
| 1317 | City of Paranaque, Philippines                |        35.58 |
| 1318 | Lebork, Poland                                |        35.58 |
| 1319 | Revuca, Slovakia                              |        35.58 |
| 1320 | Kapakli, Turkey                               |        35.58 |
| 1321 | Clovis, United States                         |        35.58 |
| 1322 | Bafra, Turkey                                 |        35.5  |
| 1323 | Kryvyy Rih, Ukraine                           |        35.5  |
| 1324 | Marmara Ereglisi, Turkey                      |        35.42 |
| 1325 | Ostrava, Czechia                              |        35.42 |
| 1326 | Haiphong, Vietnam                             |        35.42 |
| 1327 | Nakhon Sawan, Thailand                        |        35.33 |
| 1328 | Kodaikanal, India                             |        35.33 |
| 1329 | Prokuplje, Serbia                             |        35.25 |
| 1330 | Burdur, Turkey                                |        35.25 |
| 1331 | Nicosia, Cyprus                               |        35.25 |
| 1332 | Tempe, United States                          |        35.25 |
| 1333 | Arad, Israel                                  |        35.25 |
| 1334 | Kirikkale, Turkey                             |        35.17 |
| 1335 | Ulubey, Turkey                                |        35.17 |
| 1336 | Fort St John, Canada                          |        35.17 |
| 1337 | Turlock, United States                        |        35.17 |
| 1338 | Fort Bliss, United States                     |        35.08 |
| 1339 | Ribeirao Preto, Brazil                        |        35.08 |
| 1340 | Dayan, China                                  |        35.08 |
| 1341 | Nis, Serbia                                   |        35    |
| 1342 | Glendale, United States                       |        35    |
| 1343 | Herriman, United States                       |        35    |
| 1344 | Thu Dau Mot, Vietnam                          |        35    |
| 1345 | Nopala De Villagran, Mexico                   |        35    |
| 1346 | Vratimov, Czechia                             |        34.92 |
| 1347 | Al `Amarah, Iraq                              |        34.92 |
| 1348 | Turzovka, Slovakia                            |        34.83 |
| 1349 | Ankara, Turkey                                |        34.83 |
| 1350 | Korfez, Turkey                                |        34.83 |
| 1351 | Gar, China                                    |        34.83 |
| 1352 | Sahy, Slovakia                                |        34.75 |
| 1353 | Nantou, Taiwan                                |        34.75 |
| 1354 | Ardahan, Turkey                               |        34.75 |
| 1355 | Anthony, United States                        |        34.75 |
| 1356 | Bossier City, United States                   |        34.75 |
| 1357 | Chanute, United States                        |        34.75 |
| 1358 | Trogir, Croatia                               |        34.75 |
| 1359 | Bulgan, Mongolia                              |        34.75 |
| 1360 | Nova Gorica, Slovenia                         |        34.58 |
| 1361 | Bade, Taiwan                                  |        34.58 |
| 1362 | Nakhon Phanom, Thailand                       |        34.58 |
| 1363 | Qom, Iran                                     |        34.58 |
| 1364 | Katherine, Australia                          |        34.5  |
| 1365 | Xinqing, China                                |        34.5  |
| 1366 | Vitkov, Czechia                               |        34.5  |
| 1367 | Pardes Hanna Karkur, Israel                   |        34.5  |
| 1368 | Haikou, China                                 |        34.42 |
| 1369 | Nigde, Turkey                                 |        34.42 |
| 1370 | Belur, India                                  |        34.33 |
| 1371 | Cesky Tesin, Czechia                          |        34.33 |
| 1372 | Zagorje, Slovenia                             |        34.33 |
| 1373 | Gijon, Spain                                  |        34.33 |
| 1374 | Crestline, United States                      |        34.33 |
| 1375 | Puerto Montt, Chile                           |        34.25 |
| 1376 | Kraljevo, Serbia                              |        34.25 |
| 1377 | Buje, Croatia                                 |        34.17 |
| 1378 | Dakar, Senegal                                |        34.17 |
| 1379 | Eskisehir, Turkey                             |        34.17 |
| 1380 | Sangli, India                                 |        34.08 |
| 1381 | Watertown, United States                      |        34.08 |
| 1382 | Lima, Peru                                    |        34    |
| 1383 | Zagreb, Croatia                               |        34    |
| 1384 | Jagodina, Serbia                              |        34    |
| 1385 | Ban Lam Sam Kaeo, Thailand                    |        34    |
| 1386 | Tulsa, United States                          |        34    |
| 1387 | Darjeeling, India                             |        33.92 |
| 1388 | Tumkur, India                                 |        33.92 |
| 1389 | Netanya, Israel                               |        33.92 |
| 1390 | Itaquaquecetuba, Brazil                       |        33.92 |
| 1391 | Altay, China                                  |        33.92 |
| 1392 | Saint Denis, France                           |        33.92 |
| 1393 | Pretoria, South Africa                        |        33.92 |
| 1394 | Patnos, Turkey                                |        33.92 |
| 1395 | Phoenix, United States                        |        33.92 |
| 1396 | Kobylka, Poland                               |        33.83 |
| 1397 | Niepolomice, Poland                           |        33.83 |
| 1398 | Nakhon Si Thammarat, Thailand                 |        33.83 |
| 1399 | Murree, Pakistan                              |        33.75 |
| 1400 | Piracicaba, Brazil                            |        33.75 |
| 1401 | Keelung, Taiwan                               |        33.75 |
| 1402 | Mulvane, United States                        |        33.75 |
| 1403 | Yoqneam Illit, Israel                         |        33.67 |
| 1404 | Al Aqabah, Jordan                             |        33.67 |
| 1405 | Jeddah, Saudi Arabia                          |        33.67 |
| 1406 | Alpine, United States                         |        33.67 |
| 1407 | Puerto Aysen, Chile                           |        33.58 |
| 1408 | Marignane, France                             |        33.58 |
| 1409 | Ub, Serbia                                    |        33.58 |
| 1410 | Lorca, Spain                                  |        33.58 |
| 1411 | Khon Kaen, Thailand                           |        33.58 |
| 1412 | Paulinia, Brazil                              |        33.5  |
| 1413 | Slavicin, Czechia                             |        33.5  |
| 1414 | Wschowa, Poland                               |        33.5  |
| 1415 | Banqiao, Taiwan                               |        33.5  |
| 1416 | Pontianak, Indonesia                          |        33.42 |
| 1417 | Banak, Iran                                   |        33.42 |
| 1418 | Polokwane, South Africa                       |        33.42 |
| 1419 | Ferraz De Vasconcelos, Brazil                 |        33.33 |
| 1420 | Beroun, Czechia                               |        33.33 |
| 1421 | Piastow, Poland                               |        33.33 |
| 1422 | Banning, United States                        |        33.33 |
| 1423 | Modesto, United States                        |        33.25 |
| 1424 | Jirkov, Czechia                               |        33.25 |
| 1425 | Kielce, Poland                                |        33.25 |
| 1426 | Hsinchu, Taiwan                               |        33.25 |
| 1427 | Jefferson, United States                      |        33.17 |
| 1428 | Zemun, Serbia                                 |        33.17 |
| 1429 | Yala, Thailand                                |        33.17 |
| 1430 | Bartin, Turkey                                |        33.17 |
| 1431 | Bilecik, Turkey                               |        33.17 |
| 1432 | Prince George, Canada                         |        33.08 |
| 1433 | Ricany, Czechia                               |        33.08 |
| 1434 | Otwock, Poland                                |        33.08 |
| 1435 | Guarulhos, Brazil                             |        33    |
| 1436 | Nada, China                                   |        33    |
| 1437 | Opava, Czechia                                |        33    |
| 1438 | Grass Valley, United States                   |        33    |
| 1439 | Roosevelt, United States                      |        32.92 |
| 1440 | Studenka, Czechia                             |        32.92 |
| 1441 | Zabrze, Poland                                |        32.92 |
| 1442 | Leacock, United States                        |        32.83 |
| 1443 | Conakry, Guinea                               |        32.83 |
| 1444 | Hirado, Japan                                 |        32.83 |
| 1445 | Randburg, South Africa                        |        32.83 |
| 1446 | Cartagena, Spain                              |        32.83 |
| 1447 | Glendora, United States                       |        32.83 |
| 1448 | North Valley, United States                   |        32.75 |
| 1449 | Frydek Mistek, Czechia                        |        32.75 |
| 1450 | Nove Mesto Nad Metuji, Czechia                |        32.75 |
| 1451 | Miaoli, Taiwan                                |        32.75 |
| 1452 | Yozgat, Turkey                                |        32.75 |
| 1453 | Usti Nad Labem, Czechia                       |        32.67 |
| 1454 | Tabriz, Iran                                  |        32.67 |
| 1455 | Radom, Poland                                 |        32.67 |
| 1456 | Pingzhen, Taiwan                              |        32.67 |
| 1457 | Nakhon Ratchasima, Thailand                   |        32.67 |
| 1458 | Kenner, United States                         |        32.58 |
| 1459 | Vimperk, Czechia                              |        32.58 |
| 1460 | Omachi, Japan                                 |        32.58 |
| 1461 | Lindon, United States                         |        32.5  |
| 1462 | Vina Del Mar, Chile                           |        32.5  |
| 1463 | Fukang, China                                 |        32.5  |
| 1464 | Trhove Sviny, Czechia                         |        32.5  |
| 1465 | Trinec, Czechia                               |        32.5  |
| 1466 | Kamigoto, Japan                               |        32.5  |
| 1467 | Katowice, Poland                              |        32.5  |
| 1468 | Torun, Poland                                 |        32.42 |
| 1469 | Osasco, Brazil                                |        32.42 |
| 1470 | Coudekerque Branche, France                   |        32.42 |
| 1471 | Pocatello, United States                      |        32.42 |
| 1472 | Bydgoszcz, Poland                             |        32.42 |
| 1473 | Motril, Spain                                 |        32.33 |
| 1474 | Plasencia, Spain                              |        32.33 |
| 1475 | Zhubei, Taiwan                                |        32.33 |
| 1476 | Findikli, Turkey                              |        32.33 |
| 1477 | Taguig City, Philippines                      |        32.33 |
| 1478 | Kastamonu, Turkey                             |        32.25 |
| 1479 | Covington, United States                      |        32.25 |
| 1480 | Rybnik, Poland                                |        32.17 |
| 1481 | Antequera, Spain                              |        32.17 |
| 1482 | Chico, United States                          |        32.17 |
| 1483 | Whitehorse, Canada                            |        32.17 |
| 1484 | Antofagasta, Chile                            |        32.17 |
| 1485 | Karvina, Czechia                              |        32.17 |
| 1486 | Moravska Trebova, Czechia                     |        32.17 |
| 1487 | Cao Bang, Vietnam                             |        32.17 |
| 1488 | Bijapur, India                                |        32.17 |
| 1489 | Hani I Elezit, Kosovo                         |        32.17 |
| 1490 | Piedras Blancas, Spain                        |        32.08 |
| 1491 | Taipei, Taiwan                                |        32.08 |
| 1492 | Brookings, United States                      |        32.08 |
| 1493 | Sao Caetano Do Sul, Brazil                    |        32.08 |
| 1494 | Basuo, China                                  |        32.08 |
| 1495 | Jiaji, China                                  |        32.08 |
| 1496 | Jesenik, Czechia                              |        32.08 |
| 1497 | Lake Elsinore, United States                  |        32.08 |
| 1498 | Attard, Malta                                 |        32.08 |
| 1499 | Oviedo, Spain                                 |        32    |
| 1500 | Finike, Turkey                                |        32    |
| 1501 | Abidjan, Cote D’Ivoire                        |        32    |
| 1502 | Moore, United States                          |        32    |
| 1503 | Nur Sultan, Kazakhstan                        |        32    |
| 1504 | Drobeta Turnu Severin, Romania                |        31.92 |
| 1505 | Aviles, Spain                                 |        31.92 |
| 1506 | Most, Czechia                                 |        31.92 |
| 1507 | Prerov, Czechia                               |        31.92 |
| 1508 | Trutnov, Czechia                              |        31.92 |
| 1509 | Orange Cove, United States                    |        31.92 |
| 1510 | Osijek, Croatia                               |        31.83 |
| 1511 | Litvinov, Czechia                             |        31.83 |
| 1512 | Maryville, United States                      |        31.83 |
| 1513 | South Tucson, United States                   |        31.83 |
| 1514 | Arcos De La Frontera, Spain                   |        31.75 |
| 1515 | Jaen, Spain                                   |        31.75 |
| 1516 | Aberdeen, China                               |        31.75 |
| 1517 | Sabac, Serbia                                 |        31.67 |
| 1518 | Aranyaprathet, Thailand                       |        31.67 |
| 1519 | Karabuk, Turkey                               |        31.67 |
| 1520 | Grande Prairie, Canada                        |        31.67 |
| 1521 | Telc, Czechia                                 |        31.67 |
| 1522 | Box Elder, United States                      |        31.58 |
| 1523 | Mrkonjic Grad, Bosnia And Herzegovina         |        31.58 |
| 1524 | Jacarei, Brazil                               |        31.58 |
| 1525 | Cenon, France                                 |        31.58 |
| 1526 | Colombo, Sri Lanka                            |        31.5  |
| 1527 | Thermi, Greece                                |        31.42 |
| 1528 | Hiji, Japan                                   |        31.42 |
| 1529 | Ita, Japan                                    |        31.42 |
| 1530 | Teplice, Czechia                              |        31.42 |
| 1531 | Rovinari, Romania                             |        31.42 |
| 1532 | Murska Sobota, Slovenia                       |        31.42 |
| 1533 | Sumperk, Czechia                              |        31.33 |
| 1534 | Granada, Spain                                |        31.33 |
| 1535 | Lao Cai, Vietnam                              |        31.33 |
| 1536 | Moranbah, Australia                           |        31.25 |
| 1537 | Araraquara, Brazil                            |        31.25 |
| 1538 | Gokcebey, Turkey                              |        31.25 |
| 1539 | East Porterville, United States               |        31.25 |
| 1540 | Kluczbork, Poland                             |        31.17 |
| 1541 | Krupka, Czechia                               |        31.17 |
| 1542 | Podcetrtek, Slovenia                          |        31.17 |
| 1543 | Bingol, Turkey                                |        31.17 |
| 1544 | Canakkale, Turkey                             |        31.17 |
| 1545 | Ipsala, Turkey                                |        31.17 |
| 1546 | Grand Rapids, United States                   |        31.08 |
| 1547 | Minot, United States                          |        31.08 |
| 1548 | Sao Sebastiao, Brazil                         |        31    |
| 1549 | Limassol, Cyprus                              |        31    |
| 1550 | Prostejov, Czechia                            |        31    |
| 1551 | Bismarck, United States                       |        31    |
| 1552 | Valparai, India                               |        30.92 |
| 1553 | Bogota, Colombia                              |        30.92 |
| 1554 | Mielec, Poland                                |        30.92 |
| 1555 | Priboj, Serbia                                |        30.92 |
| 1556 | Clairton, United States                       |        30.92 |
| 1557 | Dickinson, United States                      |        30.92 |
| 1558 | East Los Angeles, United States               |        30.92 |
| 1559 | Imaricho Ko, Japan                            |        30.83 |
| 1560 | Hradec Kralove, Czechia                       |        30.83 |
| 1561 | Legnica, Poland                               |        30.83 |
| 1562 | Koga, Japan                                   |        30.75 |
| 1563 | Shingu, Japan                                 |        30.75 |
| 1564 | Castelnau Le Lez, France                      |        30.75 |
| 1565 | Mataro, Spain                                 |        30.75 |
| 1566 | San Adrian, Spain                             |        30.75 |
| 1567 | Wichita, United States                        |        30.75 |
| 1568 | Ishinari, Japan                               |        30.67 |
| 1569 | Gllogovc, Kosovo                              |        30.67 |
| 1570 | Americana, Brazil                             |        30.67 |
| 1571 | Rychvald, Czechia                             |        30.67 |
| 1572 | Pancevo, Serbia                               |        30.67 |
| 1573 | Gettysburg, United States                     |        30.67 |
| 1574 | Overland Park, United States                  |        30.67 |
| 1575 | Blatna, Czechia                               |        30.58 |
| 1576 | Pardubice, Czechia                            |        30.58 |
| 1577 | Manosque, France                              |        30.58 |
| 1578 | Lubon, Poland                                 |        30.58 |
| 1579 | Ibiza, Spain                                  |        30.58 |
| 1580 | Beaver Dam, United States                     |        30.58 |
| 1581 | Ranchettes, United States                     |        30.58 |
| 1582 | Smithfield, United States                     |        30.58 |
| 1583 | Fukuoka, Japan                                |        30.5  |
| 1584 | Kazo, Japan                                   |        30.5  |
| 1585 | Litomerice, Czechia                           |        30.5  |
| 1586 | Le Bouscat, France                            |        30.5  |
| 1587 | Valenciennes, France                          |        30.5  |
| 1588 | Omaha, United States                          |        30.42 |
| 1589 | Nimes, France                                 |        30.42 |
| 1590 | Xalapa, Mexico                                |        30.42 |
| 1591 | Rzeszow, Poland                               |        30.42 |
| 1592 | Palafrugell, Spain                            |        30.42 |
| 1593 | Indianapolis, United States                   |        30.33 |
| 1594 | Chomutov, Czechia                             |        30.33 |
| 1595 | Kladno, Czechia                               |        30.33 |
| 1596 | Pribram, Czechia                              |        30.33 |
| 1597 | Kurobeshin, Japan                             |        30.33 |
| 1598 | Nagasaki, Japan                               |        30.33 |
| 1599 | Sasaguri, Japan                               |        30.33 |
| 1600 | Tamana, Japan                                 |        30.33 |
| 1601 | Tulancingo, Mexico                            |        30.33 |
| 1602 | Granollers, Spain                             |        30.33 |
| 1603 | Derry Township, United States                 |        30.33 |
| 1604 | Topeka, United States                         |        30.25 |
| 1605 | Koshigaya, Japan                              |        30.25 |
| 1606 | Heroica Nogales, Mexico                       |        30.25 |
| 1607 | Gdynia, Poland                                |        30.25 |
| 1608 | Arth, Switzerland                             |        30.25 |
| 1609 | Santos, Brazil                                |        30.17 |
| 1610 | Merignac, France                              |        30.17 |
| 1611 | Iizuka, Japan                                 |        30.17 |
| 1612 | Osawa, Japan                                  |        30.17 |
| 1613 | Saijo, Japan                                  |        30.17 |
| 1614 | Shimabara, Japan                              |        30.17 |
| 1615 | Cacem, Portugal                               |        30.17 |
| 1616 | Osilnica, Slovenia                            |        30.17 |
| 1617 | Kromeriz, Czechia                             |        30.08 |
| 1618 | Mikulov, Czechia                              |        30.08 |
| 1619 | Arles, France                                 |        30.08 |
| 1620 | Nakatsu, Japan                                |        30.08 |
| 1621 | Tagaytay, Philippines                         |        30.08 |
| 1622 | Krompachy, Slovakia                           |        30.08 |
| 1623 | Port Talbot, United Kingdom                   |        30.08 |
| 1624 | Madera, United States                         |        30    |
| 1625 | Roudnice Nad Labem, Czechia                   |        30    |
| 1626 | Imabari, Japan                                |        30    |
| 1627 | Noda, Japan                                   |        30    |
| 1628 | Ogaki, Japan                                  |        30    |
| 1629 | Takanabe, Japan                               |        30    |
| 1630 | Jundiai, Brazil                               |        29.92 |
| 1631 | Kutna Hora, Czechia                           |        29.92 |
| 1632 | Prachatice, Czechia                           |        29.92 |
| 1633 | Talence, France                               |        29.92 |
| 1634 | Hasuda, Japan                                 |        29.92 |
| 1635 | Tachiarai, Japan                              |        29.92 |
| 1636 | Hays, United States                           |        29.92 |
| 1637 | Ogden, United States                          |        29.83 |
| 1638 | Steti, Czechia                                |        29.83 |
| 1639 | Angouleme, France                             |        29.83 |
| 1640 | Hanyu, Japan                                  |        29.83 |
| 1641 | Kanonjicho, Japan                             |        29.83 |
| 1642 | Kasaoka, Japan                                |        29.83 |
| 1643 | Kasukabe, Japan                               |        29.83 |
| 1644 | Kumagaya, Japan                               |        29.83 |
| 1645 | Burgos, Spain                                 |        29.83 |
| 1646 | Ban Talat Rangsit, Thailand                   |        29.83 |
| 1647 | Lancaster, United States                      |        29.75 |
| 1648 | Lander, United States                         |        29.75 |
| 1649 | South Salt Lake, United States                |        29.75 |
| 1650 | Spanish Fork, United States                   |        29.75 |
| 1651 | Kadan, Czechia                                |        29.75 |
| 1652 | Olomouc, Czechia                              |        29.75 |
| 1653 | Joso, Japan                                   |        29.75 |
| 1654 | Kitatajima, Japan                             |        29.75 |
| 1655 | Masaki, Japan                                 |        29.75 |
| 1656 | Minamishiro, Japan                            |        29.75 |
| 1657 | Tatebayashi, Japan                            |        29.75 |
| 1658 | Neuchatel, Switzerland                        |        29.75 |
| 1659 | Karaman, Turkey                               |        29.75 |
| 1660 | Gary, United States                           |        29.75 |
| 1661 | Sidney, United States                         |        29.67 |
| 1662 | Kunisakimachi Tsurugawa, Japan                |        29.67 |
| 1663 | Muroran, Japan                                |        29.67 |
| 1664 | Yuasa, Japan                                  |        29.67 |
| 1665 | Temirtau, Kazakhstan                          |        29.67 |
| 1666 | Horta, Portugal                               |        29.67 |
| 1667 | Moguer, Spain                                 |        29.67 |
| 1668 | Tudela, Spain                                 |        29.67 |
| 1669 | Udon Thani, Thailand                          |        29.67 |
| 1670 | Logan, United States                          |        29.58 |
| 1671 | Progress Village, United States               |        29.58 |
| 1672 | Topanga, United States                        |        29.58 |
| 1673 | West Bountiful, United States                 |        29.58 |
| 1674 | Kosmonosy, Czechia                            |        29.58 |
| 1675 | Uherske Hradiste, Czechia                     |        29.58 |
| 1676 | Zlin, Czechia                                 |        29.58 |
| 1677 | Saint Laurent Du Var, France                  |        29.58 |
| 1678 | Gotsucho, Japan                               |        29.58 |
| 1679 | Honcho, Japan                                 |        29.58 |
| 1680 | Narutocho Mitsuishi, Japan                    |        29.58 |
| 1681 | Omaezaki, Japan                               |        29.58 |
| 1682 | Sakaiminato, Japan                            |        29.58 |
| 1683 | Faro, Portugal                                |        29.58 |
| 1684 | Brig Glis, Switzerland                        |        29.58 |
| 1685 | Siirt, Turkey                                 |        29.58 |
| 1686 | Brigham City, United States                   |        29.58 |
| 1687 | Highland Park, United States                  |        29.5  |
| 1688 | Lewistown, United States                      |        29.5  |
| 1689 | Provo, United States                          |        29.5  |
| 1690 | Frydlant, Czechia                             |        29.5  |
| 1691 | Jesenice, Czechia                             |        29.5  |
| 1692 | Tanvald, Czechia                              |        29.5  |
| 1693 | Grande Synthe, France                         |        29.5  |
| 1694 | Saint Raphael, France                         |        29.5  |
| 1695 | Udhampur, India                               |        29.5  |
| 1696 | Arao, Japan                                   |        29.5  |
| 1697 | Gyoda, Japan                                  |        29.5  |
| 1698 | Konosu, Japan                                 |        29.5  |
| 1699 | Narashino, Japan                              |        29.5  |
| 1700 | Niihama, Japan                                |        29.5  |
| 1701 | Edmond, United States                         |        29.5  |
| 1702 | Ban Suan, Thailand                            |        29.42 |
| 1703 | Franklin Township, United States              |        29.42 |
| 1704 | Havre, United States                          |        29.42 |
| 1705 | Perpignan, France                             |        29.42 |
| 1706 | Shakopee, United States                       |        29.42 |
| 1707 | Sharon, United States                         |        29.42 |
| 1708 | Simi Valley, United States                    |        29.42 |
| 1709 | Syracuse, United States                       |        29.42 |
| 1710 | Winthrop Harbor, United States                |        29.42 |
| 1711 | Higashi Osaka, Japan                          |        29.42 |
| 1712 | Shirayamamachi, Japan                         |        29.42 |
| 1713 | Bikin, Russia                                 |        29.33 |
| 1714 | Trat, Thailand                                |        29.33 |
| 1715 | Wencheng, China                               |        29.33 |
| 1716 | Arras, France                                 |        29.33 |
| 1717 | La Valette Du Var, France                     |        29.33 |
| 1718 | Lormont, France                               |        29.33 |
| 1719 | Salon De Provence, France                     |        29.33 |
| 1720 | Mandan, United States                         |        29.33 |
| 1721 | Gobo, Japan                                   |        29.33 |
| 1722 | Kosai, Japan                                  |        29.33 |
| 1723 | Zakopane, Poland                              |        29.25 |
| 1724 | Cintruenigo, Spain                            |        29.25 |
| 1725 | Blaine, United States                         |        29.25 |
| 1726 | Bohumin, Czechia                              |        29.25 |
| 1727 | Midvale, United States                        |        29.25 |
| 1728 | Santa Fe, United States                       |        29.25 |
| 1729 | Bolzano, Italy                                |        29.25 |
| 1730 | Abiko, Japan                                  |        29.25 |
| 1731 | Chiba, Japan                                  |        29.25 |
| 1732 | Fukata, Japan                                 |        29.25 |
| 1733 | Fukayacho, Japan                              |        29.25 |
| 1734 | Hakui, Japan                                  |        29.25 |
| 1735 | Higashi Matsuyama, Japan                      |        29.25 |
| 1736 | Ishikida, Japan                               |        29.25 |
| 1737 | Matsuzaka, Japan                              |        29.25 |
| 1738 | Sumiyama, Japan                               |        29.25 |
| 1739 | Gorzow Wielkopolski, Poland                   |        29.25 |
| 1740 | Inowroclaw, Poland                            |        29.25 |
| 1741 | Ljubljana, Slovenia                           |        29.17 |
| 1742 | Sevilla, Spain                                |        29.17 |
| 1743 | East York, United States                      |        29.17 |
| 1744 | Glenpool, United States                       |        29.17 |
| 1745 | Edmonton, Canada                              |        29.17 |
| 1746 | Slapanice, Czechia                            |        29.17 |
| 1747 | Gersfeld, Germany                             |        29.17 |
| 1748 | Porterville, United States                    |        29.17 |
| 1749 | Steelton, United States                       |        29.17 |
| 1750 | Kagoshima, Japan                              |        29.17 |
| 1751 | Kure, Japan                                   |        29.17 |
| 1752 | Nyuzen, Japan                                 |        29.17 |
| 1753 | Castro Marim, Portugal                        |        29.08 |
| 1754 | Marasesti, Romania                            |        29.08 |
| 1755 | Kosice, Slovakia                              |        29.08 |
| 1756 | Betong, Thailand                              |        29.08 |
| 1757 | Grossalmerode, Germany                        |        29.08 |
| 1758 | Murray, United States                         |        29.08 |
| 1759 | New Castle, United States                     |        29.08 |
| 1760 | Hayashima, Japan                              |        29.08 |
| 1761 | Honjo, Japan                                  |        29.08 |
| 1762 | Shimo Tsuma, Japan                            |        29.08 |
| 1763 | Yotsukaido, Japan                             |        29.08 |
| 1764 | Zentsujicho, Japan                            |        29.08 |
| 1765 | Oral, Kazakhstan                              |        29.08 |
| 1766 | Hat Yai, Thailand                             |        29    |
| 1767 | Manaus, Brazil                                |        29    |
| 1768 | Cold Lake, Canada                             |        29    |
| 1769 | Castres, France                               |        29    |
| 1770 | Prairieville, United States                   |        29    |
| 1771 | Ageoshimo, Japan                              |        29    |
| 1772 | Kakogawacho Honmachi, Japan                   |        29    |
| 1773 | Nagato, Japan                                 |        29    |
| 1774 | As Salt, Jordan                               |        29    |
| 1775 | Jerez De La Frontera, Spain                   |        28.92 |
| 1776 | Nymburk, Czechia                              |        28.92 |
| 1777 | Toulon, France                                |        28.92 |
| 1778 | Heppenheim, Germany                           |        28.92 |
| 1779 | Hobbs, United States                          |        28.92 |
| 1780 | Asti, Italy                                   |        28.92 |
| 1781 | Hikari, Japan                                 |        28.92 |
| 1782 | Nobeoka, Japan                                |        28.92 |
| 1783 | Saga, Japan                                   |        28.92 |
| 1784 | Dabrowa Gornicza, Poland                      |        28.92 |
| 1785 | Almeria, Spain                                |        28.83 |
| 1786 | Puigcerda, Spain                              |        28.83 |
| 1787 | Camp Pendleton South, United States           |        28.83 |
| 1788 | Hranice, Czechia                              |        28.83 |
| 1789 | Klasterec Nad Ohri, Czechia                   |        28.83 |
| 1790 | Liberec, Czechia                              |        28.83 |
| 1791 | Dunkerque, France                             |        28.83 |
| 1792 | Konigstein Im Taunus, Germany                 |        28.83 |
| 1793 | Tahlequah, United States                      |        28.83 |
| 1794 | Bandipura, India                              |        28.83 |
| 1795 | Atami, Japan                                  |        28.83 |
| 1796 | Chigasaki, Japan                              |        28.83 |
| 1797 | Izuo, Japan                                   |        28.83 |
| 1798 | Kasamatsucho, Japan                           |        28.83 |
| 1799 | Kobe, Japan                                   |        28.83 |
| 1800 | Komatsushimacho, Japan                        |        28.83 |
| 1801 | Osaka, Japan                                  |        28.83 |
| 1802 | Shimizucho, Japan                             |        28.83 |
| 1803 | Suzuka, Japan                                 |        28.83 |
| 1804 | Fushe Kosove, Kosovo                          |        28.83 |
| 1805 | Pabianice, Poland                             |        28.75 |
| 1806 | Piotrkow Trybunalski, Poland                  |        28.75 |
| 1807 | Almada, Portugal                              |        28.75 |
| 1808 | Golega, Portugal                              |        28.75 |
| 1809 | Camden, United States                         |        28.75 |
| 1810 | Colusa, United States                         |        28.75 |
| 1811 | Evansville, United States                     |        28.75 |
| 1812 | Green Valley, United States                   |        28.75 |
| 1813 | Roseville, United States                      |        28.75 |
| 1814 | St Matthews, United States                    |        28.75 |
| 1815 | Waukesha, United States                       |        28.75 |
| 1816 | Kamiichi, Japan                               |        28.75 |
| 1817 | Kumamoto, Japan                               |        28.75 |
| 1818 | Nogata, Japan                                 |        28.75 |
| 1819 | Biala Podlaska, Poland                        |        28.75 |
| 1820 | Palma, Spain                                  |        28.67 |
| 1821 | Valencia, Spain                               |        28.67 |
| 1822 | Wancheng, China                               |        28.67 |
| 1823 | Ceske Budejovice, Czechia                     |        28.67 |
| 1824 | Kraslice, Czechia                             |        28.67 |
| 1825 | Tournefeuille, France                         |        28.67 |
| 1826 | New Brighton, United States                   |        28.67 |
| 1827 | Tooele, United States                         |        28.67 |
| 1828 | Woodward, United States                       |        28.67 |
| 1829 | Gosen, Japan                                  |        28.67 |
| 1830 | Hikone, Japan                                 |        28.67 |
| 1831 | Isehara, Japan                                |        28.67 |
| 1832 | Kukichuo, Japan                               |        28.67 |
| 1833 | Oakashicho, Japan                             |        28.67 |
| 1834 | Tokushima, Japan                              |        28.67 |
| 1835 | Ube, Japan                                    |        28.67 |
| 1836 | Yao, Japan                                    |        28.67 |
| 1837 | Czestochowa, Poland                           |        28.67 |
| 1838 | Wroclaw, Poland                               |        28.58 |
| 1839 | Estarreja, Portugal                           |        28.58 |
| 1840 | Almonte, Spain                                |        28.58 |
| 1841 | Cadiz, Spain                                  |        28.58 |
| 1842 | Huelva, Spain                                 |        28.58 |
| 1843 | Villareal, Spain                              |        28.58 |
| 1844 | Nevsehir, Turkey                              |        28.58 |
| 1845 | Dimitrovgrad, Bulgaria                        |        28.58 |
| 1846 | Brno, Czechia                                 |        28.58 |
| 1847 | Bethune, France                               |        28.58 |
| 1848 | Saint Malo, France                            |        28.58 |
| 1849 | Springdale, United States                     |        28.58 |
| 1850 | Welby, United States                          |        28.58 |
| 1851 | Kashiwa, Japan                                |        28.58 |
| 1852 | Miyoshidai, Japan                             |        28.58 |
| 1853 | Saitama, Japan                                |        28.58 |
| 1854 | Satte, Japan                                  |        28.58 |
| 1855 | Tsurugashima, Japan                           |        28.58 |
| 1856 | Umi, Japan                                    |        28.58 |
| 1857 | Baton Rouge, United States                    |        28.5  |
| 1858 | Bishop, United States                         |        28.5  |
| 1859 | Vernon, Canada                                |        28.5  |
| 1860 | Henin Beaumont, France                        |        28.5  |
| 1861 | Martapura, Indonesia                          |        28.5  |
| 1862 | Furukawamen, Japan                            |        28.5  |
| 1863 | Morohongo, Japan                              |        28.5  |
| 1864 | Narita, Japan                                 |        28.5  |
| 1865 | Oita, Japan                                   |        28.5  |
| 1866 | Yokoshiba, Japan                              |        28.5  |
| 1867 | Amman, Jordan                                 |        28.5  |
| 1868 | Ikoma, Japan                                  |        28.42 |
| 1869 | Kamakurayama, Japan                           |        28.42 |
| 1870 | Kofu, Japan                                   |        28.42 |
| 1871 | Mito, Japan                                   |        28.42 |
| 1872 | Niigata, Japan                                |        28.42 |
| 1873 | Omura, Japan                                  |        28.42 |
| 1874 | Soja, Japan                                   |        28.42 |
| 1875 | Toyama, Japan                                 |        28.42 |
| 1876 | Bielsko Biala, Poland                         |        28.42 |
| 1877 | Maua, Brazil                                  |        28.42 |
| 1878 | Brevnov, Czechia                              |        28.42 |
| 1879 | Nantes, France                                |        28.42 |
| 1880 | Belgrade, Serbia                              |        28.42 |
| 1881 | Brits, South Africa                           |        28.42 |
| 1882 | Chester, United States                        |        28.42 |
| 1883 | Viet Tri, Vietnam                             |        28.42 |
| 1884 | Fujiidera, Japan                              |        28.33 |
| 1885 | Matsuyama, Japan                              |        28.33 |
| 1886 | Mukocho, Japan                                |        28.33 |
| 1887 | Takaharu, Japan                               |        28.33 |
| 1888 | Pavlodar, Kazakhstan                          |        28.33 |
| 1889 | Knjazevac, Serbia                             |        28.33 |
| 1890 | Zarnovica, Slovakia                           |        28.33 |
| 1891 | Van, Turkey                                   |        28.33 |
| 1892 | El Cajon, United States                       |        28.33 |
| 1893 | Kansas City, United States                    |        28.33 |
| 1894 | Shahin Shahr, Iran                            |        28.25 |
| 1895 | Hofu, Japan                                   |        28.25 |
| 1896 | Inzai, Japan                                  |        28.25 |
| 1897 | Katsuragi, Japan                              |        28.25 |
| 1898 | Kyoto, Japan                                  |        28.25 |
| 1899 | Moriyama, Japan                               |        28.25 |
| 1900 | Saikaicho Kobago, Japan                       |        28.25 |
| 1901 | Toba, Japan                                   |        28.25 |
| 1902 | Togitsu, Japan                                |        28.25 |
| 1903 | Tonosho, Japan                                |        28.25 |
| 1904 | Hlinsko, Czechia                              |        28.25 |
| 1905 | Otrokovice, Czechia                           |        28.25 |
| 1906 | Calais, France                                |        28.25 |
| 1907 | Trzemeszno, Poland                            |        28.25 |
| 1908 | Vigo, Spain                                   |        28.25 |
| 1909 | Kaufman, United States                        |        28.25 |
| 1910 | Lawton, United States                         |        28.25 |
| 1911 | North Middleton, United States                |        28.25 |
| 1912 | Santa Clarita, United States                  |        28.25 |
| 1913 | Channarayapatna, India                        |        28.17 |
| 1914 | Hagi, Japan                                   |        28.17 |
| 1915 | Higashi Hiroshima, Japan                      |        28.17 |
| 1916 | Kamagaya, Japan                               |        28.17 |
| 1917 | Kaneyama, Japan                               |        28.17 |
| 1918 | Kimitsu, Japan                                |        28.17 |
| 1919 | Kuwana, Japan                                 |        28.17 |
| 1920 | Takeocho Takeo, Japan                         |        28.17 |
| 1921 | Tomioka, Japan                                |        28.17 |
| 1922 | Gevgelija, Macedonia                          |        28.17 |
| 1923 | Gogolin, Poland                               |        28.17 |
| 1924 | Aracatuba, Brazil                             |        28.17 |
| 1925 | Guaratingueta, Brazil                         |        28.17 |
| 1926 | Kansk, Russia                                 |        28.17 |
| 1927 | Allen Park, United States                     |        28.17 |
| 1928 | Carlsbad, United States                       |        28.17 |
| 1929 | Conroe, United States                         |        28.17 |
| 1930 | Fargo, United States                          |        28.17 |
| 1931 | Galveston, United States                      |        28.17 |
| 1932 | Salt Lake City, United States                 |        28.17 |
| 1933 | Bando, Japan                                  |        28.08 |
| 1934 | Chichibu, Japan                               |        28.08 |
| 1935 | Hashima, Japan                                |        28.08 |
| 1936 | Kariya, Japan                                 |        28.08 |
| 1937 | Kawara, Japan                                 |        28.08 |
| 1938 | Oiso, Japan                                   |        28.08 |
| 1939 | Sayama, Japan                                 |        28.08 |
| 1940 | Shimotsucho Kominami, Japan                   |        28.08 |
| 1941 | Togane, Japan                                 |        28.08 |
| 1942 | Valasske Mezirici, Czechia                    |        28.08 |
| 1943 | Romans Sur Isere, France                      |        28.08 |
| 1944 | La Linea De La Concepcion, Spain              |        28.08 |
| 1945 | Zaragoza, Spain                               |        28.08 |
| 1946 | Burbank, United States                        |        28.08 |
| 1947 | Ventimiglia, Italy                            |        28    |
| 1948 | Hatsukaichi, Japan                            |        28    |
| 1949 | Kadogawa, Japan                               |        28    |
| 1950 | Kanazawa, Japan                               |        28    |
| 1951 | Misato, Japan                                 |        28    |
| 1952 | Neya, Japan                                   |        28    |
| 1953 | Nomimachi, Japan                              |        28    |
| 1954 | Yashima, Japan                                |        28    |
| 1955 | Hoogstraten, Belgium                          |        28    |
| 1956 | La Rochelle, France                           |        28    |
| 1957 | Mont Saint Martin, France                     |        28    |
| 1958 | Rodez, France                                 |        28    |
| 1959 | Lone Grove, United States                     |        28    |
| 1960 | Sheboygan, United States                      |        28    |
| 1961 | Nesher, Israel                                |        27.92 |
| 1962 | Niiza, Japan                                  |        27.92 |
| 1963 | Sakaki, Japan                                 |        27.92 |
| 1964 | Shinozaki, Japan                              |        27.92 |
| 1965 | Tainai, Japan                                 |        27.92 |
| 1966 | Takamori, Japan                               |        27.92 |
| 1967 | Sanya, China                                  |        27.92 |
| 1968 | Blois, France                                 |        27.92 |
| 1969 | Douai, France                                 |        27.92 |
| 1970 | Lorient, France                               |        27.92 |
| 1971 | Klerksdorp, South Africa                      |        27.92 |
| 1972 | Acton, United Kingdom                         |        27.92 |
| 1973 | Erwin, United States                          |        27.92 |
| 1974 | Kokomo, United States                         |        27.92 |
| 1975 | Madison, United States                        |        27.92 |
| 1976 | Somerset, United States                       |        27.92 |
| 1977 | Tracy, United States                          |        27.92 |
| 1978 | Watford City, United States                   |        27.92 |
| 1979 | Ashdod, Israel                                |        27.83 |
| 1980 | Gan Yavne, Israel                             |        27.83 |
| 1981 | Beppu, Japan                                  |        27.83 |
| 1982 | Hamamatsu, Japan                              |        27.83 |
| 1983 | Nagareyama, Japan                             |        27.83 |
| 1984 | Sakado, Japan                                 |        27.83 |
| 1985 | Shibukawa, Japan                              |        27.83 |
| 1986 | Ureshinomachi Shimojuku, Japan                |        27.83 |
| 1987 | Kaunas, Lithuania                             |        27.83 |
| 1988 | Panciu, Romania                               |        27.83 |
| 1989 | Ecija, Spain                                  |        27.83 |
| 1990 | Valldoreix, Spain                             |        27.83 |
| 1991 | Notre Dame, United States                     |        27.83 |
| 1992 | Queens, United States                         |        27.83 |
| 1993 | Hanno, Japan                                  |        27.75 |
| 1994 | Hidaka, Japan                                 |        27.75 |
| 1995 | Sakaidecho, Japan                             |        27.75 |
| 1996 | Sakata, Japan                                 |        27.75 |
| 1997 | Sakura, Japan                                 |        27.75 |
| 1998 | Sato, Japan                                   |        27.75 |
| 1999 | Yokkaichi, Japan                              |        27.75 |
| 2000 | Chepelare, Bulgaria                           |        27.75 |
| 2001 | Bluewater, Canada                             |        27.75 |
| 2002 | St Thomas, Canada                             |        27.75 |
| 2003 | Joue Les Tours, France                        |        27.75 |
| 2004 | Santana, Portugal                             |        27.75 |
| 2005 | Avila, Spain                                  |        27.75 |
| 2006 | Yilan, Taiwan                                 |        27.75 |
| 2007 | Thung Song, Thailand                          |        27.75 |
| 2008 | Bartlett, United States                       |        27.75 |
| 2009 | Hurricane, United States                      |        27.75 |
| 2010 | Seaford, United States                        |        27.75 |
| 2011 | Uniontown, United States                      |        27.75 |
| 2012 | Kakamigahara, Japan                           |        27.67 |
| 2013 | Kawagoe, Japan                                |        27.67 |
| 2014 | Kawaguchi, Japan                              |        27.67 |
| 2015 | Matsubushi, Japan                             |        27.67 |
| 2016 | Noshiromachi, Japan                           |        27.67 |
| 2017 | Omiyacho, Japan                               |        27.67 |
| 2018 | Uji, Japan                                    |        27.67 |
| 2019 | Obiliq, Kosovo                                |        27.67 |
| 2020 | Banff, Canada                                 |        27.67 |
| 2021 | London, Canada                                |        27.67 |
| 2022 | Oakville, Canada                              |        27.67 |
| 2023 | Saint Mande, France                           |        27.67 |
| 2024 | Beocin, Serbia                                |        27.67 |
| 2025 | Bethlehem, United States                      |        27.67 |
| 2026 | El Rio, United States                         |        27.67 |
| 2027 | Milton, United States                         |        27.67 |
| 2028 | Pocono, United States                         |        27.67 |
| 2029 | Shively, United States                        |        27.67 |
| 2030 | Jerusalem, Israel                             |        27.58 |
| 2031 | Higashiomi, Japan                             |        27.58 |
| 2032 | Himi, Japan                                   |        27.58 |
| 2033 | Joetsu, Japan                                 |        27.58 |
| 2034 | Kashiwara, Japan                              |        27.58 |
| 2035 | Miyazu, Japan                                 |        27.58 |
| 2036 | Omihachiman, Japan                            |        27.58 |
| 2037 | Shima, Japan                                  |        27.58 |
| 2038 | Tadaoka Higashi, Japan                        |        27.58 |
| 2039 | Tonami, Japan                                 |        27.58 |
| 2040 | Tsu, Japan                                    |        27.58 |
| 2041 | Yaizu, Japan                                  |        27.58 |
| 2042 | Yasugicho, Japan                              |        27.58 |
| 2043 | Plzen, Czechia                                |        27.58 |
| 2044 | Chateauroux, France                           |        27.58 |
| 2045 | Toulouse, France                              |        27.58 |
| 2046 | Leczyca, Poland                               |        27.58 |
| 2047 | Penamacor, Portugal                           |        27.58 |
| 2048 | Isparta, Turkey                               |        27.58 |
| 2049 | Coronado, United States                       |        27.58 |
| 2050 | Merced, United States                         |        27.58 |
| 2051 | Port Washington, United States                |        27.58 |
| 2052 | Kilkunda, India                               |        27.5  |
| 2053 | Savona, Italy                                 |        27.5  |
| 2054 | Futtsu, Japan                                 |        27.5  |
| 2055 | Isahaya, Japan                                |        27.5  |
| 2056 | Kamisu, Japan                                 |        27.5  |
| 2057 | Kashima, Japan                                |        27.5  |
| 2058 | Miyake Naka, Japan                            |        27.5  |
| 2059 | Nishinomiya Hama, Japan                       |        27.5  |
| 2060 | Takamatsu, Japan                              |        27.5  |
| 2061 | Yachiyo, Japan                                |        27.5  |
| 2062 | Sao Paulo, Brazil                             |        27.5  |
| 2063 | Blagnac, France                               |        27.5  |
| 2064 | Creil, France                                 |        27.5  |
| 2065 | Cottbus, Germany                              |        27.5  |
| 2066 | Boscombe, United Kingdom                      |        27.5  |
| 2067 | Alta Sierra, United States                    |        27.5  |
| 2068 | Corsicana, United States                      |        27.5  |
| 2069 | Eaton, United States                          |        27.5  |
| 2070 | Kalamazoo, United States                      |        27.5  |
| 2071 | St Louis, United States                       |        27.42 |
| 2072 | Willows, United States                        |        27.42 |
| 2073 | Campinas, Brazil                              |        27.42 |
| 2074 | Hostivice, Czechia                            |        27.42 |
| 2075 | Anglet, France                                |        27.42 |
| 2076 | Reims, France                                 |        27.42 |
| 2077 | Akita, Japan                                  |        27.42 |
| 2078 | Funato, Japan                                 |        27.42 |
| 2079 | Iwata, Japan                                  |        27.42 |
| 2080 | Kawaii, Japan                                 |        27.42 |
| 2081 | Nichinan, Japan                               |        27.42 |
| 2082 | Shinkai, Japan                                |        27.42 |
| 2083 | Darwin, Australia                             |        27.33 |
| 2084 | Marilia, Brazil                               |        27.33 |
| 2085 | Chatham, Canada                               |        27.33 |
| 2086 | Fougeres, France                              |        27.33 |
| 2087 | Rennes, France                                |        27.33 |
| 2088 | Vannes, France                                |        27.33 |
| 2089 | Frankfurt (Oder), Germany                     |        27.33 |
| 2090 | Oberviechtach, Germany                        |        27.33 |
| 2091 | Trier, Germany                                |        27.33 |
| 2092 | Ise, Japan                                    |        27.33 |
| 2093 | Itami, Japan                                  |        27.33 |
| 2094 | Kamo, Japan                                   |        27.33 |
| 2095 | Kisarazu, Japan                               |        27.33 |
| 2096 | Matsue, Japan                                 |        27.33 |
| 2097 | Shimomura, Japan                              |        27.33 |
| 2098 | Tahara, Japan                                 |        27.33 |
| 2099 | Toyohashi, Japan                              |        27.33 |
| 2100 | Tsukawaki, Japan                              |        27.33 |
| 2101 | Tsuruga, Japan                                |        27.33 |
| 2102 | Rostusa, Macedonia                            |        27.33 |
| 2103 | Walbrzych, Poland                             |        27.33 |
| 2104 | Leon, Spain                                   |        27.33 |
| 2105 | Logrono, Spain                                |        27.33 |
| 2106 | Surat Thani, Thailand                         |        27.33 |
| 2107 | Bayburt, Turkey                               |        27.33 |
| 2108 | St Joseph, United States                      |        27.25 |
| 2109 | Terre Haute, United States                    |        27.25 |
| 2110 | Wilmington, United States                     |        27.25 |
| 2111 | Guelph, Canada                                |        27.25 |
| 2112 | Cheb, Czechia                                 |        27.25 |
| 2113 | Olivet, France                                |        27.25 |
| 2114 | Chofugaoka, Japan                             |        27.25 |
| 2115 | Daitocho, Japan                               |        27.25 |
| 2116 | Hirao, Japan                                  |        27.25 |
| 2117 | Hiroshima, Japan                              |        27.25 |
| 2118 | Ichikawa, Japan                               |        27.25 |
| 2119 | Kawanishicho, Japan                           |        27.25 |
| 2120 | Machida, Japan                                |        27.25 |
| 2121 | Nagahama, Japan                               |        27.25 |
| 2122 | Oga, Japan                                    |        27.25 |
| 2123 | Otsu, Japan                                   |        27.25 |
| 2124 | Ozu, Japan                                    |        27.25 |
| 2125 | Shikama, Japan                                |        27.25 |
| 2126 | Suwa, Japan                                   |        27.25 |
| 2127 | Tsuchiura, Japan                              |        27.25 |
| 2128 | Bombarral, Portugal                           |        27.25 |
| 2129 | Presov, Slovakia                              |        27.25 |
| 2130 | Mahon, Spain                                  |        27.25 |
| 2131 | Valladolid, Spain                             |        27.25 |
| 2132 | Ordu, Turkey                                  |        27.25 |
| 2133 | Boothwyn, United States                       |        27.25 |
| 2134 | New Garden, United States                     |        27.17 |
| 2135 | Ross Township, United States                  |        27.17 |
| 2136 | Tecumseh, United States                       |        27.17 |
| 2137 | Roztoky, Czechia                              |        27.17 |
| 2138 | Amiens, France                                |        27.17 |
| 2139 | Angers, France                                |        27.17 |
| 2140 | Biarritz, France                              |        27.17 |
| 2141 | Cholet, France                                |        27.17 |
| 2142 | Schwarzenberg, Germany                        |        27.17 |
| 2143 | Holon, Israel                                 |        27.17 |
| 2144 | Hokota, Japan                                 |        27.17 |
| 2145 | Tanabe, Japan                                 |        27.17 |
| 2146 | Tsuruoka, Japan                               |        27.17 |
| 2147 | Zushi, Japan                                  |        27.17 |
| 2148 | Zary, Poland                                  |        27.17 |
| 2149 | Palos De La Frontera, Spain                   |        27.17 |
| 2150 | Ealing, United Kingdom                        |        27.17 |
| 2151 | Lacy Lakeview, United States                  |        27.08 |
| 2152 | Portage, United States                        |        27.08 |
| 2153 | Pelhrimov, Czechia                            |        27.08 |
| 2154 | Abbeville, France                             |        27.08 |
| 2155 | Ajaccio, France                               |        27.08 |
| 2156 | Nice, France                                  |        27.08 |
| 2157 | Biesenthal, Germany                           |        27.08 |
| 2158 | Khorramabad, Iran                             |        27.08 |
| 2159 | Higashi Murayama, Japan                       |        27.08 |
| 2160 | Higashiyamato, Japan                          |        27.08 |
| 2161 | Ichihara, Japan                               |        27.08 |
| 2162 | Ide, Japan                                    |        27.08 |
| 2163 | Kusatsu, Japan                                |        27.08 |
| 2164 | Nagano, Japan                                 |        27.08 |
| 2165 | Nanbei, Japan                                 |        27.08 |
| 2166 | Ogoshi, Japan                                 |        27.08 |
| 2167 | Takashima, Japan                              |        27.08 |
| 2168 | Salisbury, United States                      |        27    |
| 2169 | Dubrovnik, Croatia                            |        27    |
| 2170 | Albi, France                                  |        27    |
| 2171 | Le Mans, France                               |        27    |
| 2172 | Montpellier, France                           |        27    |
| 2173 | Brandenburg, Germany                          |        27    |
| 2174 | Gamagori, Japan                               |        27    |
| 2175 | Hashimoto, Japan                              |        27    |
| 2176 | Kaita, Japan                                  |        27    |
| 2177 | Kudamatsu, Japan                              |        27    |
| 2178 | Masuda, Japan                                 |        27    |
| 2179 | Mitai, Japan                                  |        27    |
| 2180 | Nagoya, Japan                                 |        27    |
| 2181 | Odacho Oda, Japan                             |        27    |
| 2182 | Tama, Japan                                   |        27    |
| 2183 | Tsubame, Japan                                |        27    |
| 2184 | Yokohama, Japan                               |        27    |
| 2185 | Yokotemachi, Japan                            |        27    |
| 2186 | Kocani, Macedonia                             |        27    |
| 2187 | Davao, Philippines                            |        27    |
| 2188 | Bals, Romania                                 |        27    |
| 2189 | Cisnadie, Romania                             |        27    |
| 2190 | Greendale, United States                      |        27    |
| 2191 | Raleigh, United States                        |        26.92 |
| 2192 | Valrico, United States                        |        26.92 |
| 2193 | Yuba City, United States                      |        26.92 |
| 2194 | Gorna Oryahovitsa, Bulgaria                   |        26.92 |
| 2195 | Shumen, Bulgaria                              |        26.92 |
| 2196 | Klatovy, Czechia                              |        26.92 |
| 2197 | Chartres, France                              |        26.92 |
| 2198 | Maubeuge, France                              |        26.92 |
| 2199 | Meyzieu, France                               |        26.92 |
| 2200 | Mulhouse, France                              |        26.92 |
| 2201 | Eibenstock, Germany                           |        26.92 |
| 2202 | Trochtelfingen, Germany                       |        26.92 |
| 2203 | Rehovot, Israel                               |        26.92 |
| 2204 | Iwakuni, Japan                                |        26.92 |
| 2205 | Toki, Japan                                   |        26.92 |
| 2206 | Tokorozawa, Japan                             |        26.92 |
| 2207 | Yakage, Japan                                 |        26.92 |
| 2208 | Yawata Shimizui, Japan                        |        26.92 |
| 2209 | Lugano, Switzerland                           |        26.92 |
| 2210 | Casper, United States                         |        26.92 |
| 2211 | Mcalester, United States                      |        26.83 |
| 2212 | Carapicuiba, Brazil                           |        26.83 |
| 2213 | Presidente Prudente, Brazil                   |        26.83 |
| 2214 | Le Creusot, France                            |        26.83 |
| 2215 | Villiers Le Bel, France                       |        26.83 |
| 2216 | Bexbach, Germany                              |        26.83 |
| 2217 | Eisenhuttenstadt, Germany                     |        26.83 |
| 2218 | Ludwigshafen, Germany                         |        26.83 |
| 2219 | Monschau, Germany                             |        26.83 |
| 2220 | Plon, Germany                                 |        26.83 |
| 2221 | Sonthofen, Germany                            |        26.83 |
| 2222 | Starnberg, Germany                            |        26.83 |
| 2223 | Zierenberg, Germany                           |        26.83 |
| 2224 | Tondabayashicho, Japan                        |        26.83 |
| 2225 | Toride, Japan                                 |        26.83 |
| 2226 | Zama, Japan                                   |        26.83 |
| 2227 | Warsaw, Poland                                |        26.83 |
| 2228 | Buftea, Romania                               |        26.83 |
| 2229 | Craiova, Romania                              |        26.83 |
| 2230 | Belleville, Canada                            |        26.75 |
| 2231 | Alencon, France                               |        26.75 |
| 2232 | Boulogne Sur Mer, France                      |        26.75 |
| 2233 | Pau, France                                   |        26.75 |
| 2234 | Izumo, Japan                                  |        26.75 |
| 2235 | Naganohara, Japan                             |        26.75 |
| 2236 | Waki, Japan                                   |        26.75 |
| 2237 | Alba Iulia, Romania                           |        26.75 |
| 2238 | Trang, Thailand                               |        26.75 |
| 2239 | Sheerness, United Kingdom                     |        26.75 |
| 2240 | Cedar Rapids, United States                   |        26.75 |
| 2241 | Jackson, United States                        |        26.67 |
| 2242 | Thibodaux, United States                      |        26.67 |
| 2243 | Waterloo, Canada                              |        26.67 |
| 2244 | Auxerre, France                               |        26.67 |
| 2245 | Bourges, France                               |        26.67 |
| 2246 | Montbeliard, France                           |        26.67 |
| 2247 | Lindenfels, Germany                           |        26.67 |
| 2248 | Aioi, Japan                                   |        26.67 |
| 2249 | Itoigawa, Japan                               |        26.67 |
| 2250 | Nago, Japan                                   |        26.67 |
| 2251 | Ogawa, Japan                                  |        26.67 |
| 2252 | Ouda Yamaguchi, Japan                         |        26.67 |
| 2253 | Saiki, Japan                                  |        26.67 |
| 2254 | Takahama, Japan                               |        26.67 |
| 2255 | Takasagocho Takasemachi, Japan                |        26.67 |
| 2256 | Yato, Japan                                   |        26.67 |
| 2257 | Kornik, Poland                                |        26.67 |
| 2258 | Bragadiru, Romania                            |        26.67 |
| 2259 | Kranj, Slovenia                               |        26.67 |
| 2260 | Porto Cristo, Spain                           |        26.67 |
| 2261 | Sabadell, Spain                               |        26.67 |
| 2262 | Clinton, United States                        |        26.67 |
| 2263 | Colville, United States                       |        26.67 |
| 2264 | Folsom, United States                         |        26.67 |
| 2265 | Northwest Harborcreek, United States          |        26.58 |
| 2266 | Port Huron, United States                     |        26.58 |
| 2267 | Taubate, Brazil                               |        26.58 |
| 2268 | Sokolov, Czechia                              |        26.58 |
| 2269 | Trebic, Czechia                               |        26.58 |
| 2270 | Copenhagen, Denmark                           |        26.58 |
| 2271 | Epernay, France                               |        26.58 |
| 2272 | Orleans, France                               |        26.58 |
| 2273 | Eberswalde, Germany                           |        26.58 |
| 2274 | Anjomachi, Japan                              |        26.58 |
| 2275 | Handa, Japan                                  |        26.58 |
| 2276 | Ishioka, Japan                                |        26.58 |
| 2277 | Mineshita, Japan                              |        26.58 |
| 2278 | Nango, Japan                                  |        26.58 |
| 2279 | Shibuya, Japan                                |        26.58 |
| 2280 | Tateyama, Japan                               |        26.58 |
| 2281 | Usuki, Japan                                  |        26.58 |
| 2282 | Yawatahama Shi, Japan                         |        26.58 |
| 2283 | Grevenmacher, Luxembourg                      |        26.58 |
| 2284 | Novi Sad, Serbia                              |        26.58 |
| 2285 | Algeciras, Spain                              |        26.58 |
| 2286 | Mugla, Turkey                                 |        26.58 |
| 2287 | Douglas, United States                        |        26.58 |
| 2288 | Leon Valley, United States                    |        26.5  |
| 2289 | Moline, United States                         |        26.5  |
| 2290 | Plovdiv, Bulgaria                             |        26.5  |
| 2291 | Brantford, Canada                             |        26.5  |
| 2292 | Hamilton, Canada                              |        26.5  |
| 2293 | Dole, France                                  |        26.5  |
| 2294 | Spremberg, Germany                            |        26.5  |
| 2295 | Kasugai, Japan                                |        26.5  |
| 2296 | Kokubunji, Japan                              |        26.5  |
| 2297 | Mihara, Japan                                 |        26.5  |
| 2298 | Nishiwaki, Japan                              |        26.5  |
| 2299 | Owariasahi, Japan                             |        26.5  |
| 2300 | Oyabe, Japan                                  |        26.5  |
| 2301 | Tsuyama, Japan                                |        26.5  |
| 2302 | Yurihonjo, Japan                              |        26.5  |
| 2303 | Mszczonow, Poland                             |        26.5  |
| 2304 | Zielona Gora, Poland                          |        26.5  |
| 2305 | Sacavem, Portugal                             |        26.5  |
| 2306 | Port Elizabeth, South Africa                  |        26.5  |
| 2307 | Onteniente, Spain                             |        26.5  |
| 2308 | Requena, Spain                                |        26.5  |
| 2309 | Singapore, Singapore                          |        26.42 |
| 2310 | Tsarevo, Bulgaria                             |        26.42 |
| 2311 | Monessen, United States                       |        26.42 |
| 2312 | Awara, Japan                                  |        26.42 |
| 2313 | Itoman, Japan                                 |        26.42 |
| 2314 | Kamirenjaku, Japan                            |        26.42 |
| 2315 | Kokawa, Japan                                 |        26.42 |
| 2316 | Maizuru, Japan                                |        26.42 |
| 2317 | Shimotoba, Japan                              |        26.42 |
| 2318 | Shimotoda, Japan                              |        26.42 |
| 2319 | Torihama, Japan                               |        26.42 |
| 2320 | Mangghystau, Kazakhstan                       |        26.42 |
| 2321 | Palmela, Portugal                             |        26.33 |
| 2322 | Phatthalung, Thailand                         |        26.33 |
| 2323 | Diyarbakir, Turkey                            |        26.33 |
| 2324 | Giresun, Turkey                               |        26.33 |
| 2325 | Cary, United States                           |        26.33 |
| 2326 | Newmarket, Canada                             |        26.33 |
| 2327 | St Catharines, Canada                         |        26.33 |
| 2328 | Sudbury, Canada                               |        26.33 |
| 2329 | La Roche Sur Yon, France                      |        26.33 |
| 2330 | Braunlage, Germany                            |        26.33 |
| 2331 | Itzehoe, Germany                              |        26.33 |
| 2332 | Netphen, Germany                              |        26.33 |
| 2333 | Jeffersontown, United States                  |        26.33 |
| 2334 | Marion, United States                         |        26.33 |
| 2335 | Normal, United States                         |        26.33 |
| 2336 | State College, United States                  |        26.33 |
| 2337 | Inabe, Japan                                  |        26.33 |
| 2338 | Kurayoshi, Japan                              |        26.33 |
| 2339 | Sandacho, Japan                               |        26.33 |
| 2340 | Shimogamo, Japan                              |        26.33 |
| 2341 | Minatitlan, Mexico                            |        26.33 |
| 2342 | Sakon Nakhon, Thailand                        |        26.25 |
| 2343 | Cankiri, Turkey                               |        26.25 |
| 2344 | Nottingham, United Kingdom                    |        26.25 |
| 2345 | Baraboo, United States                        |        26.25 |
| 2346 | Enoch, United States                          |        26.25 |
| 2347 | Chalons En Champagne, France                  |        26.25 |
| 2348 | Dreux, France                                 |        26.25 |
| 2349 | Saint Dizier, France                          |        26.25 |
| 2350 | Saint Quentin, France                         |        26.25 |
| 2351 | Milford, United States                        |        26.25 |
| 2352 | Savoy, United States                          |        26.25 |
| 2353 | Iruma, Japan                                  |        26.25 |
| 2354 | Kanzakimachi Kanzaki, Japan                   |        26.25 |
| 2355 | Sekimachi, Japan                              |        26.25 |
| 2356 | Takehara, Japan                               |        26.25 |
| 2357 | Wakayama, Japan                               |        26.25 |
| 2358 | Esch Sur Alzette, Luxembourg                  |        26.25 |
| 2359 | S Hertogenbosch, Netherlands                  |        26.25 |
| 2360 | Szczecin, Poland                              |        26.17 |
| 2361 | Marbella, Spain                               |        26.17 |
| 2362 | Sri Jayewardenepura Kotte, Sri Lanka          |        26.17 |
| 2363 | Hualien, Taiwan                               |        26.17 |
| 2364 | Novomoskovs'k, Ukraine                        |        26.17 |
| 2365 | Arnold, United States                         |        26.17 |
| 2366 | Chalon Sur Saone, France                      |        26.17 |
| 2367 | Cherbourg, France                             |        26.17 |
| 2368 | Forbach, France                               |        26.17 |
| 2369 | Lunel, France                                 |        26.17 |
| 2370 | Perigueux, France                             |        26.17 |
| 2371 | Jamestown, United States                      |        26.17 |
| 2372 | Koja, Japan                                   |        26.17 |
| 2373 | Minamiozuma, Japan                            |        26.17 |
| 2374 | Miyajima, Japan                               |        26.17 |
| 2375 | Obu, Japan                                    |        26.17 |
| 2376 | Ustron, Poland                                |        26.08 |
| 2377 | A Coruna, Spain                               |        26.08 |
| 2378 | Apollo Beach, United States                   |        26.08 |
| 2379 | Dickson City, United States                   |        26.08 |
| 2380 | Burlington, Canada                            |        26.08 |
| 2381 | Kincardine, Canada                            |        26.08 |
| 2382 | Thiais, France                                |        26.08 |
| 2383 | Burghausen, Germany                           |        26.08 |
| 2384 | Erkner, Germany                               |        26.08 |
| 2385 | Aki, Japan                                    |        26.08 |
| 2386 | Atsugicho, Japan                              |        26.08 |
| 2387 | Fukui, Japan                                  |        26.08 |
| 2388 | Ritto, Japan                                  |        26.08 |
| 2389 | Tajimi, Japan                                 |        26.08 |
| 2390 | Irbid, Jordan                                 |        26.08 |
| 2391 | Siedlce, Poland                               |        26    |
| 2392 | Barnaul, Russia                               |        26    |
| 2393 | Krasno nad Kysucou, Slovakia                  |        26    |
| 2394 | Lucenec, Slovakia                             |        26    |
| 2395 | La Baneza, Spain                              |        26    |
| 2396 | Diadema, Brazil                               |        26    |
| 2397 | Loyalist, Canada                              |        26    |
| 2398 | Znojmo, Czechia                               |        26    |
| 2399 | Lauenburg, Germany                            |        26    |
| 2400 | Luckenwalde, Germany                          |        26    |
| 2401 | Holland, United States                        |        26    |
| 2402 | Marshfield, United States                     |        26    |
| 2403 | Milltown, United States                       |        26    |
| 2404 | Vinh, Vietnam                                 |        26    |
| 2405 | Hitachiomiya, Japan                           |        26    |
| 2406 | Kobayashi, Japan                              |        26    |
| 2407 | Nisshin, Japan                                |        26    |
| 2408 | Suzukawa, Japan                               |        26    |
| 2409 | Taketoyo, Japan                               |        26    |
| 2410 | Tamuramachi Moriyama, Japan                   |        26    |
| 2411 | Phuket, Thailand                              |        25.92 |
| 2412 | Caerdydd, United Kingdom                      |        25.92 |
| 2413 | Brampton, Canada                              |        25.92 |
| 2414 | Cergy, France                                 |        25.92 |
| 2415 | Charleville Mezieres, France                  |        25.92 |
| 2416 | Kassel, Germany                               |        25.92 |
| 2417 | King City, United States                      |        25.92 |
| 2418 | Lawrence, United States                       |        25.92 |
| 2419 | Lawrenceville, United States                  |        25.92 |
| 2420 | Habikino, Japan                               |        25.92 |
| 2421 | Sagae, Japan                                  |        25.92 |
| 2422 | Tatsunocho Tominaga, Japan                    |        25.92 |
| 2423 | Grudziadz, Poland                             |        25.92 |
| 2424 | Apatin, Serbia                                |        25.83 |
| 2425 | Zamora, Spain                                 |        25.83 |
| 2426 | Kirsehir, Turkey                              |        25.83 |
| 2427 | Bristol, United Kingdom                       |        25.83 |
| 2428 | Sao Bernardo Do Campo, Brazil                 |        25.83 |
| 2429 | Windsor, Canada                               |        25.83 |
| 2430 | Coutances, France                             |        25.83 |
| 2431 | Etampes, France                               |        25.83 |
| 2432 | Lisieux, France                               |        25.83 |
| 2433 | Eichwalde, Germany                            |        25.83 |
| 2434 | Mittenwalde, Germany                          |        25.83 |
| 2435 | Plymouth Township, United States              |        25.83 |
| 2436 | Waldeck, Germany                              |        25.83 |
| 2437 | Ichinomiya, Japan                             |        25.83 |
| 2438 | Kanada, Japan                                 |        25.83 |
| 2439 | Minano, Japan                                 |        25.83 |
| 2440 | Shizuoka, Japan                               |        25.83 |
| 2441 | Wajimazakimachi, Japan                        |        25.83 |
| 2442 | Rize, Turkey                                  |        25.75 |
| 2443 | Sinop, Turkey                                 |        25.75 |
| 2444 | Gillingham, United Kingdom                    |        25.75 |
| 2445 | Villa Sarmiento, Argentina                    |        25.75 |
| 2446 | Dubrowna, Belarus                             |        25.75 |
| 2447 | Jau, Brazil                                   |        25.75 |
| 2448 | Tachov, Czechia                               |        25.75 |
| 2449 | Birkenfeld, Germany                           |        25.75 |
| 2450 | Winston Salem, United States                  |        25.75 |
| 2451 | Worms, Germany                                |        25.75 |
| 2452 | Aizawa, Japan                                 |        25.75 |
| 2453 | Iwaki, Japan                                  |        25.75 |
| 2454 | Minami Soma, Japan                            |        25.75 |
| 2455 | Mobara, Japan                                 |        25.75 |
| 2456 | Saku, Japan                                   |        25.75 |
| 2457 | Shirakawa, Japan                              |        25.75 |
| 2458 | Tokamachi, Japan                              |        25.75 |
| 2459 | Tsushima, Japan                               |        25.75 |
| 2460 | Aksay, Kazakhstan                             |        25.75 |
| 2461 | Polaniec, Poland                              |        25.67 |
| 2462 | Ruzomberok, Slovakia                          |        25.67 |
| 2463 | Madrid, Spain                                 |        25.67 |
| 2464 | Bellinzona, Switzerland                       |        25.67 |
| 2465 | Frostburg, United States                      |        25.67 |
| 2466 | Glenview, United States                       |        25.67 |
| 2467 | Smolyan, Bulgaria                             |        25.67 |
| 2468 | Hlucin, Czechia                               |        25.67 |
| 2469 | Bastia, France                                |        25.67 |
| 2470 | Caen, France                                  |        25.67 |
| 2471 | Lens, France                                  |        25.67 |
| 2472 | Poitiers, France                              |        25.67 |
| 2473 | Rambouillet, France                           |        25.67 |
| 2474 | Sotteville les Rouen, France                  |        25.67 |
| 2475 | Bautzen, Germany                              |        25.67 |
| 2476 | Schleswig, Germany                            |        25.67 |
| 2477 | Jericho, United States                        |        25.67 |
| 2478 | Halabjah, Iraq                                |        25.67 |
| 2479 | Kani, Japan                                   |        25.67 |
| 2480 | Kiyosu, Japan                                 |        25.67 |
| 2481 | Toyokawa, Japan                               |        25.67 |
| 2482 | Yamazaki, Japan                               |        25.67 |
| 2483 | Yonago, Japan                                 |        25.67 |
| 2484 | Castellon De La Plana, Spain                  |        25.58 |
| 2485 | Yeniceoba, Turkey                             |        25.58 |
| 2486 | Kirkstall, United Kingdom                     |        25.58 |
| 2487 | Valparaiso, Chile                             |        25.58 |
| 2488 | Jacinto City, United States                   |        25.58 |
| 2489 | Lynn, United States                           |        25.58 |
| 2490 | Raritan, United States                        |        25.58 |
| 2491 | Zittau, Germany                               |        25.58 |
| 2492 | Hadera, Israel                                |        25.58 |
| 2493 | Nakai, Japan                                  |        25.58 |
| 2494 | Sakurai, Japan                                |        25.58 |
| 2495 | Tsubata, Japan                                |        25.58 |
| 2496 | Lisbon, Portugal                              |        25.5  |
| 2497 | Badalona, Spain                               |        25.5  |
| 2498 | Peterborough, Canada                          |        25.5  |
| 2499 | Annweiler Am Trifels, Germany                 |        25.5  |
| 2500 | Borken, Germany                               |        25.5  |
| 2501 | Elsterwerda, Germany                          |        25.5  |
| 2502 | Konstanz, Germany                             |        25.5  |
| 2503 | Panthersville, United States                  |        25.5  |
| 2504 | Thousand Oaks, United States                  |        25.5  |
| 2505 | Vernal, United States                         |        25.5  |
| 2506 | Ware, United States                           |        25.5  |
| 2507 | Wilkes Barre, United States                   |        25.5  |
| 2508 | Tel Aviv Yafo, Israel                         |        25.5  |
| 2509 | Fukuyama, Japan                               |        25.5  |
| 2510 | Kitagata, Japan                               |        25.5  |
| 2511 | Naha, Japan                                   |        25.5  |
| 2512 | Nairobi, Kenya                                |        25.5  |
| 2513 | Daiwanishi, Japan                             |        25.42 |
| 2514 | Honmachi, Japan                               |        25.42 |
| 2515 | Inuyama, Japan                                |        25.42 |
| 2516 | Kose, Japan                                   |        25.42 |
| 2517 | Otaru, Japan                                  |        25.42 |
| 2518 | Tobe, Japan                                   |        25.42 |
| 2519 | Tokyo, Japan                                  |        25.42 |
| 2520 | Yachimata, Japan                              |        25.42 |
| 2521 | Yamaguchi, Japan                              |        25.42 |
| 2522 | Yashio, Japan                                 |        25.42 |
| 2523 | Groningen, Netherlands                        |        25.42 |
| 2524 | Sao Jose Dos Campos, Brazil                   |        25.42 |
| 2525 | Cornwall, Canada                              |        25.42 |
| 2526 | Auch, France                                  |        25.42 |
| 2527 | Dijon, France                                 |        25.42 |
| 2528 | Villeparisis, France                          |        25.42 |
| 2529 | Griesheim, Germany                            |        25.42 |
| 2530 | Norderney, Germany                            |        25.42 |
| 2531 | Radebeul, Germany                             |        25.42 |
| 2532 | Schwedt (Oder), Germany                       |        25.42 |
| 2533 | Plymouth, United Kingdom                      |        25.42 |
| 2534 | Floresville, United States                    |        25.42 |
| 2535 | Millville, United States                      |        25.42 |
| 2536 | Seekonk, United States                        |        25.42 |
| 2537 | Fuji, Japan                                   |        25.33 |
| 2538 | Fukuchiyama, Japan                            |        25.33 |
| 2539 | Ishikari, Japan                               |        25.33 |
| 2540 | Morioka, Japan                                |        25.33 |
| 2541 | Nishio, Japan                                 |        25.33 |
| 2542 | Yorii, Japan                                  |        25.33 |
| 2543 | Nesebar, Bulgaria                             |        25.33 |
| 2544 | Bourg En Bresse, France                       |        25.33 |
| 2545 | Goch, Germany                                 |        25.33 |
| 2546 | Nauen, Germany                                |        25.33 |
| 2547 | Steinheim Am Main, Germany                    |        25.33 |
| 2548 | Strausberg, Germany                           |        25.33 |
| 2549 | Cluj Napoca, Romania                          |        25.33 |
| 2550 | Pantelimon, Romania                           |        25.33 |
| 2551 | Martin, Slovakia                              |        25.33 |
| 2552 | Villena, Spain                                |        25.33 |
| 2553 | Alanya, Turkey                                |        25.33 |
| 2554 | Royal Leamington Spa, United Kingdom          |        25.33 |
| 2555 | Brockton, United States                       |        25.33 |
| 2556 | Steubenville, United States                   |        25.33 |
| 2557 | Gifu, Japan                                   |        25.25 |
| 2558 | Hitachi Naka, Japan                           |        25.25 |
| 2559 | Seto, Japan                                   |        25.25 |
| 2560 | Prague, Czechia                               |        25.25 |
| 2561 | Troyes, France                                |        25.25 |
| 2562 | Herzogenrath, Germany                         |        25.25 |
| 2563 | Limburg, Germany                              |        25.25 |
| 2564 | Neustadt An Der Donau, Germany                |        25.25 |
| 2565 | Torrelavega, Spain                            |        25.25 |
| 2566 | Thonex, Switzerland                           |        25.25 |
| 2567 | Chernivtsi, Ukraine                           |        25.25 |
| 2568 | Hilsea, United Kingdom                        |        25.25 |
| 2569 | Aldine, United States                         |        25.25 |
| 2570 | Johnstown, United States                      |        25.25 |
| 2571 | Kittanning, United States                     |        25.25 |
| 2572 | Rutland, United States                        |        25.25 |
| 2573 | Hitachi, Japan                                |        25.17 |
| 2574 | Ishii, Japan                                  |        25.17 |
| 2575 | Sasayama, Japan                               |        25.17 |
| 2576 | Caloocan City, Philippines                    |        25.17 |
| 2577 | Escaldes Engordany, Andorra                   |        25.17 |
| 2578 | Neuenburg Am Rhein, Germany                   |        25.17 |
| 2579 | Raunheim, Germany                             |        25.17 |
| 2580 | Zilina, Slovakia                              |        25.17 |
| 2581 | Cuevas Del Almanzora, Spain                   |        25.17 |
| 2582 | Molndal, Sweden                               |        25.17 |
| 2583 | Brixworth, United Kingdom                     |        25.17 |
| 2584 | Marshall, United States                       |        25.17 |
| 2585 | St Michael, United States                     |        25.17 |
| 2586 | Ypsilanti, United States                      |        25.17 |
| 2587 | Aizawl, India                                 |        25.08 |
| 2588 | Funagata, Japan                               |        25.08 |
| 2589 | Fussa, Japan                                  |        25.08 |
| 2590 | Ishigaki, Japan                               |        25.08 |
| 2591 | Kitaibaraki, Japan                            |        25.08 |
| 2592 | Naka, Japan                                   |        25.08 |
| 2593 | Naga City, Philippines                        |        25.08 |
| 2594 | Lloydminster, Canada                          |        25.08 |
| 2595 | Rokycany, Czechia                             |        25.08 |
| 2596 | Bourgoin Jallieu, France                      |        25.08 |
| 2597 | Evreux, France                                |        25.08 |
| 2598 | Lambeth, United Kingdom                       |        25.08 |
| 2599 | Greensboro, United States                     |        25.08 |
| 2600 | Seville, United States                        |        25.08 |
| 2601 | Kamitakeshi, Japan                            |        25    |
| 2602 | Kamiyoshida, Japan                            |        25    |
| 2603 | Kawanakajima, Japan                           |        25    |
| 2604 | Otsuki, Japan                                 |        25    |
| 2605 | Sabae, Japan                                  |        25    |
| 2606 | Toyooka, Japan                                |        25    |
| 2607 | Tsukumiura, Japan                             |        25    |
| 2608 | Cholpon Ata, Kyrgyzstan                       |        25    |
| 2609 | Dock Sur, Argentina                           |        25    |
| 2610 | Gardanne, France                              |        25    |
| 2611 | Lodz, Poland                                  |        25    |
| 2612 | Sines, Portugal                               |        25    |
| 2613 | Hwlffordd, United Kingdom                     |        25    |
| 2614 | Alsip, United States                          |        25    |
| 2615 | Brighton Township, United States              |        25    |
| 2616 | New London, United States                     |        25    |
| 2617 | Portsmouth, United States                     |        25    |
| 2618 | Santa Barbara, United States                  |        25    |
| 2619 | Ayabe, Japan                                  |        24.92 |
| 2620 | Kanie, Japan                                  |        24.92 |
| 2621 | Sukumo, Japan                                 |        24.92 |
| 2622 | Uwajima, Japan                                |        24.92 |
| 2623 | Klaipeda, Lithuania                           |        24.92 |
| 2624 | Sant Julia De Loria, Andorra                  |        24.92 |
| 2625 | Eeklo, Belgium                                |        24.92 |
| 2626 | Mississauga, Canada                           |        24.92 |
| 2627 | Smithers, Canada                              |        24.92 |
| 2628 | Saint Brieuc, France                          |        24.92 |
| 2629 | Vichy, France                                 |        24.92 |
| 2630 | Falkensee, Germany                            |        24.92 |
| 2631 | Kaiserslautern, Germany                       |        24.92 |
| 2632 | Athens, Greece                                |        24.83 |
| 2633 | Chiryu, Japan                                 |        24.83 |
| 2634 | Hamura, Japan                                 |        24.83 |
| 2635 | Tottori, Japan                                |        24.83 |
| 2636 | Les Mureaux, France                           |        24.83 |
| 2637 | Rillieux La Pape, France                      |        24.83 |
| 2638 | Freiburg Im Breisgau, Germany                 |        24.83 |
| 2639 | Greiz, Germany                                |        24.83 |
| 2640 | Munich, Germany                               |        24.83 |
| 2641 | Moncao, Portugal                              |        24.83 |
| 2642 | Somcuta Mare, Romania                         |        24.83 |
| 2643 | Lugo, Spain                                   |        24.83 |
| 2644 | Braidwood, United States                      |        24.83 |
| 2645 | East St Louis, United States                  |        24.83 |
| 2646 | Meridian, United States                       |        24.83 |
| 2647 | Nevada, United States                         |        24.83 |
| 2648 | North Elba, United States                     |        24.83 |
| 2649 | South Laurel, United States                   |        24.83 |
| 2650 | Wittenberge, Germany                          |        24.75 |
| 2651 | Inashiki, Japan                               |        24.75 |
| 2652 | Varna, Bulgaria                               |        24.75 |
| 2653 | Dax, France                                   |        24.75 |
| 2654 | Le Petit Quevilly, France                     |        24.75 |
| 2655 | Oyonnax, France                               |        24.75 |
| 2656 | Belzig, Germany                               |        24.75 |
| 2657 | Frankenthal, Germany                          |        24.75 |
| 2658 | Burriana, Spain                               |        24.75 |
| 2659 | Bronx, United States                          |        24.75 |
| 2660 | Columbus, United States                       |        24.75 |
| 2661 | De Witt, United States                        |        24.75 |
| 2662 | Findlay, United States                        |        24.75 |
| 2663 | Rochester, United States                      |        24.75 |
| 2664 | Hanamaki Onsen, Japan                         |        24.67 |
| 2665 | Kikugawa, Japan                               |        24.67 |
| 2666 | Kumano, Japan                                 |        24.67 |
| 2667 | Matsudo, Japan                                |        24.67 |
| 2668 | Nasushiobara, Japan                           |        24.67 |
| 2669 | Oshu, Japan                                   |        24.67 |
| 2670 | Sagamihara, Japan                             |        24.67 |
| 2671 | Tachikawa, Japan                              |        24.67 |
| 2672 | Maaseik, Belgium                              |        24.67 |
| 2673 | Sofia, Bulgaria                               |        24.67 |
| 2674 | Kuressaare, Estonia                           |        24.67 |
| 2675 | Echirolles, France                            |        24.67 |
| 2676 | Friedrichshafen, Germany                      |        24.67 |
| 2677 | Hurth, Germany                                |        24.67 |
| 2678 | Suceava, Romania                              |        24.67 |
| 2679 | Payerne, Switzerland                          |        24.67 |
| 2680 | Lome, Togo                                    |        24.67 |
| 2681 | Saltash, United Kingdom                       |        24.67 |
| 2682 | Cockeysville, United States                   |        24.67 |
| 2683 | Denton, United States                         |        24.67 |
| 2684 | Fillmore, United States                       |        24.67 |
| 2685 | Manhattan, United States                      |        24.67 |
| 2686 | Marana, United States                         |        24.67 |
| 2687 | Mount Ivy, United States                      |        24.67 |
| 2688 | Rancho Calaveras, United States               |        24.67 |
| 2689 | Yoshinaga, Japan                              |        24.58 |
| 2690 | Sorocaba, Brazil                              |        24.58 |
| 2691 | Barrie, Canada                                |        24.58 |
| 2692 | Toronto, Canada                               |        24.58 |
| 2693 | Torcy, France                                 |        24.58 |
| 2694 | Rastatt, Germany                              |        24.58 |
| 2695 | Pacos De Ferreira, Portugal                   |        24.58 |
| 2696 | Ourense, Spain                                |        24.58 |
| 2697 | Binningen, Switzerland                        |        24.58 |
| 2698 | Hernando, United States                       |        24.58 |
| 2699 | Manteca, United States                        |        24.58 |
| 2700 | Milwaukee, United States                      |        24.58 |
| 2701 | San Pablo, United States                      |        24.58 |
| 2702 | Sharonville, United States                    |        24.58 |
| 2703 | Hachioji, Japan                               |        24.5  |
| 2704 | Miyazaki, Japan                               |        24.5  |
| 2705 | Obama, Japan                                  |        24.5  |
| 2706 | Okazaki, Japan                                |        24.5  |
| 2707 | Ome, Japan                                    |        24.5  |
| 2708 | Luxembourg, Luxembourg                        |        24.5  |
| 2709 | Novo Selo, Macedonia                          |        24.5  |
| 2710 | Bayonne, France                               |        24.5  |
| 2711 | Metz, France                                  |        24.5  |
| 2712 | Aurich, Germany                               |        24.5  |
| 2713 | Hanau, Germany                                |        24.5  |
| 2714 | Kehl, Germany                                 |        24.5  |
| 2715 | Neuruppin, Germany                            |        24.5  |
| 2716 | Ilford, United Kingdom                        |        24.5  |
| 2717 | Wigan, United Kingdom                         |        24.5  |
| 2718 | York, United Kingdom                          |        24.5  |
| 2719 | Edgewood, United States                       |        24.5  |
| 2720 | Munhall, United States                        |        24.42 |
| 2721 | Redding, United States                        |        24.42 |
| 2722 | Woodland, United States                       |        24.42 |
| 2723 | North Bay, Canada                             |        24.42 |
| 2724 | Marseille, France                             |        24.42 |
| 2725 | Vandoeuvre Les Nancy, France                  |        24.42 |
| 2726 | Wiesbaden, Germany                            |        24.42 |
| 2727 | Wildau, Germany                               |        24.42 |
| 2728 | Maebashi, Japan                               |        24.42 |
| 2729 | Minokamo, Japan                               |        24.42 |
| 2730 | Murayama, Japan                               |        24.42 |
| 2731 | The Hague, Netherlands                        |        24.42 |
| 2732 | Kovacica, Serbia                              |        24.42 |
| 2733 | Ptuj, Slovenia                                |        24.42 |
| 2734 | Trbovlje, Slovenia                            |        24.42 |
| 2735 | Alicante, Spain                               |        24.42 |
| 2736 | Taitung, Taiwan                               |        24.42 |
| 2737 | Tunceli, Turkey                               |        24.42 |
| 2738 | Haverhill, United States                      |        24.42 |
| 2739 | St Cloud, United States                       |        24.33 |
| 2740 | Niort, France                                 |        24.33 |
| 2741 | Kempten, Germany                              |        24.33 |
| 2742 | Niesky, Germany                               |        24.33 |
| 2743 | Trostberg An Der Alz, Germany                 |        24.33 |
| 2744 | Wiesloch, Germany                             |        24.33 |
| 2745 | Aqtobe, Kazakhstan                            |        24.33 |
| 2746 | Halewood, United Kingdom                      |        24.33 |
| 2747 | Kingston Upon Hull, United Kingdom            |        24.33 |
| 2748 | Altoona, United States                        |        24.33 |
| 2749 | Estherville, United States                    |        24.33 |
| 2750 | White Plains, United States                   |        24.25 |
| 2751 | Fort Saskatchewan, Canada                     |        24.25 |
| 2752 | Parry Sound, Canada                           |        24.25 |
| 2753 | Jogeva, Estonia                               |        24.25 |
| 2754 | Darmstadt, Germany                            |        24.25 |
| 2755 | Mannheim, Germany                             |        24.25 |
| 2756 | Neuwied, Germany                              |        24.25 |
| 2757 | Oldenburg, Germany                            |        24.25 |
| 2758 | Wetzlar, Germany                              |        24.25 |
| 2759 | Ono, Japan                                    |        24.25 |
| 2760 | Chaves, Portugal                              |        24.25 |
| 2761 | Trebisov, Slovakia                            |        24.25 |
| 2762 | Barcelona, Spain                              |        24.25 |
| 2763 | Loyalsock, United States                      |        24.17 |
| 2764 | Rhinelander, United States                    |        24.17 |
| 2765 | Huntsville, Canada                            |        24.17 |
| 2766 | Bebra, Germany                                |        24.17 |
| 2767 | Leipzig, Germany                              |        24.17 |
| 2768 | Staufen Im Breisgau, Germany                  |        24.17 |
| 2769 | Nakanojomachi, Japan                          |        24.17 |
| 2770 | Brzozow, Poland                               |        24.17 |
| 2771 | Targu Jiu, Romania                            |        24.17 |
| 2772 | Hirnyk, Ukraine                               |        24.17 |
| 2773 | Blackpool, United Kingdom                     |        24.17 |
| 2774 | Caerphilly, United Kingdom                    |        24.17 |
| 2775 | Leigh On Sea, United Kingdom                  |        24.17 |
| 2776 | North Little Rock, United States              |        24.08 |
| 2777 | Saratoga, United States                       |        24.08 |
| 2778 | Tatui, Brazil                                 |        24.08 |
| 2779 | Montlucon, France                             |        24.08 |
| 2780 | Herrenberg, Germany                           |        24.08 |
| 2781 | Zeven, Germany                                |        24.08 |
| 2782 | Fukushima, Japan                              |        24.08 |
| 2783 | Ina, Japan                                    |        24.08 |
| 2784 | Sakai, Japan                                  |        24.08 |
| 2785 | Yonashiro Teruma, Japan                       |        24.08 |
| 2786 | Yunoshima, Japan                              |        24.08 |
| 2787 | Fort De France, Martinique                    |        24.08 |
| 2788 | Utrecht, Netherlands                          |        24.08 |
| 2789 | Santiago De Compostela, Spain                 |        24.08 |
| 2790 | Bern, Switzerland                             |        24.08 |
| 2791 | Frauenfeld, Switzerland                       |        24.08 |
| 2792 | East Grinstead, United Kingdom                |        24.08 |
| 2793 | Boston, United States                         |        24.08 |
| 2794 | Elizabethtown, United States                  |        24.08 |
| 2795 | Lexington, United States                      |        24    |
| 2796 | Lompoc, United States                         |        24    |
| 2797 | Aurillac, France                              |        24    |
| 2798 | Hohen Neuendorf, Germany                      |        24    |
| 2799 | Ulm, Germany                                  |        24    |
| 2800 | Worth Am Rhein, Germany                       |        24    |
| 2801 | Minamisuita, Japan                            |        24    |
| 2802 | Toyota, Japan                                 |        24    |
| 2803 | Wakabadai, Japan                              |        24    |
| 2804 | New Albany, United States                     |        23.92 |
| 2805 | Macon, France                                 |        23.92 |
| 2806 | Filderstadt, Germany                          |        23.92 |
| 2807 | Michelstadt, Germany                          |        23.92 |
| 2808 | Ebetsu, Japan                                 |        23.92 |
| 2809 | Nishi, Japan                                  |        23.92 |
| 2810 | Tateishi, Japan                               |        23.92 |
| 2811 | Rubi, Spain                                   |        23.92 |
| 2812 | Aiken, United States                          |        23.92 |
| 2813 | Augusta, United States                        |        23.92 |
| 2814 | Chelsea, United States                        |        23.92 |
| 2815 | Des Moines, United States                     |        23.92 |
| 2816 | Galloway, United States                       |        23.92 |
| 2817 | Richmond, Australia                           |        23.83 |
| 2818 | Dieppe, France                                |        23.83 |
| 2819 | Paris, France                                 |        23.83 |
| 2820 | Saint Martin d'Heres, France                  |        23.83 |
| 2821 | Ludwigsburg, Germany                          |        23.83 |
| 2822 | Prum, Germany                                 |        23.83 |
| 2823 | Reutlingen, Germany                           |        23.83 |
| 2824 | Soest, Germany                                |        23.83 |
| 2825 | Botosani, Romania                             |        23.83 |
| 2826 | Kostel, Slovenia                              |        23.83 |
| 2827 | Davos, Switzerland                            |        23.83 |
| 2828 | Sankt Gallen, Switzerland                     |        23.83 |
| 2829 | Afyonkarahisar, Turkey                        |        23.83 |
| 2830 | Appleton, United States                       |        23.83 |
| 2831 | Bennington, United States                     |        23.83 |
| 2832 | Carteret, United States                       |        23.83 |
| 2833 | Fairfield, United States                      |        23.83 |
| 2834 | Waxahachie, United States                     |        23.75 |
| 2835 | Nancy, France                                 |        23.75 |
| 2836 | Koblenz, Germany                              |        23.75 |
| 2837 | Furukawa, Japan                               |        23.75 |
| 2838 | Tafalla, Spain                                |        23.75 |
| 2839 | Elazig, Turkey                                |        23.75 |
| 2840 | Beaumont, United States                       |        23.75 |
| 2841 | Flint, United States                          |        23.75 |
| 2842 | Galena Park, United States                    |        23.75 |
| 2843 | River Rouge, United States                    |        23.67 |
| 2844 | Oshawa, Canada                                |        23.67 |
| 2845 | Brive La Gaillarde, France                    |        23.67 |
| 2846 | Gap, France                                   |        23.67 |
| 2847 | Fellbach, Germany                             |        23.67 |
| 2848 | Lampertheim, Germany                          |        23.67 |
| 2849 | Pirmasens, Germany                            |        23.67 |
| 2850 | Teltow, Germany                               |        23.67 |
| 2851 | Inazawa, Japan                                |        23.67 |
| 2852 | Voluntari, Romania                            |        23.67 |
| 2853 | Maribor, Slovenia                             |        23.67 |
| 2854 | Azpeitia, Spain                               |        23.67 |
| 2855 | Lausanne, Switzerland                         |        23.67 |
| 2856 | Andover, United Kingdom                       |        23.67 |
| 2857 | Rock Ferry, United Kingdom                    |        23.67 |
| 2858 | Avignon, France                               |        23.58 |
| 2859 | Marcq En Baroeul, France                      |        23.58 |
| 2860 | Montigny Les Metz, France                     |        23.58 |
| 2861 | Goslar, Germany                               |        23.58 |
| 2862 | Haselunne, Germany                            |        23.58 |
| 2863 | Heidelberg, Germany                           |        23.58 |
| 2864 | Tubingen, Germany                             |        23.58 |
| 2865 | Shinshiro, Japan                              |        23.58 |
| 2866 | Dearborn, United States                       |        23.58 |
| 2867 | Evergreen Park, United States                 |        23.58 |
| 2868 | Londonderry, United States                    |        23.5  |
| 2869 | Wilton, United States                         |        23.5  |
| 2870 | Medellin, Colombia                            |        23.5  |
| 2871 | Braunschweig, Germany                         |        23.5  |
| 2872 | Neu Zauche, Germany                           |        23.5  |
| 2873 | Ino, Japan                                    |        23.5  |
| 2874 | Bilgoraj, Poland                              |        23.5  |
| 2875 | Malbork, Poland                               |        23.5  |
| 2876 | Sibiu, Romania                                |        23.5  |
| 2877 | Senec, Slovakia                               |        23.5  |
| 2878 | Bandirma, Turkey                              |        23.5  |
| 2879 | Erfelek, Turkey                               |        23.5  |
| 2880 | Eccles, United Kingdom                        |        23.5  |
| 2881 | Gresham Park, United States                   |        23.5  |
| 2882 | Bucharest, Romania                            |        23.42 |
| 2883 | Puchov, Slovakia                              |        23.42 |
| 2884 | Dubendorf, Switzerland                        |        23.42 |
| 2885 | Sion, Switzerland                             |        23.42 |
| 2886 | Leeds, United Kingdom                         |        23.42 |
| 2887 | Newbold, United Kingdom                       |        23.42 |
| 2888 | Garden City, United States                    |        23.42 |
| 2889 | Geelong, Australia                            |        23.42 |
| 2890 | Blagoevgrad, Bulgaria                         |        23.42 |
| 2891 | Ottawa, Canada                                |        23.42 |
| 2892 | Hazebrouck, France                            |        23.42 |
| 2893 | Saint Etienne, France                         |        23.42 |
| 2894 | Schneverdingen, Germany                       |        23.42 |
| 2895 | Woodlake, United States                       |        23.42 |
| 2896 | Chita, Japan                                  |        23.42 |
| 2897 | Miyoshi, Japan                                |        23.42 |
| 2898 | Odate, Japan                                  |        23.42 |
| 2899 | Riehen, Switzerland                           |        23.33 |
| 2900 | Birmingham, United Kingdom                    |        23.33 |
| 2901 | Preston, United Kingdom                       |        23.33 |
| 2902 | Ryhope, United Kingdom                        |        23.33 |
| 2903 | Berkley, United States                        |        23.33 |
| 2904 | Dentsville, United States                     |        23.33 |
| 2905 | Yanchep, Australia                            |        23.33 |
| 2906 | Fulda, Germany                                |        23.33 |
| 2907 | Jerseyville, United States                    |        23.33 |
| 2908 | Volos, Greece                                 |        23.33 |
| 2909 | Haifa, Israel                                 |        23.33 |
| 2910 | Yamagata, Japan                               |        23.33 |
| 2911 | Portugalete, Spain                            |        23.25 |
| 2912 | Algiers, Algeria                              |        23.25 |
| 2913 | Chongshan, China                              |        23.25 |
| 2914 | Biberach, Germany                             |        23.25 |
| 2915 | Hannover, Germany                             |        23.25 |
| 2916 | Karlsruhe, Germany                            |        23.25 |
| 2917 | Kelsterbach, Germany                          |        23.25 |
| 2918 | Hollister, United States                      |        23.25 |
| 2919 | La Crosse, United States                      |        23.25 |
| 2920 | University Of California Davis, United States |        23.25 |
| 2921 | Wolfsburg, Germany                            |        23.25 |
| 2922 | Baramula, India                               |        23.25 |
| 2923 | Uchiko, Japan                                 |        23.25 |
| 2924 | Amsterdam, Netherlands                        |        23.25 |
| 2925 | Arnhem, Netherlands                           |        23.25 |
| 2926 | Trnava, Slovakia                              |        23.17 |
| 2927 | Bethal, South Africa                          |        23.17 |
| 2928 | Girona, Spain                                 |        23.17 |
| 2929 | Malmo, Sweden                                 |        23.17 |
| 2930 | Leicester, United Kingdom                     |        23.17 |
| 2931 | Norwich, United Kingdom                       |        23.17 |
| 2932 | Green Bay, United States                      |        23.17 |
| 2933 | Greenfield, United States                     |        23.17 |
| 2934 | Mandurah, Australia                           |        23.17 |
| 2935 | Dammarie Le Lys, France                       |        23.17 |
| 2936 | Melun, France                                 |        23.17 |
| 2937 | Nevers, France                                |        23.17 |
| 2938 | Strasbourg, France                            |        23.17 |
| 2939 | Villefranche Sur Saone, France                |        23.17 |
| 2940 | Annaberg Buchholz, Germany                    |        23.17 |
| 2941 | Dinslaken, Germany                            |        23.17 |
| 2942 | Frankfurt, Germany                            |        23.17 |
| 2943 | Obiraki, Japan                                |        23.17 |
| 2944 | Bislim Bajgora, Kosovo                        |        23.17 |
| 2945 | Maastricht, Netherlands                       |        23.17 |
| 2946 | Rotterdam, Netherlands                        |        23.17 |
| 2947 | Lomza, Poland                                 |        23.08 |
| 2948 | Halfway, United States                        |        23.08 |
| 2949 | Sainte Foy Les Lyon, France                   |        23.08 |
| 2950 | Schwerte, Germany                             |        23.08 |
| 2951 | Kearney, United States                        |        23.08 |
| 2952 | Livermore, United States                      |        23.08 |
| 2953 | Painesville, United States                    |        23.08 |
| 2954 | Iwashita, Japan                               |        23.08 |
| 2955 | Kadoma, Japan                                 |        23.08 |
| 2956 | Clifton, United Kingdom                       |        23    |
| 2957 | Clemmons, United States                       |        23    |
| 2958 | Giessen, Germany                              |        23    |
| 2959 | Schwabach, Germany                            |        23    |
| 2960 | Pasadena, United States                       |        23    |
| 2961 | Pascagoula, United States                     |        23    |
| 2962 | Red Bluff, United States                      |        23    |
| 2963 | Novaci Straini, Romania                       |        22.92 |
| 2964 | Castro Urdiales, Spain                        |        22.92 |
| 2965 | Cordoba, Spain                                |        22.92 |
| 2966 | Southampton, United Kingdom                   |        22.92 |
| 2967 | Chartiers, United States                      |        22.92 |
| 2968 | Red Deer, Canada                              |        22.92 |
| 2969 | Annemasse, France                             |        22.92 |
| 2970 | Marburg, Germany                              |        22.92 |
| 2971 | Monroe, United States                         |        22.92 |
| 2972 | Town N Country, United States                 |        22.92 |
| 2973 | Weissenthurm, Germany                         |        22.92 |
| 2974 | Takaoka, Japan                                |        22.92 |
| 2975 | Leeuwarden, Netherlands                       |        22.92 |
| 2976 | Funchal, Portugal                             |        22.83 |
| 2977 | Vranov nad Topl'ou, Slovakia                  |        22.83 |
| 2978 | Chur, Switzerland                             |        22.83 |
| 2979 | Burslem, United Kingdom                       |        22.83 |
| 2980 | Benton, United States                         |        22.83 |
| 2981 | Cadillac, United States                       |        22.83 |
| 2982 | Gulfport, United States                       |        22.83 |
| 2983 | Baden Baden, Germany                          |        22.83 |
| 2984 | Gottingen, Germany                            |        22.83 |
| 2985 | Seabrook, United States                       |        22.83 |
| 2986 | Miyako, Japan                                 |        22.83 |
| 2987 | Niimi, Japan                                  |        22.83 |
| 2988 | Taragi, Japan                                 |        22.83 |
| 2989 | Vaduz, Liechtenstein                          |        22.83 |
| 2990 | Sopot, Poland                                 |        22.75 |
| 2991 | Santander, Spain                              |        22.75 |
| 2992 | Zaporizhzhia, Ukraine                         |        22.75 |
| 2993 | Ashland, United States                        |        22.75 |
| 2994 | Badger, United States                         |        22.75 |
| 2995 | Fullerton, United States                      |        22.75 |
| 2996 | Rouen, France                                 |        22.75 |
| 2997 | Mount Pleasant, United States                 |        22.75 |
| 2998 | Salinas, United States                        |        22.75 |
| 2999 | Villingen Schwenningen, Germany               |        22.75 |
| 3000 | Wilhelmshaven, Germany                        |        22.75 |
| 3001 | Chitila, Romania                              |        22.67 |
| 3002 | Senica, Slovakia                              |        22.67 |
| 3003 | Donostia, Spain                               |        22.67 |
| 3004 | Wrecsam, United Kingdom                       |        22.67 |
| 3005 | Belton, United States                         |        22.67 |
| 3006 | Detroit Lakes, United States                  |        22.67 |
| 3007 | Durham, United States                         |        22.67 |
| 3008 | Newcastle, Australia                          |        22.67 |
| 3009 | Tamworth, Australia                           |        22.67 |
| 3010 | Wollongong, Australia                         |        22.67 |
| 3011 | Achim, Germany                                |        22.67 |
| 3012 | Heilbronn, Germany                            |        22.67 |
| 3013 | Osnabruck, Germany                            |        22.67 |
| 3014 | Bor, Serbia                                   |        22.58 |
| 3015 | Hnusta, Slovakia                              |        22.58 |
| 3016 | Interlaken, Switzerland                       |        22.58 |
| 3017 | Coventry, United Kingdom                      |        22.58 |
| 3018 | Leyton, United Kingdom                        |        22.58 |
| 3019 | Penicuik, United Kingdom                      |        22.58 |
| 3020 | Sheffield, United Kingdom                     |        22.58 |
| 3021 | Vratsa, Bulgaria                              |        22.58 |
| 3022 | Castlegar, Canada                             |        22.58 |
| 3023 | Kohtla Jarve, Estonia                         |        22.58 |
| 3024 | Antibes, France                               |        22.58 |
| 3025 | Aalen, Germany                                |        22.58 |
| 3026 | Luchow, Germany                               |        22.58 |
| 3027 | Sulzbach Rosenberg, Germany                   |        22.58 |
| 3028 | Montgomery, United States                     |        22.58 |
| 3029 | Wolfenbuttel, Germany                         |        22.58 |
| 3030 | Velky Meder, Slovakia                         |        22.5  |
| 3031 | Warrington, United Kingdom                    |        22.5  |
| 3032 | Yarm, United Kingdom                          |        22.5  |
| 3033 | Sillamae, Estonia                             |        22.5  |
| 3034 | Mendota, United States                        |        22.5  |
| 3035 | Oceano, United States                         |        22.5  |
| 3036 | Lang Son, Vietnam                             |        22.5  |
| 3037 | Nishihara, Japan                              |        22.42 |
| 3038 | Zwolle, Netherlands                           |        22.42 |
| 3039 | Saint John, Canada                            |        22.42 |
| 3040 | Tocopilla, Chile                              |        22.42 |
| 3041 | Helsinki, Finland                             |        22.42 |
| 3042 | Besancon, France                              |        22.42 |
| 3043 | Valence, France                               |        22.42 |
| 3044 | Voiron, France                                |        22.42 |
| 3045 | Gifhorn, Germany                              |        22.42 |
| 3046 | Herdorf, Germany                              |        22.42 |
| 3047 | Senta, Serbia                                 |        22.42 |
| 3048 | Titel, Serbia                                 |        22.42 |
| 3049 | Catford, United Kingdom                       |        22.42 |
| 3050 | Aspen Hill, United States                     |        22.42 |
| 3051 | Casas Adobes, United States                   |        22.42 |
| 3052 | Smyrna, United States                         |        22.42 |
| 3053 | Taboao Da Serra, Brazil                       |        22.33 |
| 3054 | Kameno, Bulgaria                              |        22.33 |
| 3055 | Kamloops, Canada                              |        22.33 |
| 3056 | Pula, Croatia                                 |        22.33 |
| 3057 | Epinal, France                                |        22.33 |
| 3058 | Focsani, Romania                              |        22.33 |
| 3059 | Indija, Serbia                                |        22.33 |
| 3060 | Bardejov, Slovakia                            |        22.33 |
| 3061 | Vitoria Gasteiz, Spain                        |        22.33 |
| 3062 | Cheraw, United States                         |        22.33 |
| 3063 | Hendersonville, United States                 |        22.33 |
| 3064 | Accra, Ghana                                  |        22.25 |
| 3065 | Roanne, France                                |        22.25 |
| 3066 | Pulheim, Germany                              |        22.25 |
| 3067 | Anderson, United States                       |        22.25 |
| 3068 | Cincinnati, United States                     |        22.25 |
| 3069 | Waveland, United States                       |        22.25 |
| 3070 | Izu, Japan                                    |        22.17 |
| 3071 | Kamaishi, Japan                               |        22.17 |
| 3072 | Jaral Del Progreso, Mexico                    |        22.17 |
| 3073 | Eindhoven, Netherlands                        |        22.17 |
| 3074 | Hamar, Norway                                 |        22.17 |
| 3075 | Tartu, Estonia                                |        22.17 |
| 3076 | Norderstedt, Germany                          |        22.17 |
| 3077 | Kragujevac, Serbia                            |        22.17 |
| 3078 | Belfast, United Kingdom                       |        22.17 |
| 3079 | Landore, United Kingdom                       |        22.17 |
| 3080 | Brainerd, United States                       |        22.17 |
| 3081 | North Adams, United States                    |        22.17 |
| 3082 | West Greenwich, United States                 |        22.17 |
| 3083 | Meadow Lake, Canada                           |        22.08 |
| 3084 | Lunen, Germany                                |        22.08 |
| 3085 | Tauberbischofsheim, Germany                   |        22.08 |
| 3086 | Rasnov, Romania                               |        22.08 |
| 3087 | Kropyvnytskyi, Ukraine                        |        22.08 |
| 3088 | Austin, United States                         |        22.08 |
| 3089 | Ojai, United States                           |        22.08 |
| 3090 | Kilkenny, Ireland                             |        22    |
| 3091 | Muswellbrook, Australia                       |        22    |
| 3092 | Narva, Estonia                                |        22    |
| 3093 | Omsk, Russia                                  |        22    |
| 3094 | Banska Bystrica, Slovakia                     |        22    |
| 3095 | Robinson, United States                       |        22    |
| 3096 | Wesel, Germany                                |        21.92 |
| 3097 | St Albert, Canada                             |        21.92 |
| 3098 | Tarbes, France                                |        21.92 |
| 3099 | Leinefelde, Germany                           |        21.92 |
| 3100 | Sulphur, United States                        |        21.92 |
| 3101 | Vreden, Germany                               |        21.83 |
| 3102 | Jisr Ez Zarqa, Israel                         |        21.83 |
| 3103 | Jaroslaw, Poland                              |        21.83 |
| 3104 | Leibnitz, Austria                             |        21.83 |
| 3105 | Brest, Belarus                                |        21.83 |
| 3106 | Essen, Belgium                                |        21.83 |
| 3107 | Rijeka, Croatia                               |        21.83 |
| 3108 | Kiel, Germany                                 |        21.83 |
| 3109 | Komarno, Slovakia                             |        21.83 |
| 3110 | Tarragona, Spain                              |        21.83 |
| 3111 | Dollis Hill, United Kingdom                   |        21.83 |
| 3112 | Gateshead, United Kingdom                     |        21.83 |
| 3113 | Lisburn, United Kingdom                       |        21.83 |
| 3114 | Kirby, United States                          |        21.83 |
| 3115 | Murraysville, United States                   |        21.83 |
| 3116 | Rietavas, Lithuania                           |        21.75 |
| 3117 | Haarlem, Netherlands                          |        21.75 |
| 3118 | Trujillo, Peru                                |        21.75 |
| 3119 | Edson, Canada                                 |        21.75 |
| 3120 | Nettetal, Germany                             |        21.75 |
| 3121 | Miedzyrzecz, Poland                           |        21.75 |
| 3122 | Durban, South Africa                          |        21.75 |
| 3123 | Keene, United States                          |        21.75 |
| 3124 | Tampa, United States                          |        21.75 |
| 3125 | Warr Acres, United States                     |        21.75 |
| 3126 | Fremantle, Australia                          |        21.67 |
| 3127 | Wolfsberg, Austria                            |        21.67 |
| 3128 | Bauru, Brazil                                 |        21.67 |
| 3129 | Haren, Germany                                |        21.67 |
| 3130 | Bishopbriggs, United Kingdom                  |        21.67 |
| 3131 | Culcheth, United Kingdom                      |        21.67 |
| 3132 | Middlesbrough, United Kingdom                 |        21.67 |
| 3133 | Missoula, United States                       |        21.67 |
| 3134 | Speedway, United States                       |        21.67 |
| 3135 | Yulee, United States                          |        21.67 |
| 3136 | Williams Lake, Canada                         |        21.58 |
| 3137 | Pantin, France                                |        21.58 |
| 3138 | Pforzheim, Germany                            |        21.58 |
| 3139 | Schweinfurt, Germany                          |        21.58 |
| 3140 | Volokolamsk, Russia                           |        21.58 |
| 3141 | Manchester, United Kingdom                    |        21.58 |
| 3142 | Stockton On Tees, United Kingdom              |        21.58 |
| 3143 | Jacksonville Beach, United States             |        21.58 |
| 3144 | Palatka, United States                        |        21.58 |
| 3145 | Ponca City, United States                     |        21.58 |
| 3146 | Red Oak, United States                        |        21.58 |
| 3147 | Ratingen, Germany                             |        21.5  |
| 3148 | Oftringen, Switzerland                        |        21.5  |
| 3149 | Reading, United Kingdom                       |        21.5  |
| 3150 | Bowling Green, United States                  |        21.5  |
| 3151 | Greenville, United States                     |        21.5  |
| 3152 | Homestead, United States                      |        21.5  |
| 3153 | North Fair Oaks, United States                |        21.42 |
| 3154 | Mahalapye, Botswana                           |        21.42 |
| 3155 | Dassel, Germany                               |        21.42 |
| 3156 | Cabuyao, Philippines                          |        21.42 |
| 3157 | Gdansk, Poland                                |        21.42 |
| 3158 | Zvolen, Slovakia                              |        21.42 |
| 3159 | Charleston, United States                     |        21.42 |
| 3160 | Louisville, United States                     |        21.33 |
| 3161 | Mckinleyville, United States                  |        21.33 |
| 3162 | Yakima, United States                         |        21.33 |
| 3163 | Oullins, France                               |        21.33 |
| 3164 | Suhareke, Kosovo                              |        21.33 |
| 3165 | Smederevo, Serbia                             |        21.33 |
| 3166 | Malacky, Slovakia                             |        21.33 |
| 3167 | Cedar Park, United States                     |        21.33 |
| 3168 | Quakers Hill, Australia                       |        21.25 |
| 3169 | Tahmoor, Australia                            |        21.25 |
| 3170 | Annecy, France                                |        21.25 |
| 3171 | Grenoble, France                              |        21.25 |
| 3172 | Shiraz, Iran                                  |        21.25 |
| 3173 | Bytow, Poland                                 |        21.25 |
| 3174 | Eibar, Spain                                  |        21.25 |
| 3175 | Fort Lee, United States                       |        21.25 |
| 3176 | Muldrow, United States                        |        21.17 |
| 3177 | Polson, United States                         |        21.17 |
| 3178 | Cooranbong, Australia                         |        21.17 |
| 3179 | Orange, Australia                             |        21.17 |
| 3180 | Saint Etienne Du Rouvray, France              |        21.17 |
| 3181 | Biella, Italy                                 |        21.17 |
| 3182 | Naples, Italy                                 |        21.17 |
| 3183 | Sapporo, Japan                                |        21.17 |
| 3184 | Otopeni, Romania                              |        21.17 |
| 3185 | Bassersdorf, Switzerland                      |        21.17 |
| 3186 | Dent, United States                           |        21.17 |
| 3187 | Ironton, United States                        |        21.08 |
| 3188 | Mcdonough, United States                      |        21.08 |
| 3189 | Mead, United States                           |        21.08 |
| 3190 | Sandpoint, United States                      |        21.08 |
| 3191 | Zadar, Croatia                                |        21.08 |
| 3192 | Roubaix, France                               |        21.08 |
| 3193 | Holzminden, Germany                           |        21.08 |
| 3194 | Samarinda, Indonesia                          |        21.08 |
| 3195 | Laguna De Duero, Spain                        |        21.08 |
| 3196 | Drayton Valley, Canada                        |        21    |
| 3197 | Saguenay, Canada                              |        21    |
| 3198 | Kralupy Nad Vltavou, Czechia                  |        21    |
| 3199 | Esbjerg, Denmark                              |        21    |
| 3200 | Chamonix Mont Blanc, France                   |        21    |
| 3201 | Martigues, France                             |        21    |
| 3202 | Stuttgart, Germany                            |        21    |
| 3203 | Hrastnik, Slovenia                            |        21    |
| 3204 | Edinburgh, United Kingdom                     |        21    |
| 3205 | East Rancho Dominguez, United States          |        21    |
| 3206 | Lebanon, United States                        |        20.92 |
| 3207 | Miami, United States                          |        20.92 |
| 3208 | Fieni, Romania                                |        20.92 |
| 3209 | Timisoara, Romania                            |        20.92 |
| 3210 | Bratislava, Slovakia                          |        20.92 |
| 3211 | Liptovsky Hradok, Slovakia                    |        20.92 |
| 3212 | Trencin, Slovakia                             |        20.92 |
| 3213 | Emeryville, United States                     |        20.92 |
| 3214 | Rouyn Noranda, Canada                         |        20.83 |
| 3215 | Labin, Croatia                                |        20.83 |
| 3216 | Dresden, Germany                              |        20.83 |
| 3217 | Guanajuato, Mexico                            |        20.83 |
| 3218 | Bacau, Romania                                |        20.83 |
| 3219 | Partizanske, Slovakia                         |        20.83 |
| 3220 | Malaga, Spain                                 |        20.83 |
| 3221 | Tarboro, United States                        |        20.75 |
| 3222 | Quebec City, Canada                           |        20.75 |
| 3223 | Gliwice, Poland                               |        20.75 |
| 3224 | Prievidza, Slovakia                           |        20.75 |
| 3225 | Bilbao, Spain                                 |        20.75 |
| 3226 | Hua Hin, Thailand                             |        20.75 |
| 3227 | Glasgow, United Kingdom                       |        20.75 |
| 3228 | Decatur, United States                        |        20.75 |
| 3229 | Helena Valley West Central, United States     |        20.75 |
| 3230 | Slatina, Romania                              |        20.67 |
| 3231 | Dunajska Streda, Slovakia                     |        20.67 |
| 3232 | Hamina, Finland                               |        20.58 |
| 3233 | Chambery, France                              |        20.58 |
| 3234 | Monaco, Monaco                                |        20.58 |
| 3235 | Poprad, Slovakia                              |        20.58 |
| 3236 | Cambuslang, United Kingdom                    |        20.58 |
| 3237 | Steyning, United Kingdom                      |        20.58 |
| 3238 | Midway, United States                         |        20.5  |
| 3239 | Minneapolis, United States                    |        20.5  |
| 3240 | South Houston, United States                  |        20.5  |
| 3241 | Stony Plain, Canada                           |        20.5  |
| 3242 | Thunder Bay, Canada                           |        20.5  |
| 3243 | Bordeaux, France                              |        20.5  |
| 3244 | Montelimar, France                            |        20.5  |
| 3245 | Ludenscheid, Germany                          |        20.5  |
| 3246 | Popesti Leordeni, Romania                     |        20.5  |
| 3247 | Liptovsky Mikulas, Slovakia                   |        20.5  |
| 3248 | Rutherglen, United Kingdom                    |        20.5  |
| 3249 | Grants Pass, United States                    |        20.42 |
| 3250 | Hazard, United States                         |        20.42 |
| 3251 | Mcminns Lagoon, Australia                     |        20.42 |
| 3252 | Lile Perrot, Canada                           |        20.42 |
| 3253 | Mont Royal, Canada                            |        20.42 |
| 3254 | Straelen, Germany                             |        20.42 |
| 3255 | Nipomo, United States                         |        20.42 |
| 3256 | Upper Mount Bethel, United States             |        20.42 |
| 3257 | Soka, Japan                                   |        20.42 |
| 3258 | Antrim, United Kingdom                        |        20.33 |
| 3259 | Singleton, Australia                          |        20.33 |
| 3260 | Berlin, Germany                               |        20.33 |
| 3261 | Mainz, Germany                                |        20.33 |
| 3262 | Sampit, Indonesia                             |        20.33 |
| 3263 | Skien, Norway                                 |        20.33 |
| 3264 | Highgate, United Kingdom                      |        20.25 |
| 3265 | Cold Springs, United States                   |        20.25 |
| 3266 | Sao Jose Do Rio Preto, Brazil                 |        20.25 |
| 3267 | Calgary, Canada                               |        20.25 |
| 3268 | Espoo, Finland                                |        20.25 |
| 3269 | Vienne, France                                |        20.25 |
| 3270 | Monrovia, Liberia                             |        20.25 |
| 3271 | Plumstead, United Kingdom                     |        20.17 |
| 3272 | Gilroy, United States                         |        20.17 |
| 3273 | Campbelltown, Australia                       |        20.17 |
| 3274 | Charlemagne, Canada                           |        20.17 |
| 3275 | Mercer Island, United States                  |        20.17 |
| 3276 | Ridgecrest, United States                     |        20.17 |
| 3277 | Vacaville, United States                      |        20.17 |
| 3278 | Durlesti, Moldova                             |        20.17 |
| 3279 | Pontevedra, Spain                             |        20.08 |
| 3280 | Holywood, United Kingdom                      |        20.08 |
| 3281 | Worsley, United Kingdom                       |        20.08 |
| 3282 | Butte, United States                          |        20.08 |
| 3283 | Escanaba, United States                       |        20.08 |
| 3284 | Fairbanks, United States                      |        20.08 |
| 3285 | Greensburg, United States                     |        20.08 |
| 3286 | Sliven, Bulgaria                              |        20.08 |
| 3287 | Brossard, Canada                              |        20.08 |
| 3288 | Coquimbo, Chile                               |        20.08 |
| 3289 | Elsdorf, Germany                              |        20.08 |
| 3290 | Hattingen, Germany                            |        20.08 |
| 3291 | Zrenjanin, Serbia                             |        20    |
| 3292 | Uzhhorod, Ukraine                             |        20    |
| 3293 | Gunnedah, Australia                           |        20    |
| 3294 | Trois Rivieres, Canada                        |        20    |
| 3295 | Sayre, United States                          |        20    |
| 3296 | Budennovsk, Russia                            |        19.92 |
| 3297 | Nitra, Slovakia                               |        19.92 |
| 3298 | Ashburn, United States                        |        19.92 |
| 3299 | Contra Costa Centre, United States            |        19.92 |
| 3300 | Thionville, France                            |        19.92 |
| 3301 | Lubeck, Germany                               |        19.92 |
| 3302 | Potsdam, Germany                              |        19.92 |
| 3303 | Artvin, Turkey                                |        19.83 |
| 3304 | Boulder, United States                        |        19.83 |
| 3305 | Ferry Pass, United States                     |        19.83 |
| 3306 | Dandenong, Australia                          |        19.83 |
| 3307 | Koflach, Austria                              |        19.83 |
| 3308 | Kardzhali, Bulgaria                           |        19.83 |
| 3309 | Tallinn, Estonia                              |        19.83 |
| 3310 | Tapa, Estonia                                 |        19.83 |
| 3311 | San Leandro, United States                    |        19.83 |
| 3312 | Svaty Jur, Slovakia                           |        19.75 |
| 3313 | Columbia Heights, United States               |        19.75 |
| 3314 | Gainesville, United States                    |        19.75 |
| 3315 | Groveton, United States                       |        19.75 |
| 3316 | Boucherville, Canada                          |        19.75 |
| 3317 | Terrebonne, Canada                            |        19.75 |
| 3318 | Lyon, France                                  |        19.75 |
| 3319 | Schenefeld, Germany                           |        19.75 |
| 3320 | Solingen, Germany                             |        19.75 |
| 3321 | Mammoth Lakes, United States                  |        19.75 |
| 3322 | Rajaori, India                                |        19.75 |
| 3323 | Bene Beraq, Israel                            |        19.75 |
| 3324 | Redondo, Portugal                             |        19.67 |
| 3325 | Medyn', Russia                                |        19.67 |
| 3326 | Stara Pazova, Serbia                          |        19.67 |
| 3327 | West Drayton, United Kingdom                  |        19.67 |
| 3328 | Atascadero, United States                     |        19.67 |
| 3329 | Columbine, United States                      |        19.67 |
| 3330 | Edgewater, United States                      |        19.67 |
| 3331 | Montreal, Canada                              |        19.67 |
| 3332 | Westmount, Canada                             |        19.67 |
| 3333 | Augsburg, Germany                             |        19.67 |
| 3334 | Pointe A Pitre, Guadeloupe                    |        19.67 |
| 3335 | Cape Town, South Africa                       |        19.58 |
| 3336 | Ecorse, United States                         |        19.58 |
| 3337 | Saint Chamond, France                         |        19.58 |
| 3338 | Kennewick, United States                      |        19.58 |
| 3339 | Lynden, United States                         |        19.58 |
| 3340 | Winchester, United States                     |        19.58 |
| 3341 | Herzliyya, Israel                             |        19.58 |
| 3342 | Blackwood, United Kingdom                     |        19.5  |
| 3343 | Cloquet, United States                        |        19.5  |
| 3344 | Goleta, United States                         |        19.5  |
| 3345 | Santa Rosa, Argentina                         |        19.5  |
| 3346 | Dorval, Canada                                |        19.5  |
| 3347 | Paphos, Cyprus                                |        19.5  |
| 3348 | Kelheim, Germany                              |        19.5  |
| 3349 | Krefeld, Germany                              |        19.5  |
| 3350 | Longmont, United States                       |        19.5  |
| 3351 | Loudon, United States                         |        19.5  |
| 3352 | Seaside, United States                        |        19.5  |
| 3353 | Venice Gardens, United States                 |        19.5  |
| 3354 | Bialystok, Poland                             |        19.5  |
| 3355 | Mount Evelyn, Australia                       |        19.42 |
| 3356 | Burgas, Bulgaria                              |        19.42 |
| 3357 | Lancienne Lorette, Canada                     |        19.42 |
| 3358 | Bessemer, United States                       |        19.42 |
| 3359 | San Rafael, United States                     |        19.42 |
| 3360 | Bierun Stary, Poland                          |        19.33 |
| 3361 | Bathurst, Australia                           |        19.33 |
| 3362 | Klagenfurt, Austria                           |        19.33 |
| 3363 | Laval, Canada                                 |        19.33 |
| 3364 | Clermont Ferrand, France                      |        19.33 |
| 3365 | Aquia Harbour, United States                  |        19.33 |
| 3366 | Lachute, Canada                               |        19.25 |
| 3367 | Oradea, Romania                               |        19.25 |
| 3368 | Barrhead, United Kingdom                      |        19.25 |
| 3369 | Arlington, United States                      |        19.25 |
| 3370 | New York, United States                       |        19.25 |
| 3371 | Weiz, Austria                                 |        19.17 |
| 3372 | Minsk, Belarus                                |        19.17 |
| 3373 | Cranbrook, Canada                             |        19.17 |
| 3374 | Gatineau, Canada                              |        19.17 |
| 3375 | Beauvais, France                              |        19.17 |
| 3376 | Reze, France                                  |        19.17 |
| 3377 | Saint Nazaire, France                         |        19.17 |
| 3378 | Sered', Slovakia                              |        19.17 |
| 3379 | Lviv, Ukraine                                 |        19.17 |
| 3380 | Coeur Dalene, United States                   |        19.17 |
| 3381 | Solok, Indonesia                              |        19.08 |
| 3382 | Eisenstadt, Austria                           |        19.08 |
| 3383 | Sherbrooke, Canada                            |        19.08 |
| 3384 | Opfikon, Switzerland                          |        19.08 |
| 3385 | Aqtau, Kazakhstan                             |        19    |
| 3386 | Moncton, Canada                               |        19    |
| 3387 | Hamburg, Germany                              |        19    |
| 3388 | Sosnowiec, Poland                             |        19    |
| 3389 | Ban Dung, Thailand                            |        19    |
| 3390 | Fruitville, United States                     |        19    |
| 3391 | Lake Havasu City, United States               |        19    |
| 3392 | Ha Long, Vietnam                              |        19    |
| 3393 | Napier, New Zealand                           |        18.92 |
| 3394 | Albury, Australia                             |        18.92 |
| 3395 | Shawinigan, Canada                            |        18.92 |
| 3396 | Sorel Tracy, Canada                           |        18.92 |
| 3397 | Bielefeld, Germany                            |        18.92 |
| 3398 | Villanueva Y Geltru, Spain                    |        18.92 |
| 3399 | Hampton, United Kingdom                       |        18.92 |
| 3400 | Kilmarnock, United Kingdom                    |        18.92 |
| 3401 | Charlotte, United States                      |        18.92 |
| 3402 | Cullowhee, United States                      |        18.92 |
| 3403 | Ontario, United States                        |        18.92 |
| 3404 | Handwara, India                               |        18.83 |
| 3405 | Wakuya, Japan                                 |        18.83 |
| 3406 | Levis, Canada                                 |        18.83 |
| 3407 | Ostersund, Sweden                             |        18.83 |
| 3408 | Rotkreuz, Switzerland                         |        18.83 |
| 3409 | Mitcham, United Kingdom                       |        18.83 |
| 3410 | Galt, United States                           |        18.83 |
| 3411 | San Francisco, United States                  |        18.83 |
| 3412 | Kulgam, India                                 |        18.75 |
| 3413 | Rishon Leziyyon, Israel                       |        18.75 |
| 3414 | Goulburn, Australia                           |        18.75 |
| 3415 | Antwerp, Belgium                              |        18.75 |
| 3416 | Kourou, French Guiana                         |        18.75 |
| 3417 | Deming, United States                         |        18.75 |
| 3418 | Port Isabel, United States                    |        18.75 |
| 3419 | Rosice, Czechia                               |        18.67 |
| 3420 | Vrsac, Serbia                                 |        18.67 |
| 3421 | Banbridge, United Kingdom                     |        18.67 |
| 3422 | Chalmette, United States                      |        18.67 |
| 3423 | Tualatin, United States                       |        18.67 |
| 3424 | Amos, Canada                                  |        18.58 |
| 3425 | Beloeil, Canada                               |        18.58 |
| 3426 | Temiskaming Shores, Canada                    |        18.58 |
| 3427 | Arica, Chile                                  |        18.58 |
| 3428 | Dortmund, Germany                             |        18.58 |
| 3429 | Bistrita, Romania                             |        18.58 |
| 3430 | Galati, Romania                               |        18.58 |
| 3431 | Ferrol, Spain                                 |        18.58 |
| 3432 | Chickasaw, United States                      |        18.58 |
| 3433 | Drammen, Norway                               |        18.5  |
| 3434 | Salaberry De Valleyfield, Canada              |        18.5  |
| 3435 | Bottrop, Germany                              |        18.5  |
| 3436 | Munster, Germany                              |        18.5  |
| 3437 | New Haven, United States                      |        18.5  |
| 3438 | Sacramento, United States                     |        18.5  |
| 3439 | Penrith, Australia                            |        18.42 |
| 3440 | Shannon, Canada                               |        18.42 |
| 3441 | St Paul, Canada                               |        18.42 |
| 3442 | Pargas, Finland                               |        18.42 |
| 3443 | Cayenne, French Guiana                        |        18.42 |
| 3444 | Couva, Trinidad And Tobago                    |        18.42 |
| 3445 | Brovary, Ukraine                              |        18.42 |
| 3446 | Khmelnytskyi, Ukraine                         |        18.42 |
| 3447 | Duluth, United States                         |        18.42 |
| 3448 | Lakeland, United States                       |        18.33 |
| 3449 | Waterbury, United States                      |        18.33 |
| 3450 | Jimboomba, Australia                          |        18.33 |
| 3451 | Longueuil, Canada                             |        18.33 |
| 3452 | Istres, France                                |        18.33 |
| 3453 | Vilnius, Lithuania                            |        18.33 |
| 3454 | Kamin' Kashyrs'kyy, Ukraine                   |        18.33 |
| 3455 | Ternopil, Ukraine                             |        18.33 |
| 3456 | Kew Green, United Kingdom                     |        18.33 |
| 3457 | Columbia Falls, United States                 |        18.33 |
| 3458 | Jacksonville, United States                   |        18.25 |
| 3459 | Limoges, France                               |        18.25 |
| 3460 | Handlova, Slovakia                            |        18.25 |
| 3461 | Morrisville, United States                    |        18.17 |
| 3462 | Stara Zagora, Bulgaria                        |        18.17 |
| 3463 | Edmundston, Canada                            |        18.17 |
| 3464 | Estevan, Canada                               |        18.17 |
| 3465 | Timaru, New Zealand                           |        18.17 |
| 3466 | Novohrad Volynskyi, Ukraine                   |        18.17 |
| 3467 | Cucuta, Colombia                              |        18.08 |
| 3468 | Saint Benoit, Reunion                         |        18.08 |
| 3469 | Ziar Nad Hronom, Slovakia                     |        18.08 |
| 3470 | Zurich, Switzerland                           |        18.08 |
| 3471 | Erith, United Kingdom                         |        18.08 |
| 3472 | Lackland Afb, United States                   |        18    |
| 3473 | Talent, United States                         |        18    |
| 3474 | Nogent Sur Oise, France                       |        18    |
| 3475 | Aachen, Germany                               |        18    |
| 3476 | Datteln, Germany                              |        18    |
| 3477 | Petah Tiqwa, Israel                           |        18    |
| 3478 | Pogoanele, Romania                            |        18    |
| 3479 | Linz, Austria                                 |        17.92 |
| 3480 | Larisa, Greece                                |        17.92 |
| 3481 | Invercargill, New Zealand                     |        17.92 |
| 3482 | Laconia, United States                        |        17.83 |
| 3483 | Jihlava, Czechia                              |        17.83 |
| 3484 | Dunedin, New Zealand                          |        17.83 |
| 3485 | Iasi, Romania                                 |        17.83 |
| 3486 | Helsingborg, Sweden                           |        17.83 |
| 3487 | Obukhiv, Ukraine                              |        17.83 |
| 3488 | Granite City, United States                   |        17.83 |
| 3489 | Enns, Austria                                 |        17.75 |
| 3490 | East Highland Park, United States             |        17.75 |
| 3491 | Highland Springs, United States               |        17.67 |
| 3492 | Spokane Valley, United States                 |        17.67 |
| 3493 | Emerald, Australia                            |        17.67 |
| 3494 | Ipswich, Australia                            |        17.67 |
| 3495 | Sumqayit, Azerbaijan                          |        17.67 |
| 3496 | Aix En Provence, France                       |        17.67 |
| 3497 | Saint Ouen, France                            |        17.67 |
| 3498 | Sarreguemines, France                         |        17.67 |
| 3499 | Qiryat Ono, Israel                            |        17.67 |
| 3500 | Rogasovci, Slovenia                           |        17.67 |
| 3501 | Vinnichki, Ukraine                            |        17.67 |
| 3502 | Eltham, United Kingdom                        |        17.67 |
| 3503 | Holly Hill, United States                     |        17.58 |
| 3504 | Parker, United States                         |        17.58 |
| 3505 | South Gate Ridge, United States               |        17.58 |
| 3506 | La Madeleine, France                          |        17.58 |
| 3507 | Wuppertal, Germany                            |        17.58 |
| 3508 | Tsuruta, Japan                                |        17.58 |
| 3509 | Bielawa, Poland                               |        17.58 |
| 3510 | Staraya Kupavna, Russia                       |        17.58 |
| 3511 | Ivano Frankivsk, Ukraine                      |        17.58 |
| 3512 | Brandermill, United States                    |        17.58 |
| 3513 | Pikeville, United States                      |        17.5  |
| 3514 | Treasure Island, United States                |        17.5  |
| 3515 | Kulu, India                                   |        17.5  |
| 3516 | Sendai, Japan                                 |        17.5  |
| 3517 | Holborn, United Kingdom                       |        17.5  |
| 3518 | Carei, Romania                                |        17.42 |
| 3519 | Pezinok, Slovakia                             |        17.42 |
| 3520 | Raymond Terrace, Australia                    |        17.42 |
| 3521 | Leverkusen, Germany                           |        17.42 |
| 3522 | Highlands, United States                      |        17.42 |
| 3523 | Poquoson, United States                       |        17.42 |
| 3524 | Winter Park, United States                    |        17.42 |
| 3525 | Unna, Germany                                 |        17.42 |
| 3526 | Nikel, Russia                                 |        17.33 |
| 3527 | Elizabeth, United States                      |        17.33 |
| 3528 | Klosterneuburg, Austria                       |        17.33 |
| 3529 | Le Havre, France                              |        17.33 |
| 3530 | Hopewell, United States                       |        17.33 |
| 3531 | Lansing, United States                        |        17.33 |
| 3532 | Marianna, United States                       |        17.33 |
| 3533 | Derry, United Kingdom                         |        17.25 |
| 3534 | West Ham, United Kingdom                      |        17.25 |
| 3535 | Carrollton, United States                     |        17.25 |
| 3536 | Monchengladbach, Germany                      |        17.25 |
| 3537 | Rio Vista, United States                      |        17.25 |
| 3538 | Breaza, Romania                               |        17.17 |
| 3539 | Korenovsk, Russia                             |        17.17 |
| 3540 | Stanford Le Hope, United Kingdom              |        17.17 |
| 3541 | Bridgeport, United States                     |        17.17 |
| 3542 | Graz, Austria                                 |        17.17 |
| 3543 | Southwest Ranches, United States              |        17.17 |
| 3544 | Stuart, United States                         |        17.17 |
| 3545 | Manali, India                                 |        17.17 |
| 3546 | Nelson, New Zealand                           |        17.17 |
| 3547 | Murfatlar, Romania                            |        17.08 |
| 3548 | Subotica, Serbia                              |        17.08 |
| 3549 | Adiyaman, Turkey                              |        17.08 |
| 3550 | Barnstaple, United Kingdom                    |        17.08 |
| 3551 | Cooper City, United States                    |        17.08 |
| 3552 | Danbury, United States                        |        17.08 |
| 3553 | Fayetteville, United States                   |        17.08 |
| 3554 | Ansbach, Germany                              |        17.08 |
| 3555 | Lake City, United States                      |        17.08 |
| 3556 | Texarkana, United States                      |        17.08 |
| 3557 | Aomori, Japan                                 |        17.08 |
| 3558 | Kairaki, New Zealand                          |        17.08 |
| 3559 | Elverum, Norway                               |        17.08 |
| 3560 | Petrzalka, Slovakia                           |        17    |
| 3561 | Baie Saint Paul, Canada                       |        17    |
| 3562 | Gennevilliers, France                         |        17    |
| 3563 | Patam, Indonesia                              |        17    |
| 3564 | Astrakhan', Russia                            |        16.92 |
| 3565 | Fruit Cove, United States                     |        16.92 |
| 3566 | Stockerau, Austria                            |        16.92 |
| 3567 | Abbotsford, Canada                            |        16.92 |
| 3568 | Roberval, Canada                              |        16.92 |
| 3569 | Yorkton, Canada                               |        16.92 |
| 3570 | Bello, Colombia                               |        16.92 |
| 3571 | Maardu, Estonia                               |        16.92 |
| 3572 | Vaulx En Velin, France                        |        16.92 |
| 3573 | Iowa City, United States                      |        16.92 |
| 3574 | Spokane, United States                        |        16.92 |
| 3575 | Kerkyra, Greece                               |        16.92 |
| 3576 | Armuli, Iceland                               |        16.92 |
| 3577 | Oxford, United Kingdom                        |        16.83 |
| 3578 | Knittelfeld, Austria                          |        16.83 |
| 3579 | Meaux, France                                 |        16.83 |
| 3580 | Upper Grand Lagoon, United States             |        16.83 |
| 3581 | Warner Robins, United States                  |        16.83 |
| 3582 | Leninsk, Russia                               |        16.75 |
| 3583 | Dnipro, Ukraine                               |        16.75 |
| 3584 | Dayton, United States                         |        16.75 |
| 3585 | Great Falls, United States                    |        16.75 |
| 3586 | Traralgon, Australia                          |        16.75 |
| 3587 | La Serena, Chile                              |        16.75 |
| 3588 | Kastav, Croatia                               |        16.75 |
| 3589 | Naperville, United States                     |        16.75 |
| 3590 | Ho Chi Minh City, Vietnam                     |        16.75 |
| 3591 | Blenheim, New Zealand                         |        16.75 |
| 3592 | Kidbrooke, United Kingdom                     |        16.67 |
| 3593 | East Hartford, United States                  |        16.67 |
| 3594 | Hainburg An Der Donau, Austria                |        16.67 |
| 3595 | Mistelbach, Austria                           |        16.67 |
| 3596 | Voitsberg, Austria                            |        16.67 |
| 3597 | Phnom Penh, Cambodia                          |        16.67 |
| 3598 | Vallejo, United States                        |        16.67 |
| 3599 | Warren, United States                         |        16.67 |
| 3600 | Beloozerskiy, Russia                          |        16.58 |
| 3601 | Snina, Slovakia                               |        16.58 |
| 3602 | Chepstow, United Kingdom                      |        16.58 |
| 3603 | Traun, Austria                                |        16.58 |
| 3604 | Pernik, Bulgaria                              |        16.58 |
| 3605 | Lantana, United States                        |        16.58 |
| 3606 | Raananna, Israel                              |        16.58 |
| 3607 | Natori Shi, Japan                             |        16.58 |
| 3608 | Deta, Romania                                 |        16.5  |
| 3609 | Sundsvall, Sweden                             |        16.5  |
| 3610 | Kremenchuk, Ukraine                           |        16.5  |
| 3611 | Groves, United States                         |        16.5  |
| 3612 | Cali, Colombia                                |        16.5  |
| 3613 | Roskilde, Denmark                             |        16.5  |
| 3614 | Lake Mary, United States                      |        16.5  |
| 3615 | Las Cruces, United States                     |        16.5  |
| 3616 | Redmond, United States                        |        16.5  |
| 3617 | South Burlington, United States               |        16.5  |
| 3618 | Coffs Harbour, Australia                      |        16.42 |
| 3619 | Mioveni, Romania                              |        16.42 |
| 3620 | Umea, Sweden                                  |        16.42 |
| 3621 | Chicago, United States                        |        16.42 |
| 3622 | Greeley, United States                        |        16.42 |
| 3623 | West Melbourne, United States                 |        16.42 |
| 3624 | Sydney, Australia                             |        16.33 |
| 3625 | Miastko, Poland                               |        16.33 |
| 3626 | Brasov, Romania                               |        16.33 |
| 3627 | Sremski Karlovci, Serbia                      |        16.33 |
| 3628 | Truckee, United States                        |        16.33 |
| 3629 | Bat Yam, Israel                               |        16.25 |
| 3630 | Morwell, Australia                            |        16.25 |
| 3631 | Port Pirie, Australia                         |        16.25 |
| 3632 | Muckendorf An Der Donau, Austria              |        16.25 |
| 3633 | Passau, Germany                               |        16.25 |
| 3634 | Yekaterinburg, Russia                         |        16.25 |
| 3635 | Ocala, United States                          |        16.25 |
| 3636 | Lelystad, Netherlands                         |        16.17 |
| 3637 | Granville, Australia                          |        16.17 |
| 3638 | Lovech, Bulgaria                              |        16.17 |
| 3639 | Petite Rosselle, France                       |        16.17 |
| 3640 | Nuremberg, Germany                            |        16.17 |
| 3641 | Braila, Romania                               |        16.17 |
| 3642 | Topoloveni, Romania                           |        16.17 |
| 3643 | Montmagny, Canada                             |        16.08 |
| 3644 | Broadway, United States                       |        16.08 |
| 3645 | Joliet, United States                         |        16.08 |
| 3646 | Knik Fairview, United States                  |        16.08 |
| 3647 | Oak Park, United States                       |        16.08 |
| 3648 | Tallahassee, United States                    |        16.08 |
| 3649 | Hai Duong, Vietnam                            |        16.08 |
| 3650 | Gladstone, Australia                          |        16    |
| 3651 | Amstetten, Austria                            |        16    |
| 3652 | Mazyr, Belarus                                |        16    |
| 3653 | Kemi, Finland                                 |        16    |
| 3654 | Litchfield, United States                     |        16    |
| 3655 | Little Rock, United States                    |        16    |
| 3656 | Moundsville, United States                    |        16    |
| 3657 | Wurzburg, Germany                             |        15.92 |
| 3658 | East Lake, United States                      |        15.92 |
| 3659 | Mont Laurier, Canada                          |        15.83 |
| 3660 | Canton, United States                         |        15.83 |
| 3661 | Omak, United States                           |        15.83 |
| 3662 | Ramat Gan, Israel                             |        15.75 |
| 3663 | Schellenberg, Liechtenstein                   |        15.75 |
| 3664 | Ashton, New Zealand                           |        15.75 |
| 3665 | Creston, Canada                               |        15.75 |
| 3666 | Pereslavl' Zalesskiy, Russia                  |        15.75 |
| 3667 | Noya, Spain                                   |        15.75 |
| 3668 | Vinnytsia, Ukraine                            |        15.75 |
| 3669 | Akron, United States                          |        15.75 |
| 3670 | Clarksville, United States                    |        15.75 |
| 3671 | Sakurazuka, Japan                             |        15.67 |
| 3672 | Dobrich, Bulgaria                             |        15.67 |
| 3673 | Airdrie, Canada                               |        15.67 |
| 3674 | Hinton, Canada                                |        15.67 |
| 3675 | Vantaa, Finland                               |        15.67 |
| 3676 | Dusseldorf, Germany                           |        15.67 |
| 3677 | Ploiesti, Romania                             |        15.67 |
| 3678 | Kyiv, Ukraine                                 |        15.67 |
| 3679 | Rockford, United States                       |        15.67 |
| 3680 | Rahat, Israel                                 |        15.58 |
| 3681 | Glencoe, New Zealand                          |        15.58 |
| 3682 | Mo I Rana, Norway                             |        15.58 |
| 3683 | Wentworthville, Australia                     |        15.58 |
| 3684 | Ganserndorf, Austria                          |        15.58 |
| 3685 | Wels, Austria                                 |        15.58 |
| 3686 | Cologne, Germany                              |        15.58 |
| 3687 | Flensburg, Germany                            |        15.58 |
| 3688 | Alexandria, Romania                           |        15.58 |
| 3689 | Sandy, United Kingdom                         |        15.58 |
| 3690 | Flowing Wells, United States                  |        15.58 |
| 3691 | Chisinau, Moldova                             |        15.5  |
| 3692 | Koszalin, Poland                              |        15.5  |
| 3693 | Temiscouata Sur Le Lac, Canada                |        15.5  |
| 3694 | Cournon Dauvergne, France                     |        15.5  |
| 3695 | Stefanesti, Romania                           |        15.5  |
| 3696 | Tomsk, Russia                                 |        15.5  |
| 3697 | Volgograd, Russia                             |        15.5  |
| 3698 | Cicero, United States                         |        15.5  |
| 3699 | Vinton, United States                         |        15.5  |
| 3700 | Worthington, United States                    |        15.5  |
| 3701 | University Of Virginia, United States         |        15.42 |
| 3702 | Mount Isa, Australia                          |        15.42 |
| 3703 | Flin Flon, Canada                             |        15.42 |
| 3704 | Bobigny, France                               |        15.42 |
| 3705 | Oberhausen, Germany                           |        15.42 |
| 3706 | Ozery, Russia                                 |        15.42 |
| 3707 | Apple Valley, United States                   |        15.42 |
| 3708 | Hammond, United States                        |        15.42 |
| 3709 | Mackay, Australia                             |        15.33 |
| 3710 | Sankt Polten, Austria                         |        15.33 |
| 3711 | Hachimancho, Japan                            |        15.33 |
| 3712 | Rifu, Japan                                   |        15.33 |
| 3713 | Buzau, Romania                                |        15.33 |
| 3714 | Irkutsk, Russia                               |        15.33 |
| 3715 | Albemarle, United States                      |        15.33 |
| 3716 | Bay City, United States                       |        15.33 |
| 3717 | Sunnyside, United States                      |        15.25 |
| 3718 | Toppenish, United States                      |        15.25 |
| 3719 | Moe, Australia                                |        15.25 |
| 3720 | Wagga Wagga, Australia                        |        15.25 |
| 3721 | Gross Enzersdorf, Austria                     |        15.25 |
| 3722 | Vienna, Austria                               |        15.25 |
| 3723 | Hagen, Germany                                |        15.25 |
| 3724 | Zhangaozen, Kazakhstan                        |        15.25 |
| 3725 | Lillehammer, Norway                           |        15.25 |
| 3726 | Canby, United States                          |        15.25 |
| 3727 | Golden Gate, United States                    |        15.25 |
| 3728 | Rahway, United States                         |        15.17 |
| 3729 | Whyalla, Australia                            |        15.17 |
| 3730 | Braunau Am Inn, Austria                       |        15.17 |
| 3731 | Coueron, France                               |        15.17 |
| 3732 | Oslo, Norway                                  |        15.17 |
| 3733 | Gavle, Sweden                                 |        15.17 |
| 3734 | Hartford, United States                       |        15.17 |
| 3735 | Port Macquarie, Australia                     |        15.08 |
| 3736 | Riviere Du Loup, Canada                       |        15.08 |
| 3737 | Nasice, Croatia                               |        15.08 |
| 3738 | Gonesse, France                               |        15.08 |
| 3739 | Villeneuve Sur Lot, France                    |        15.08 |
| 3740 | Ennis, Ireland                                |        15.08 |
| 3741 | Limerick, Ireland                             |        15.08 |
| 3742 | Visby, Sweden                                 |        15.08 |
| 3743 | Lacey, United States                          |        15    |
| 3744 | Orchard Homes, United States                  |        15    |
| 3745 | Zeltweg, Austria                              |        15    |
| 3746 | Weyburn, Canada                               |        15    |
| 3747 | Iquique, Chile                                |        15    |
| 3748 | Dzerzhinskiy, Russia                          |        15    |
| 3749 | Modling, Austria                              |        14.92 |
| 3750 | Schwechat, Austria                            |        14.92 |
| 3751 | Bukittinggi, Indonesia                        |        14.92 |
| 3752 | Dungarvan, Ireland                            |        14.92 |
| 3753 | Krasnodar, Russia                             |        14.92 |
| 3754 | Lobnya, Russia                                |        14.92 |
| 3755 | Princess Anne, United States                  |        14.83 |
| 3756 | Ayr, Australia                                |        14.83 |
| 3757 | Waidhofen An Der Ybbs, Austria                |        14.83 |
| 3758 | Pazin, Croatia                                |        14.83 |
| 3759 | Schiltigheim, France                          |        14.83 |
| 3760 | Hemau, Germany                                |        14.83 |
| 3761 | Salerno, Italy                                |        14.83 |
| 3762 | Tomiya, Japan                                 |        14.83 |
| 3763 | Noumea, New Caledonia                         |        14.83 |
| 3764 | Brisbane, Australia                           |        14.75 |
| 3765 | Saint Louis, France                           |        14.75 |
| 3766 | Wanstead, United Kingdom                      |        14.75 |
| 3767 | Springfield, United States                    |        14.67 |
| 3768 | Villa Constitucion, Argentina                 |        14.67 |
| 3769 | Scharding, Austria                            |        14.67 |
| 3770 | Chilliwack, Canada                            |        14.67 |
| 3771 | Hope, Canada                                  |        14.67 |
| 3772 | Gelsenkirchen, Germany                        |        14.67 |
| 3773 | Warstein, Germany                             |        14.67 |
| 3774 | Alexandra, New Zealand                        |        14.67 |
| 3775 | Presque Isle, United States                   |        14.58 |
| 3776 | Bruck An Der Mur, Austria                     |        14.58 |
| 3777 | Leoben, Austria                               |        14.58 |
| 3778 | Waterford, Ireland                            |        14.58 |
| 3779 | Shiroishi, Japan                              |        14.58 |
| 3780 | Piatra Neamt, Romania                         |        14.58 |
| 3781 | Zhukovskiy, Russia                            |        14.58 |
| 3782 | Bend, United States                           |        14.58 |
| 3783 | Hattiesburg, United States                    |        14.58 |
| 3784 | Honolulu, United States                       |        14.5  |
| 3785 | Lafayette, United States                      |        14.5  |
| 3786 | Platteville, United States                    |        14.5  |
| 3787 | Furstenfeld, Austria                          |        14.5  |
| 3788 | Vocklabruck, Austria                          |        14.5  |
| 3789 | Suwalki, Poland                               |        14.5  |
| 3790 | Columbia City, United States                  |        14.5  |
| 3791 | Targoviste, Romania                           |        14.42 |
| 3792 | Odintsovo, Russia                             |        14.42 |
| 3793 | Greenock, United Kingdom                      |        14.42 |
| 3794 | Cheektowaga, United States                    |        14.42 |
| 3795 | Elkhart, United States                        |        14.42 |
| 3796 | Villach, Austria                              |        14.42 |
| 3797 | Pleiku, Vietnam                               |        14.42 |
| 3798 | Dunboyne, Ireland                             |        14.42 |
| 3799 | Tannum Sands, Australia                       |        14.33 |
| 3800 | Belfort, France                               |        14.33 |
| 3801 | Batumi, Georgia                               |        14.33 |
| 3802 | Furth, Germany                                |        14.33 |
| 3803 | Kapolei, United States                        |        14.33 |
| 3804 | Drama, Greece                                 |        14.33 |
| 3805 | Sarpsborg, Norway                             |        14.33 |
| 3806 | Lyubertsy, Russia                             |        14.25 |
| 3807 | Kapfenberg, Austria                           |        14.25 |
| 3808 | Laredo, United States                         |        14.25 |
| 3809 | Maplewood, United States                      |        14.25 |
| 3810 | Harrisonburg, United States                   |        14.17 |
| 3811 | Tourcoing, France                             |        14.17 |
| 3812 | Gorlitz, Germany                              |        14.17 |
| 3813 | Christchurch, New Zealand                     |        14.17 |
| 3814 | Podol'sk, Russia                              |        14.08 |
| 3815 | Tol'yatti, Russia                             |        14.08 |
| 3816 | Worcester, South Africa                       |        14.08 |
| 3817 | Buffalo, United States                        |        14.08 |
| 3818 | Fort Collins, United States                   |        14.08 |
| 3819 | Tirane, Albania                               |        14.08 |
| 3820 | Scone, Australia                              |        14.08 |
| 3821 | Markranstadt, Germany                         |        14.08 |
| 3822 | Banda Aceh, Indonesia                         |        14.08 |
| 3823 | Rikuzen Takata, Japan                         |        14.08 |
| 3824 | Pukekohe East, New Zealand                    |        14.08 |
| 3825 | Perm', Russia                                 |        14    |
| 3826 | Zhytomyr, Ukraine                             |        14    |
| 3827 | Corinda, Australia                            |        14    |
| 3828 | Bamberg, Germany                              |        14    |
| 3829 | Lifford, Ireland                              |        14    |
| 3830 | Asahikawa, Japan                              |        14    |
| 3831 | Olds, Canada                                  |        13.92 |
| 3832 | Chemnitz, Germany                             |        13.92 |
| 3833 | Duisburg, Germany                             |        13.92 |
| 3834 | Umm el Fahm, Israel                           |        13.92 |
| 3835 | Tonsberg, Norway                              |        13.92 |
| 3836 | Krasnoslobodsk, Russia                        |        13.83 |
| 3837 | Bli Bli, Australia                            |        13.83 |
| 3838 | Hall In Tirol, Austria                        |        13.83 |
| 3839 | Charleroi, Belgium                            |        13.83 |
| 3840 | Sebastopol, United States                     |        13.83 |
| 3841 | Sopron, Hungary                               |        13.83 |
| 3842 | Havelock North, New Zealand                   |        13.83 |
| 3843 | Valky, Ukraine                                |        13.75 |
| 3844 | Aveley, United Kingdom                        |        13.75 |
| 3845 | Rochedale, Australia                          |        13.75 |
| 3846 | Winnipeg, Canada                              |        13.75 |
| 3847 | Tampere, Finland                              |        13.75 |
| 3848 | Nogent Sur Marne, France                      |        13.75 |
| 3849 | Virginia, United States                       |        13.75 |
| 3850 | Kunitachi, Japan                              |        13.75 |
| 3851 | Smolensk, Russia                              |        13.67 |
| 3852 | Stockholm, Sweden                             |        13.67 |
| 3853 | Satun, Thailand                               |        13.67 |
| 3854 | Corpus Christi, United States                 |        13.67 |
| 3855 | Hickory, United States                        |        13.67 |
| 3856 | Tonawanda, United States                      |        13.67 |
| 3857 | Galway, Ireland                               |        13.67 |
| 3858 | Koencho, Japan                                |        13.67 |
| 3859 | Kezmarok, Slovakia                            |        13.58 |
| 3860 | Bitlis, Turkey                                |        13.58 |
| 3861 | Vyshhorod, Ukraine                            |        13.58 |
| 3862 | Toyomamachi teraike, Japan                    |        13.58 |
| 3863 | Lytkarino, Russia                             |        13.5  |
| 3864 | Ulundi, South Africa                          |        13.5  |
| 3865 | Musselburgh, United Kingdom                   |        13.5  |
| 3866 | Anacortes, United States                      |        13.5  |
| 3867 | Chattanooga, United States                    |        13.5  |
| 3868 | Canberra, Australia                           |        13.5  |
| 3869 | Melbourn, Australia                           |        13.5  |
| 3870 | Corner Brook, Canada                          |        13.5  |
| 3871 | Juchen, Germany                               |        13.5  |
| 3872 | Spartanburg, United States                    |        13.5  |
| 3873 | Jakobstad, Finland                            |        13.42 |
| 3874 | Issy Les Moulineaux, France                   |        13.42 |
| 3875 | Lindau, Germany                               |        13.42 |
| 3876 | Vladimir, Russia                              |        13.42 |
| 3877 | Bila Tserkva, Ukraine                         |        13.42 |
| 3878 | Johnstone, United Kingdom                     |        13.42 |
| 3879 | Alameda, United States                        |        13.42 |
| 3880 | Ukiah, United States                          |        13.42 |
| 3881 | Kurihara, Japan                               |        13.33 |
| 3882 | Perth, Australia                              |        13.33 |
| 3883 | Townsville, Australia                         |        13.33 |
| 3884 | Tame, Colombia                                |        13.33 |
| 3885 | Pori, Finland                                 |        13.33 |
| 3886 | Landshut, Germany                             |        13.33 |
| 3887 | Baia Mare, Romania                            |        13.33 |
| 3888 | Ufa, Russia                                   |        13.33 |
| 3889 | Caerleon, United Kingdom                      |        13.33 |
| 3890 | Lakeville, United States                      |        13.33 |
| 3891 | Marysville, United States                     |        13.33 |
| 3892 | Swords, Ireland                               |        13.25 |
| 3893 | Le Grand Quevilly, France                     |        13.25 |
| 3894 | Knic, Serbia                                  |        13.25 |
| 3895 | Amfissa, Greece                               |        13.17 |
| 3896 | Macetown, New Zealand                         |        13.17 |
| 3897 | Grangemouth, United Kingdom                   |        13.17 |
| 3898 | Woolwich, United Kingdom                      |        13.17 |
| 3899 | Cheney, United States                         |        13.17 |
| 3900 | Fishers, United States                        |        13.17 |
| 3901 | Jersey City, United States                    |        13.17 |
| 3902 | Trondheim, Norway                             |        13.08 |
| 3903 | Southport, Australia                          |        13.08 |
| 3904 | Bruck An Der Leitha, Austria                  |        13.08 |
| 3905 | Otradnoye, Russia                             |        13.08 |
| 3906 | Borlange, Sweden                              |        13.08 |
| 3907 | Adelaide, Australia                           |        13    |
| 3908 | Armidale, Australia                           |        13    |
| 3909 | Busteni, Romania                              |        13    |
| 3910 | Voskresensk, Russia                           |        13    |
| 3911 | Rifle, United States                          |        13    |
| 3912 | Moss, Norway                                  |        12.92 |
| 3913 | Deutschlandsberg, Austria                     |        12.92 |
| 3914 | Gronau, Germany                               |        12.92 |
| 3915 | Dolgoprudnyy, Russia                          |        12.92 |
| 3916 | Zolochiv, Ukraine                             |        12.92 |
| 3917 | Bellevue, United States                       |        12.92 |
| 3918 | Courtenay, Canada                             |        12.83 |
| 3919 | Sooke, Canada                                 |        12.83 |
| 3920 | Ramnicu Valcea, Romania                       |        12.83 |
| 3921 | Lawrenceburg, United States                   |        12.83 |
| 3922 | North Laurel, United States                   |        12.83 |
| 3923 | Kauniainen, Finland                           |        12.75 |
| 3924 | Stryy, Ukraine                                |        12.75 |
| 3925 | Eagleton Village, United States               |        12.75 |
| 3926 | Knoxville, United States                      |        12.75 |
| 3927 | Dunleary, Ireland                             |        12.67 |
| 3928 | Murzzuschlag, Austria                         |        12.67 |
| 3929 | Miercurea Ciuc, Romania                       |        12.67 |
| 3930 | Salavat, Russia                               |        12.67 |
| 3931 | Arden Arcade, United States                   |        12.67 |
| 3932 | Pine Ridge, United States                     |        12.67 |
| 3933 | Schwaz, Austria                               |        12.58 |
| 3934 | Kent, Canada                                  |        12.58 |
| 3935 | Lethbridge, Canada                            |        12.58 |
| 3936 | Elista, Russia                                |        12.58 |
| 3937 | Moskovskiy, Russia                            |        12.58 |
| 3938 | Arhavi, Turkey                                |        12.58 |
| 3939 | Bear, United States                           |        12.58 |
| 3940 | Clarkston, United States                      |        12.58 |
| 3941 | Portland, United States                       |        12.58 |
| 3942 | Roanoke Rapids, United States                 |        12.58 |
| 3943 | Utica, United States                          |        12.58 |
| 3944 | Kotel'niki, Russia                            |        12.5  |
| 3945 | Nizhniy Novgorod, Russia                      |        12.5  |
| 3946 | Yuzhno Sakhalinsk, Russia                     |        12.5  |
| 3947 | Gothenburg, Sweden                            |        12.5  |
| 3948 | Belle Glade, United States                    |        12.5  |
| 3949 | Hollabrunn, Austria                           |        12.42 |
| 3950 | Victoria, Canada                              |        12.42 |
| 3951 | Plauen, Germany                               |        12.42 |
| 3952 | Beacon, United States                         |        12.42 |
| 3953 | Lincoln, United States                        |        12.33 |
| 3954 | Madras, United States                         |        12.33 |
| 3955 | Colwood, Canada                               |        12.33 |
| 3956 | Port Moody, Canada                            |        12.33 |
| 3957 | Varkaus, Finland                              |        12.33 |
| 3958 | Marathonas, Greece                            |        12.33 |
| 3959 | Tromso, Norway                                |        12.33 |
| 3960 | Bar Harbor, United States                     |        12.33 |
| 3961 | Venissieux, France                            |        12.25 |
| 3962 | Bergen, Norway                                |        12.25 |
| 3963 | Babeni, Romania                               |        12.25 |
| 3964 | Chelyabinsk, Russia                           |        12.25 |
| 3965 | Ryazan', Russia                               |        12.25 |
| 3966 | Volzhskiy, Russia                             |        12.25 |
| 3967 | Irvine, United Kingdom                        |        12.25 |
| 3968 | Anaconda, United States                       |        12.25 |
| 3969 | Eagle Pass, United States                     |        12.25 |
| 3970 | Gridley, United States                        |        12.25 |
| 3971 | Providence, United States                     |        12.17 |
| 3972 | Stayton, United States                        |        12.17 |
| 3973 | Judenburg, Austria                            |        12.17 |
| 3974 | Langley, Canada                               |        12.17 |
| 3975 | New Westminster, Canada                       |        12.17 |
| 3976 | Kolomna, Russia                               |        12.17 |
| 3977 | Ornskoldsvik, Sweden                          |        12.17 |
| 3978 | Magalia, United States                        |        12.08 |
| 3979 | Weiser, United States                         |        12.08 |
| 3980 | Westbury, United States                       |        12.08 |
| 3981 | Innsbruck, Austria                            |        12.08 |
| 3982 | Liezen, Austria                               |        12.08 |
| 3983 | Salzburg, Austria                             |        12.08 |
| 3984 | Brandon, Canada                               |        12.08 |
| 3985 | Filyro, Greece                                |        12.08 |
| 3986 | Siteia, Greece                                |        12.08 |
| 3987 | Ulbroka, Latvia                               |        12.08 |
| 3988 | Domodedovo, Russia                            |        12.08 |
| 3989 | Krasnogorsk, Russia                           |        12.08 |
| 3990 | Moscow, Russia                                |        12.08 |
| 3991 | Thornton Heath, United Kingdom                |        12.08 |
| 3992 | Cottage Grove, United States                  |        12.08 |
| 3993 | Eugene, United States                         |        12.08 |
| 3994 | Spittal An Der Drau, Austria                  |        12    |
| 3995 | Bayreuth, Germany                             |        12    |
| 3996 | Zwickau, Germany                              |        12    |
| 3997 | Auckland, New Zealand                         |        12    |
| 3998 | Kharkiv, Ukraine                              |        12    |
| 3999 | Clayton, United States                        |        12    |
| 4000 | Colorado Springs, United States               |        12    |
| 4001 | Lewiston, United States                       |        11.92 |
| 4002 | Seattle, United States                        |        11.92 |
| 4003 | Tukwila, United States                        |        11.92 |
| 4004 | Wiener Neustadt, Austria                      |        11.92 |
| 4005 | Akmene, Lithuania                             |        11.92 |
| 4006 | Khimki, Russia                                |        11.92 |
| 4007 | Duncan, Canada                                |        11.83 |
| 4008 | Waitakere, New Zealand                        |        11.83 |
| 4009 | Harstad, Norway                               |        11.83 |
| 4010 | Klimovsk, Russia                              |        11.83 |
| 4011 | Cookeville, United States                     |        11.83 |
| 4012 | Dyersburg, United States                      |        11.83 |
| 4013 | Fife, United States                           |        11.83 |
| 4014 | Whistler, Canada                              |        11.75 |
| 4015 | Sorong, Indonesia                             |        11.75 |
| 4016 | Cagliari, Italy                               |        11.75 |
| 4017 | Kurgan, Russia                                |        11.75 |
| 4018 | Uppsala, Sweden                               |        11.75 |
| 4019 | Boryspil', Ukraine                            |        11.75 |
| 4020 | Columbia, United States                       |        11.75 |
| 4021 | Lemay, United States                          |        11.67 |
| 4022 | Midland, United States                        |        11.67 |
| 4023 | Castlebar, Ireland                            |        11.67 |
| 4024 | Cork, Ireland                                 |        11.67 |
| 4025 | Odesa, Ukraine                                |        11.67 |
| 4026 | Cramond, United Kingdom                       |        11.67 |
| 4027 | Rhymney, United Kingdom                       |        11.67 |
| 4028 | Rensselaer, United States                     |        11.58 |
| 4029 | Concord, Australia                            |        11.58 |
| 4030 | Homyel', Belarus                              |        11.58 |
| 4031 | Bonn, Germany                                 |        11.58 |
| 4032 | Sopur, India                                  |        11.58 |
| 4033 | Kuji, Japan                                   |        11.58 |
| 4034 | Reutov, Russia                                |        11.58 |
| 4035 | Vidnoye, Russia                               |        11.58 |
| 4036 | East Kilbride, United Kingdom                 |        11.58 |
| 4037 | Harriman, United States                       |        11.58 |
| 4038 | Kumanovo, Macedonia                           |        11.5  |
| 4039 | Alesund, Norway                               |        11.5  |
| 4040 | Kolpino, Russia                               |        11.5  |
| 4041 | Norrkoping, Sweden                            |        11.5  |
| 4042 | Bemidji, United States                        |        11.5  |
| 4043 | Bloomington, United States                    |        11.5  |
| 4044 | Mytishchi, Russia                             |        11.42 |
| 4045 | Queensferry, United Kingdom                   |        11.42 |
| 4046 | Baker City, United States                     |        11.42 |
| 4047 | Grand Falls, Canada                           |        11.42 |
| 4048 | Stavanger, Norway                             |        11.42 |
| 4049 | Altamont, United States                       |        11.33 |
| 4050 | White Center, United States                   |        11.33 |
| 4051 | Cupar, United Kingdom                         |        11.25 |
| 4052 | Partick, United Kingdom                       |        11.25 |
| 4053 | Krems An Der Donau, Austria                   |        11.25 |
| 4054 | Sankt Andra, Austria                          |        11.25 |
| 4055 | Kouvola, Finland                              |        11.25 |
| 4056 | Oulu, Finland                                 |        11.25 |
| 4057 | Prineville, United States                     |        11.17 |
| 4058 | Wexford, Ireland                              |        11.17 |
| 4059 | Slanic, Romania                               |        11.08 |
| 4060 | Kazan, Russia                                 |        11.08 |
| 4061 | Linkoping, Sweden                             |        11.08 |
| 4062 | Cherkasy, Ukraine                             |        11.08 |
| 4063 | Vyshneve, Ukraine                             |        11.08 |
| 4064 | Inverness, United Kingdom                     |        11.08 |
| 4065 | Ellensburg, United States                     |        11.08 |
| 4066 | San Jose, Costa Rica                          |        11.08 |
| 4067 | Akureyri, Iceland                             |        11.08 |
| 4068 | Rostov, Russia                                |        11    |
| 4069 | Antigonish, Canada                            |        11    |
| 4070 | Huasco, Chile                                 |        11    |
| 4071 | Kuopio, Finland                               |        11    |
| 4072 | Ridgefield, United States                     |        11    |
| 4073 | Riga, Latvia                                  |        11    |
| 4074 | Dedovsk, Russia                               |        10.92 |
| 4075 | Krasnoarmeysk, Russia                         |        10.92 |
| 4076 | Chornomors'k, Ukraine                         |        10.92 |
| 4077 | Hartberg, Austria                             |        10.92 |
| 4078 | Kentville, Canada                             |        10.92 |
| 4079 | Medicine Hat, Canada                          |        10.92 |
| 4080 | Nanaimo, Canada                               |        10.92 |
| 4081 | Surrey, Canada                                |        10.92 |
| 4082 | Terrace, Canada                               |        10.92 |
| 4083 | Kingsport, United States                      |        10.92 |
| 4084 | Lockwood, United States                       |        10.92 |
| 4085 | Naas, Ireland                                 |        10.92 |
| 4086 | Balashikha, Russia                            |        10.83 |
| 4087 | Sterlitamak, Russia                           |        10.83 |
| 4088 | Dunfermline, United Kingdom                   |        10.83 |
| 4089 | Radcliffe, United Kingdom                     |        10.83 |
| 4090 | Uddingston, United Kingdom                    |        10.83 |
| 4091 | Grand Junction, United States                 |        10.83 |
| 4092 | Cape Breton, Canada                           |        10.83 |
| 4093 | Jyvaskyla, Finland                            |        10.83 |
| 4094 | Palmer, United States                         |        10.83 |
| 4095 | Port Laoise, Ireland                          |        10.83 |
| 4096 | Ashino, Japan                                 |        10.83 |
| 4097 | Vsevolozhsk, Russia                           |        10.75 |
| 4098 | Kranjska Gora, Slovenia                       |        10.75 |
| 4099 | Broxburn, United Kingdom                      |        10.75 |
| 4100 | Emmett, United States                         |        10.75 |
| 4101 | Lahti, Finland                                |        10.75 |
| 4102 | Longford, Ireland                             |        10.75 |
| 4103 | Leith, United Kingdom                         |        10.67 |
| 4104 | Schladming, Austria                           |        10.67 |
| 4105 | Squamish, Canada                              |        10.67 |
| 4106 | Vancouver, United States                      |        10.67 |
| 4107 | Rauma, Finland                                |        10.58 |
| 4108 | Zelenodol'sk, Russia                          |        10.5  |
| 4109 | Sodankyla, Finland                            |        10.5  |
| 4110 | Huron, United States                          |        10.5  |
| 4111 | Dun Dealgan, Ireland                          |        10.42 |
| 4112 | Petaling Jaya, Malaysia                       |        10.42 |
| 4113 | Merimbula, Australia                          |        10.42 |
| 4114 | New Glasgow, Canada                           |        10.42 |
| 4115 | Port Alberni, Canada                          |        10.42 |
| 4116 | Woodfin, United States                        |        10.42 |
| 4117 | Turku, Finland                                |        10.33 |
| 4118 | Cherepovets, Russia                           |        10.33 |
| 4119 | Linlithgow, United Kingdom                    |        10.33 |
| 4120 | Elektrougli, Russia                           |        10.25 |
| 4121 | Ulan Ude, Russia                              |        10.25 |
| 4122 | Odessa, United States                         |        10.25 |
| 4123 | Port Angeles, United States                   |        10.25 |
| 4124 | Tacoma, United States                         |        10.25 |
| 4125 | Dublin, Ireland                               |        10.17 |
| 4126 | Central Coast, Australia                      |        10.17 |
| 4127 | Deinze, Belgium                               |        10.17 |
| 4128 | Burnaby, Canada                               |        10.17 |
| 4129 | Constanta, Romania                            |        10.17 |
| 4130 | General Pico, Argentina                       |        10.08 |
| 4131 | Giurgiu, Romania                              |        10.08 |
| 4132 | Boyarka, Ukraine                              |        10.08 |
| 4133 | Dundee, United Kingdom                        |        10.08 |
| 4134 | Pierre, United States                         |        10.08 |
| 4135 | Wangaratta, Australia                         |        10    |
| 4136 | Bad Ischl, Austria                            |        10    |
| 4137 | Stirling, United Kingdom                      |        10    |
| 4138 | Wytheville, United States                     |        10    |
| 4139 | Murata, Japan                                 |         9.92 |
| 4140 | Johor Bahru, Malaysia                         |         9.92 |
| 4141 | Sechelt, Canada                               |         9.92 |
| 4142 | Colmar, France                                |         9.92 |
| 4143 | Kulmbach, Germany                             |         9.92 |
| 4144 | Temryuk, Russia                               |         9.92 |
| 4145 | Chapelhall, United Kingdom                    |         9.92 |
| 4146 | Rayleigh, United Kingdom                      |         9.92 |
| 4147 | North Bend, United States                     |         9.92 |
| 4148 | Mournies, Greece                              |         9.83 |
| 4149 | Cooma, Australia                              |         9.83 |
| 4150 | Klingenthal, Germany                          |         9.83 |
| 4151 | High Blantyre, United Kingdom                 |         9.83 |
| 4152 | Fredericksburg, United States                 |         9.83 |
| 4153 | Moses Lake, United States                     |         9.83 |
| 4154 | Pitt Meadows, Canada                          |         9.75 |
| 4155 | Bonnybridge, United Kingdom                   |         9.75 |
| 4156 | Lanark, United Kingdom                        |         9.75 |
| 4157 | Motherwell, United Kingdom                    |         9.75 |
| 4158 | Tralee, Ireland                               |         9.67 |
| 4159 | Strenci, Latvia                               |         9.67 |
| 4160 | Freistadt, Austria                            |         9.67 |
| 4161 | Kufstein, Austria                             |         9.67 |
| 4162 | Delta, Canada                                 |         9.67 |
| 4163 | Mineral'nyye Vody, Russia                     |         9.67 |
| 4164 | Kristiansand, Norway                          |         9.58 |
| 4165 | Schrems, Austria                              |         9.58 |
| 4166 | Ivanovo, Russia                               |         9.58 |
| 4167 | Novorossiysk, Russia                          |         9.58 |
| 4168 | Irpin', Ukraine                               |         9.58 |
| 4169 | Kirkintilloch, United Kingdom                 |         9.58 |
| 4170 | Rosyth, United Kingdom                        |         9.58 |
| 4171 | Hermiston, United States                      |         9.58 |
| 4172 | Suffolk, United States                        |         9.58 |
| 4173 | Carlow, Ireland                               |         9.5  |
| 4174 | Lienz, Austria                                |         9.5  |
| 4175 | Zell Am See, Austria                          |         9.5  |
| 4176 | Lohja, Finland                                |         9.5  |
| 4177 | Crieff, United Kingdom                        |         9.5  |
| 4178 | Hazel Grove, United Kingdom                   |         9.5  |
| 4179 | Rumford, United States                        |         9.5  |
| 4180 | Ciudad Guayana, Venezuela                     |         9.5  |
| 4181 | Marystown, Canada                             |         9.42 |
| 4182 | Mount Pearl Park, Canada                      |         9.42 |
| 4183 | Monaghan, Ireland                             |         9.42 |
| 4184 | Falkirk, United Kingdom                       |         9.42 |
| 4185 | Milngavie, United Kingdom                     |         9.42 |
| 4186 | Krasnoyarsk, Russia                           |         9.33 |
| 4187 | Saint Petersburg, Russia                      |         9.33 |
| 4188 | Paarl, South Africa                           |         9.33 |
| 4189 | Duntocher, United Kingdom                     |         9.33 |
| 4190 | Kirkcaldy, United Kingdom                     |         9.33 |
| 4191 | Airway Heights, United States                 |         9.33 |
| 4192 | Ben Lomond, United States                     |         9.33 |
| 4193 | Granite Falls, United States                  |         9.33 |
| 4194 | Steyr, Austria                                |         9.25 |
| 4195 | Halifax, Canada                               |         9.25 |
| 4196 | Saue, Estonia                                 |         9.25 |
| 4197 | Seinajoki, Finland                            |         9.25 |
| 4198 | Konakovo, Russia                              |         9.25 |
| 4199 | Beppucho, Japan                               |         9.17 |
| 4200 | Forfar, United Kingdom                        |         9.17 |
| 4201 | Buena Vista, United States                    |         9.17 |
| 4202 | Wenatchee, United States                      |         9.08 |
| 4203 | Baranavichy, Belarus                          |         9.08 |
| 4204 | Odense, Denmark                               |         9.08 |
| 4205 | Nenagh, Ireland                               |         9.08 |
| 4206 | Resita, Romania                               |         9.08 |
| 4207 | Vaxjo, Sweden                                 |         9.08 |
| 4208 | Bothwell, United Kingdom                      |         9.08 |
| 4209 | Grafton, Australia                            |         9    |
| 4210 | Raisio, Finland                               |         9    |
| 4211 | Basse Terre, Guadeloupe                       |         9    |
| 4212 | Bodo, Norway                                  |         9    |
| 4213 | Alloa, United Kingdom                         |         9    |
| 4214 | Coatbridge, United Kingdom                    |         9    |
| 4215 | Juneau, United States                         |         8.92 |
| 4216 | North Auburn, United States                   |         8.92 |
| 4217 | Scottsdale, Australia                         |         8.92 |
| 4218 | Kitimat, Canada                               |         8.92 |
| 4219 | Ros Comain, Ireland                           |         8.92 |
| 4220 | Trim, Ireland                                 |         8.92 |
| 4221 | Currie, United Kingdom                        |         8.92 |
| 4222 | Copsa Mica, Romania                           |         8.83 |
| 4223 | Kostroma, Russia                              |         8.83 |
| 4224 | Kilsyth, United Kingdom                       |         8.75 |
| 4225 | Walla Walla, United States                    |         8.67 |
| 4226 | Viljandi, Estonia                             |         8.67 |
| 4227 | Kokkola, Finland                              |         8.67 |
| 4228 | Auburn, United States                         |         8.67 |
| 4229 | Launceston, Australia                         |         8.58 |
| 4230 | Ostashkov, Russia                             |         8.58 |
| 4231 | Bozeman, United States                        |         8.58 |
| 4232 | Naantali, Finland                             |         8.5  |
| 4233 | Targu Ocna, Romania                           |         8.5  |
| 4234 | Borovsk, Russia                               |         8.42 |
| 4235 | Hillsboro, United States                      |         8.42 |
| 4236 | Sweet Home, United States                     |         8.42 |
| 4237 | Protvino, Russia                              |         8.33 |
| 4238 | Lubbock, United States                        |         8.33 |
| 4239 | Ermoupoli, Greece                             |         8.33 |
| 4240 | Hafnarfjordur, Iceland                        |         8.33 |
| 4241 | Collie, Australia                             |         8.25 |
| 4242 | Kuala Lumpur, Malaysia                        |         8.25 |
| 4243 | Hameenlinna, Finland                          |         8.17 |
| 4244 | Kotka, Finland                                |         8.17 |
| 4245 | Pendleton, United States                      |         8.17 |
| 4246 | Melton, Australia                             |         8.08 |
| 4247 | Akranes, Iceland                              |         8.08 |
| 4248 | Chelan, United States                         |         8    |
| 4249 | Gmunden, Austria                              |         8    |
| 4250 | Tracyton, United States                       |         8    |
| 4251 | Tallaght, Ireland                             |         8    |
| 4252 | Brasilia, Brazil                              |         7.92 |
| 4253 | Arvin, United States                          |         7.83 |
| 4254 | Connell, United States                        |         7.83 |
| 4255 | Sao Joao da Boa Vista, Brazil                 |         7.83 |
| 4256 | Lake Forest Park, United States               |         7.83 |
| 4257 | Atyrau, Kazakhstan                            |         7.83 |
| 4258 | Slavyansk na Kubani, Russia                   |         7.75 |
| 4259 | Bellingham, United States                     |         7.75 |
| 4260 | Raahe, Finland                                |         7.75 |
| 4261 | Wodonga, Australia                            |         7.67 |
| 4262 | Harjavalta, Finland                           |         7.67 |
| 4263 | Belorechensk, Russia                          |         7.58 |
| 4264 | Karlskrona, Sweden                            |         7.58 |
| 4265 | Chapeco, Brazil                               |         7.58 |
| 4266 | Lappeenranta, Finland                         |         7.58 |
| 4267 | Silverton, United States                      |         7.58 |
| 4268 | Twin Falls, United States                     |         7.58 |
| 4269 | Nuneaton, United Kingdom                      |         7.5  |
| 4270 | Rosario, Argentina                            |         7.5  |
| 4271 | Carpentras, France                            |         7.5  |
| 4272 | Quincy, United States                         |         7.5  |
| 4273 | Shelton, United States                        |         7.5  |
| 4274 | Ikskile, Latvia                               |         7.5  |
| 4275 | Kuching, Malaysia                             |         7.5  |
| 4276 | Clonmel, Ireland                              |         7.42 |
| 4277 | Hjarup, Sweden                                |         7.42 |
| 4278 | Stretford, United Kingdom                     |         7.42 |
| 4279 | Eagle Point, United States                    |         7.42 |
| 4280 | Tukums, Latvia                                |         7.33 |
| 4281 | Devonport, Australia                          |         7.33 |
| 4282 | Ulverstone, Australia                         |         7.33 |
| 4283 | Stepney, United Kingdom                       |         7.33 |
| 4284 | The Dalles, United States                     |         7.33 |
| 4285 | Fussen, Germany                               |         7.25 |
| 4286 | Turceni, Romania                              |         7.25 |
| 4287 | Achinsk, Russia                               |         7.17 |
| 4288 | Chehalis, United States                       |         7.17 |
| 4289 | An Cabhan, Ireland                            |         7.08 |
| 4290 | Kingston, Australia                           |         7.08 |
| 4291 | Braslaw, Belarus                              |         7.08 |
| 4292 | Novo Hamburgo, Brazil                         |         7.08 |
| 4293 | North Cowichan, Canada                        |         7.08 |
| 4294 | Imatra, Finland                               |         7.08 |
| 4295 | Yaroslavl', Russia                            |         7.08 |
| 4296 | Holualoa, United States                       |         7.08 |
| 4297 | Prato, Italy                                  |         7    |
| 4298 | Bunbury, Australia                            |         7    |
| 4299 | Vaasa, Finland                                |         7    |
| 4300 | Yefremov, Russia                              |         7    |
| 4301 | Wailuku, United States                        |         7    |
| 4302 | Kalgoorlie, Australia                         |         6.92 |
| 4303 | Parkes, Australia                             |         6.92 |
| 4304 | Darregueira, Argentina                        |         6.83 |
| 4305 | Kaarina, Finland                              |         6.83 |
| 4306 | Leeton, Australia                             |         6.67 |
| 4307 | Narrabri, Australia                           |         6.67 |
| 4308 | Oatlands, Australia                           |         6.58 |
| 4309 | Battle Ground, United States                  |         6.58 |
| 4310 | Red Cliffs, Australia                         |         6.5  |
| 4311 | Bucha, Ukraine                                |         6.5  |
| 4312 | Pullman, United States                        |         6.42 |
| 4313 | New Norfolk, Australia                        |         6.42 |
| 4314 | Oliver Paipoonge, Canada                      |         6.42 |
| 4315 | Balyqshy, Kazakhstan                          |         6.42 |
| 4316 | Navodari, Romania                             |         6.42 |
| 4317 | Lismore, Australia                            |         6.33 |
| 4318 | Cobh, Ireland                                 |         6.33 |
| 4319 | Hailey, United States                         |         6.33 |
| 4320 | Longview, United States                       |         6.25 |
| 4321 | Taos, United States                           |         6.25 |
| 4322 | Son La, Vietnam                               |         6.25 |
| 4323 | Aluksne, Latvia                               |         6.25 |
| 4324 | La Grande, United States                      |         6.17 |
| 4325 | La Massana, Andorra                           |         6.17 |
| 4326 | Zelenogorsk, Russia                           |         6.17 |
| 4327 | Hilo, United States                           |         6.08 |
| 4328 | Hadfield, United Kingdom                      |         6.08 |
| 4329 | Geraldton, Australia                          |         6    |
| 4330 | Smithton, Australia                           |         6    |
| 4331 | Jamsa, Finland                                |         6    |
| 4332 | Saint George's, Grenada                       |         6    |
| 4333 | Vereya, Russia                                |         6    |
| 4334 | Cootamundra, Australia                        |         5.92 |
| 4335 | Worgl, Austria                                |         5.92 |
| 4336 | Campbell River, Canada                        |         5.92 |
| 4337 | Daugavpils, Latvia                            |         5.92 |
| 4338 | Vanrhynsdorp, South Africa                    |         5.92 |
| 4339 | Deniliquin, Australia                         |         5.83 |
| 4340 | West Vancouver, Canada                        |         5.83 |
| 4341 | Punta Arenas, Chile                           |         5.83 |
| 4342 | Rochefort, France                             |         5.75 |
| 4343 | Killarney, Ireland                            |         5.75 |
| 4344 | Calan, Romania                                |         5.75 |
| 4345 | Bourke, Australia                             |         5.67 |
| 4346 | Mildura, Australia                            |         5.67 |
| 4347 | Dubbo, Australia                              |         5.58 |
| 4348 | Mount Vernon, United States                   |         5.5  |
| 4349 | Forbes, Australia                             |         5.5  |
| 4350 | Hawaiian Paradise Park, United States         |         5.5  |
| 4351 | Beaverton, United States                      |         5.42 |
| 4352 | Cowra, Australia                              |         5.42 |
| 4353 | Ivanhoe, Australia                            |         5.42 |
| 4354 | Carrick on Shannon, Ireland                   |         5.42 |
| 4355 | Gatchina, Russia                              |         5.33 |
| 4356 | Clarkston Heights Vineland, United States     |         5.33 |
| 4357 | Knysna, South Africa                          |         5.25 |
| 4358 | Wynyard, Australia                            |         5.25 |
| 4359 | Kerch, Ukraine                                |         5.17 |
| 4360 | Hobart, Australia                             |         5.17 |
| 4361 | Moree, Australia                              |         5.17 |
| 4362 | Rexburg, United States                        |         5.17 |
| 4363 | Busselton, Australia                          |         5    |
| 4364 | Porto Alegre, Brazil                          |         5    |
| 4365 | Tay Ninh, Vietnam                             |         4.92 |
| 4366 | San Juan, Puerto Rico                         |         4.75 |
| 4367 | Renningen, Germany                            |         4.75 |
| 4368 | Tullamore, Ireland                            |         4.75 |
| 4369 | Nadlac, Romania                               |         4.58 |
| 4370 | Bendigo, Australia                            |         4.58 |
| 4371 | Hunedoara, Romania                            |         4.5  |
| 4372 | Albany, Australia                             |         4.5  |
| 4373 | Bordertown, Australia                         |         4.5  |
| 4374 | Queenstown, Australia                         |         4.5  |
| 4375 | Biel/Bienne, Switzerland                      |         4.42 |
| 4376 | Port Townsend, United States                  |         4.42 |
| 4377 | Griffith, Australia                           |         4.33 |
| 4378 | Caguas, Puerto Rico                           |         4.33 |
| 4379 | Berri, Australia                              |         4.25 |
| 4380 | Inverell, Australia                           |         4.25 |
| 4381 | Broken Hill, Australia                        |         4.17 |
| 4382 | Evora, Portugal                               |         4.17 |
| 4383 | Como, Italy                                   |         4.08 |
| 4384 | Codru, Moldova                                |         3.92 |
| 4385 | Swan Hill, Australia                          |         3.92 |
| 4386 | Plock, Poland                                 |         3.92 |
| 4387 | Isaccea, Romania                              |         3.92 |
| 4388 | Bicheno, Australia                            |         3.83 |
| 4389 | Ouyen, Australia                              |         3.83 |
| 4390 | Caledon, South Africa                         |         3.75 |
| 4391 | Sandefjord, Norway                            |         3.58 |
| 4392 | Thargomindah, Australia                       |         3.58 |
| 4393 | Ilukste, Latvia                               |         3.5  |
| 4394 | Oakley, United Kingdom                        |         3.42 |
| 4395 | Backa Topola, Serbia                          |         3.33 |
| 4396 | Novara, Italy                                 |         3.25 |
| 4397 | Sorum, Norway                                 |         3    |
| 4398 | Otelu Rosu, Romania                           |         2.67 |
| 4399 | Siret, Romania                                |         2.67 |
| 4400 | Kaluga, Russia                                |         2.67 |
| 4401 | Burnie, Australia                             |         2.58 |
| 4402 | Saldanha, South Africa                        |         2.42 |
| 4403 | Laage, Germany                                |         2.33 |
| 4404 | Narangba, Australia                           |         2.25 |
| 4405 | Oak Harbor, United States                     |         2.25 |
| 4406 | Pitesti, Romania                              |         2.17 |
| 4407 | Wilcannia, Australia                          |         2.08 |
| 4408 | Hoegaarden, Belgium                           |         1.83 |
| 4409 | Tan An, Vietnam                               |         1.75 |
| 4410 | Podvelka, Slovenia                            |         1.67 |
| 4411 | Hod HaSharon, Israel                          |         1.58 |
| 4412 | Kuala Belait, Brunei                          |         1.33 |
| 4413 | Tutong, Brunei                                |         1.33 |
| 4414 | Lihue, United States                          |         1.25 |
| 4415 | Bandar Seri Begawan, Brunei                   |         1.25 |
| 4416 | Trujillo Alto, Puerto Rico                    |         1.08 |
| 4417 | Ballarat, Australia                           |         1    |
| 4418 | Bangar, Brunei                                |         0.67 |
| 4419 | Dubrovytsya, Ukraine                          |       nan    |
| 4420 | Ndjamena, Chad                                |       nan    |
| 4421 | Phonsavan, Laos                               |       nan    |
| 4422 | Jinchang, China                               |       nan    |
| 4423 | Phon Hong, Laos                               |       nan    |
| 4424 | Jiroft, Iran                                  |       nan    |
| 4425 | Matam, Senegal                                |       nan    |
| 4426 | Bandar E Genaveh, Iran                        |       nan    |
| 4427 | Abu Qir, Egypt                                |       nan    |
| 4428 | Bamako, Mali                                  |       nan    |
| 4429 | Darhan, Mongolia                              |       nan    |
| 4430 | Ban Ton Pao, Thailand                         |       nan    |
| 4431 | Lerma, Mexico                                 |       nan    |
| 4432 | Sing Buri, Thailand                           |       nan    |
| 4433 | Ban Piang Luang, Thailand                     |       nan    |
| 4434 | Iganga, Uganda                                |       nan    |
| 4435 | Ban Mae Kha Tai, Thailand                     |       nan    |
| 4436 | Maiduguri, Nigeria                            |       nan    |
| 4437 | Et Tira, Israel                               |       nan    |
| 4438 | Al Khubar, Saudi Arabia                       |       nan    |
| 4439 | Phu Ly, Vietnam                               |       nan    |
| 4440 | Kabale, Uganda                                |       nan    |
| 4441 | Mahilyow, Belarus                             |       nan    |
| 4442 | Yunxian Chengguanzhen, China                  |       nan    |
| 4443 | Quang Tri, Vietnam                            |       nan    |
| 4444 | Iranshahr, Iran                               |       nan    |
| 4445 | Hoa Binh, Vietnam                             |       nan    |
| 4446 | Thai Binh, Vietnam                            |       nan    |
| 4447 | Tlajomulco De Zuniga, Mexico                  |       nan    |
| 4448 | Suhbaatar, Mongolia                           |       nan    |
| 4449 | Panjakent, Tajikistan                         |       nan    |
| 4450 | Al Fujayrah, United Arab Emirates             |       nan    |
| 4451 | Gomez Palacio, Mexico                         |       nan    |
| 4452 | Piedras Negras, Mexico                        |       nan    |
| 4453 | Baghdad, Iraq                                 |       nan    |
| 4454 | Port Harcourt, Nigeria                        |       nan    |
| 4455 | Calabar, Nigeria                              |       nan    |
| 4456 | Jixi, China                                   |       nan    |
| 4457 | Shahe, China                                  |       nan    |
| 4458 | Xinji, China                                  |       nan    |
| 4459 | Bang Racham, Thailand                         |       nan    |
| 4460 | Tha Maka, Thailand                            |       nan    |
| 4461 | Mityana, Uganda                               |       nan    |
| 4462 | Olgiy, Mongolia                               |       nan    |
| 4463 | Zongo, Congo (Kinshasa)                       |       nan    |
| 4464 | Manama, Bahrain                               |       nan    |
| 4465 | Nong Bua Lamphu, Thailand                     |       nan    |
| 4466 | Wakiso, Uganda                                |       nan    |
| 4467 | Borujerd, Iran                                |       nan    |
| 4468 | Mexicali, Mexico                              |       nan    |
| 4469 | Warri, Nigeria                                |       nan    |
| 4470 | Fort Portal, Uganda                           |       nan    |
| 4471 | Mubende, Uganda                               |       nan    |
| 4472 | Thakhek, Laos                                 |       nan    |
| 4473 | Kant, Kyrgyzstan                              |       nan    |
| 4474 | Techirghiol, Romania                          |       nan    |
| 4475 | Luuka Town, Uganda                            |       nan    |
| 4476 | Gaobeidian, China                             |       nan    |
| 4477 | Nangong, China                                |       nan    |
| 4478 | Taihecun, China                               |       nan    |
| 4479 | Douala, Cameroon                              |       nan    |
| 4480 | Wuan, China                                   |       nan    |
| 4481 | Oskemen, Kazakhstan                           |       nan    |
| 4482 | Erdenet, Mongolia                             |       nan    |
| 4483 | Osogbo, Nigeria                               |       nan    |
| 4484 | Thanh Hoa, Vietnam                            |       nan    |
| 4485 | Lop Buri, Thailand                            |       nan    |
| 4486 | Orumiyeh, Iran                                |       nan    |
| 4487 | Qatsrin, Israel                               |       nan    |
| 4488 | Kara Balta, Kyrgyzstan                        |       nan    |
| 4489 | Naryn, Kyrgyzstan                             |       nan    |
| 4490 | Dingzhou, China                               |       nan    |
| 4491 | Renqiu, China                                 |       nan    |
| 4492 | Fardis, Iran                                  |       nan    |
| 4493 | Bueng Kan, Thailand                           |       nan    |
| 4494 | Prachuap Khiri Khan, Thailand                 |       nan    |
| 4495 | Boskovice, Czechia                            |       nan    |
| 4496 | Bandar Abbas, Iran                            |       nan    |
| 4497 | Golmeh, Iran                                  |       nan    |
| 4498 | San Pablo De Las Salinas, Mexico              |       nan    |
| 4499 | Kamphaeng Phet, Thailand                      |       nan    |
| 4500 | Phichit, Thailand                             |       nan    |
| 4501 | Kasese, Uganda                                |       nan    |
| 4502 | Ban Aranyik, Thailand                         |       nan    |
| 4503 | Chum Phae, Thailand                           |       nan    |
| 4504 | Anguo, China                                  |       nan    |
| 4505 | Saltillo, Mexico                              |       nan    |
| 4506 | Borazjan, Iran                                |       nan    |
| 4507 | Khorramshahr, Iran                            |       nan    |
| 4508 | Kara Suu, Kyrgyzstan                          |       nan    |
| 4509 | Xam Nua, Laos                                 |       nan    |
| 4510 | Bazhou, China                                 |       nan    |
| 4511 | Hejian, China                                 |       nan    |
| 4512 | Shenzhou, China                               |       nan    |
| 4513 | Kuchinarai, Thailand                          |       nan    |
| 4514 | Takhli, Thailand                              |       nan    |
| 4515 | Gorazde, Bosnia And Herzegovina               |       nan    |
| 4516 | Balykchy, Kyrgyzstan                          |       nan    |
| 4517 | Nang Rong, Thailand                           |       nan    |
| 4518 | Gulu, Uganda                                  |       nan    |
| 4519 | Mukono, Uganda                                |       nan    |
| 4520 | Cacak, Serbia                                 |       nan    |
| 4521 | Kulob, Tajikistan                             |       nan    |
| 4522 | Ang Thong, Thailand                           |       nan    |
| 4523 | Ban Phru, Thailand                            |       nan    |
| 4524 | Phon, Thailand                                |       nan    |
| 4525 | Botou, China                                  |       nan    |
| 4526 | Luanzhou, China                               |       nan    |
| 4527 | Orchomenos, Greece                            |       nan    |
| 4528 | Tepotzotlan, Mexico                           |       nan    |
| 4529 | Ilorin, Nigeria                               |       nan    |
| 4530 | Huanghua, China                               |       nan    |
| 4531 | Lom Sak, Thailand                             |       nan    |
| 4532 | Nakhon Nayok, Thailand                        |       nan    |
| 4533 | Wuhan, China                                  |       nan    |
| 4534 | Bukan, Iran                                   |       nan    |
| 4535 | Masjed Soleyman, Iran                         |       nan    |
| 4536 | Mohammad Shahr, Iran                          |       nan    |
| 4537 | Monclova, Mexico                              |       nan    |
| 4538 | Tlalnepantla, Mexico                          |       nan    |
| 4539 | Veliko Gradiste, Serbia                       |       nan    |
| 4540 | Khorugh, Tajikistan                           |       nan    |
| 4541 | Chai Nat, Thailand                            |       nan    |
| 4542 | Chanthaburi, Thailand                         |       nan    |
| 4543 | Kantharalak, Thailand                         |       nan    |
| 4544 | Mukdahan, Thailand                            |       nan    |
| 4545 | Phibun Mangsahan, Thailand                    |       nan    |
| 4546 | Jinja, Uganda                                 |       nan    |
| 4547 | Qasr E Shirin, Iran                           |       nan    |
| 4548 | Naucalpan De Juarez, Mexico                   |       nan    |
| 4549 | Qianan, China                                 |       nan    |
| 4550 | Zunhua, China                                 |       nan    |
| 4551 | Hatay, Turkey                                 |       nan    |
| 4552 | Ninh Binh, Vietnam                            |       nan    |
| 4553 | Hpa An, Burma                                 |       nan    |
| 4554 | Savannakhet, Laos                             |       nan    |
| 4555 | Chalco, Mexico                                |       nan    |
| 4556 | Nova Varos, Serbia                            |       nan    |
| 4557 | Khartoum, Sudan                               |       nan    |
| 4558 | Ban Nong Sam Rong, Thailand                   |       nan    |
| 4559 | Khlung, Thailand                              |       nan    |
| 4560 | Amnat Charoen, Thailand                       |       nan    |
| 4561 | Kantang, Thailand                             |       nan    |
| 4562 | Nezahualcoyotl, Mexico                        |       nan    |
| 4563 | San Francisco Del Rincon, Mexico              |       nan    |
| 4564 | Zapopan, Mexico                               |       nan    |
| 4565 | Birnin Kebbi, Nigeria                         |       nan    |
| 4566 | Cotonou, Benin                                |       nan    |
| 4567 | Heihe, China                                  |       nan    |
| 4568 | Mezhdurechensk, Russia                        |       nan    |
| 4569 | Nonthaburi, Thailand                          |       nan    |
| 4570 | Warin Chamrap, Thailand                       |       nan    |
| 4571 | Yasothon, Thailand                            |       nan    |
| 4572 | Brooklyn, United States                       |       nan    |
| 4573 | Vinh Yen, Vietnam                             |       nan    |
| 4574 | Quito, Ecuador                                |       nan    |
| 4575 | Mobarakeh, Iran                               |       nan    |
| 4576 | Shahr E Kord, Iran                            |       nan    |
| 4577 | Yasuj, Iran                                   |       nan    |
| 4578 | Brescia, Italy                                |       nan    |
| 4579 | Apizaco, Mexico                               |       nan    |
| 4580 | Zacatepec, Mexico                             |       nan    |
| 4581 | Uliastay, Mongolia                            |       nan    |
| 4582 | Kaolack, Senegal                              |       nan    |
| 4583 | Chachoengsao, Thailand                        |       nan    |
| 4584 | Song Phi Nong, Thailand                       |       nan    |
| 4585 | Ban Krathum Lom, Thailand                     |       nan    |
| 4586 | Dawei, Burma                                  |       nan    |
| 4587 | Koh Kong, Cambodia                            |       nan    |
| 4588 | Pingquan, China                               |       nan    |
| 4589 | Yreka, United States                          |       nan    |
| 4590 | Ciudad Nezahualcoyotl, Mexico                 |       nan    |
| 4591 | Mexico City, Mexico                           |       nan    |
| 4592 | Poza Rica De Hidalgo, Mexico                  |       nan    |
| 4593 | Sarab, Iran                                   |       nan    |
| 4594 | Luena, Angola                                 |       nan    |
| 4595 | Hanchuan, China                               |       nan    |
| 4596 | Si Sa Ket, Thailand                           |       nan    |
| 4597 | Uthai Thani, Thailand                         |       nan    |
| 4598 | Oroqen Zizhiqi, China                         |       nan    |
| 4599 | Sangolqui, Ecuador                            |       nan    |
| 4600 | Ecatepec, Mexico                              |       nan    |
| 4601 | Dalandzadgad, Mongolia                        |       nan    |
| 4602 | Kovin, Serbia                                 |       nan    |
| 4603 | Det Udom, Thailand                            |       nan    |
| 4604 | Sikhio, Thailand                              |       nan    |
| 4605 | Tha Mai, Thailand                             |       nan    |
| 4606 | Lajkovac, Serbia                              |       nan    |
| 4607 | Ban Na Kham, Thailand                         |       nan    |
| 4608 | Bua Yai, Thailand                             |       nan    |
| 4609 | Narathiwat, Thailand                          |       nan    |
| 4610 | Wang Saphung, Thailand                        |       nan    |
| 4611 | Sosa, Japan                                   |       nan    |
| 4612 | Butuan, Philippines                           |       nan    |
| 4613 | Kumasi, Ghana                                 |       nan    |
| 4614 | Ikeda, Japan                                  |       nan    |
| 4615 | Bar, Montenegro                               |       nan    |
| 4616 | Hodonin, Czechia                              |       nan    |
| 4617 | Odobesti, Romania                             |       nan    |
| 4618 | Kalasin, Thailand                             |       nan    |
| 4619 | Krabi, Thailand                               |       nan    |
| 4620 | Phetchabun, Thailand                          |       nan    |
| 4621 | Ximeicun, China                               |       nan    |
| 4622 | Zhangjiakou Shi Xuanhua Qu, China             |       nan    |
| 4623 | Zhangzhou, China                              |       nan    |
| 4624 | Tabor, Czechia                                |       nan    |
| 4625 | Cannes, France                                |       nan    |
| 4626 | Guatemala City, Guatemala                     |       nan    |
| 4627 | Rasht, Iran                                   |       nan    |
| 4628 | Araba, Israel                                 |       nan    |
| 4629 | Kano, Nigeria                                 |       nan    |
| 4630 | Ishimbay, Russia                              |       nan    |
| 4631 | Ad Dammam, Saudi Arabia                       |       nan    |
| 4632 | Dhahran, Saudi Arabia                         |       nan    |
| 4633 | Maha Sarakham, Thailand                       |       nan    |
| 4634 | Sawankhalok, Thailand                         |       nan    |
| 4635 | Wichian Buri, Thailand                        |       nan    |
| 4636 | Al Hufuf, Saudi Arabia                        |       nan    |
| 4637 | Al Jubayl, Saudi Arabia                       |       nan    |
| 4638 | Al Qatif, Saudi Arabia                        |       nan    |
| 4639 | Phalaborwa, South Africa                      |       nan    |
| 4640 | Ban Na San, Thailand                          |       nan    |
| 4641 | Ban Patong, Thailand                          |       nan    |
| 4642 | Ban Tha Kham, Thailand                        |       nan    |
| 4643 | Zdar Nad Sazavou, Czechia                     |       nan    |
| 4644 | Patra, Greece                                 |       nan    |
| 4645 | Zacatecas, Mexico                             |       nan    |
| 4646 | Buenos Aires, Argentina                       |       nan    |
| 4647 | Bruges, Belgium                               |       nan    |
| 4648 | Brussels, Belgium                             |       nan    |
| 4649 | Diest, Belgium                                |       nan    |
| 4650 | Schaarbeek, Belgium                           |       nan    |
| 4651 | Jiangyin, China                               |       nan    |
| 4652 | Yangshe, China                                |       nan    |
| 4653 | Montrouge, France                             |       nan    |
| 4654 | Marsberg, Germany                             |       nan    |
| 4655 | Moldova Noua, Romania                         |       nan    |
| 4656 | Sfantu Gheorghe, Romania                      |       nan    |
| 4657 | Lapovo, Serbia                                |       nan    |
| 4658 | Takua Pa, Thailand                            |       nan    |
| 4659 | Highland Heights, United States               |       nan    |
| 4660 | Reidsville, United States                     |       nan    |
| 4661 | Owensboro, United States                      |       nan    |
| 4662 | Anderlecht, Belgium                           |       nan    |
| 4663 | Antoing, Belgium                              |       nan    |
| 4664 | Landen, Belgium                               |       nan    |
| 4665 | Tessenderlo, Belgium                          |       nan    |
| 4666 | Veurne, Belgium                               |       nan    |
| 4667 | Kaminokawa, Japan                             |       nan    |
| 4668 | Mooka, Japan                                  |       nan    |
| 4669 | Motosu, Japan                                 |       nan    |
| 4670 | Sano, Japan                                   |       nan    |
| 4671 | Kisumu, Kenya                                 |       nan    |
| 4672 | San Luis De La Paz, Mexico                    |       nan    |
| 4673 | San Miguel De Allende, Mexico                 |       nan    |
| 4674 | Saynshand, Mongolia                           |       nan    |
| 4675 | Poznan, Poland                                |       nan    |
| 4676 | Korkino, Russia                               |       nan    |
| 4677 | Isfara, Tajikistan                            |       nan    |
| 4678 | Farmingville, United States                   |       nan    |
| 4679 | Ziguinchor, Senegal                           |       nan    |
| 4680 | Potchefstroom, South Africa                   |       nan    |
| 4681 | Buri Ram, Thailand                            |       nan    |
| 4682 | Ko Samui, Thailand                            |       nan    |
| 4683 | Ranong, Thailand                              |       nan    |
| 4684 | Bastogne, Belgium                             |       nan    |
| 4685 | Hasselt, Belgium                              |       nan    |
| 4686 | Mons, Belgium                                 |       nan    |
| 4687 | Devnya, Bulgaria                              |       nan    |
| 4688 | Changshu, China                               |       nan    |
| 4689 | Ginowan, Japan                                |       nan    |
| 4690 | Shimotsuke, Japan                             |       nan    |
| 4691 | Tochigi, Japan                                |       nan    |
| 4692 | Atbasar, Kazakhstan                           |       nan    |
| 4693 | Sa'in Qal`eh, Iran                            |       nan    |
| 4694 | Kanuma, Japan                                 |       nan    |
| 4695 | Yaita, Japan                                  |       nan    |
| 4696 | Gjakove, Kosovo                               |       nan    |
| 4697 | Choyr, Mongolia                               |       nan    |
| 4698 | Batac, Philippines                            |       nan    |
| 4699 | Kabul, Afghanistan                            |       nan    |
| 4700 | Andenne, Belgium                              |       nan    |
| 4701 | Couvin, Belgium                               |       nan    |
| 4702 | Gent, Belgium                                 |       nan    |
| 4703 | Hotton, Belgium                               |       nan    |
| 4704 | Neufchateau, Belgium                          |       nan    |
| 4705 | Chengguan, China                              |       nan    |
| 4706 | Jurong, China                                 |       nan    |
| 4707 | Benesov, Czechia                              |       nan    |
| 4708 | Talmaciu, Romania                             |       nan    |
| 4709 | Ban Phai, Thailand                            |       nan    |
| 4710 | Ban Thum, Thailand                            |       nan    |
| 4711 | Songkhla, Thailand                            |       nan    |
| 4712 | Pidhorodne, Ukraine                           |       nan    |
| 4713 | Rohatyn, Ukraine                              |       nan    |
| 4714 | Morriston, United Kingdom                     |       nan    |
| 4715 | Corning, United States                        |       nan    |
| 4716 | Gardendale, United States                     |       nan    |
| 4717 | Phenix City, United States                    |       nan    |
| 4718 | Northridge, United States                     |       nan    |
| 4719 | Tra Vinh, Vietnam                             |       nan    |
| 4720 | Arlon, Belgium                                |       nan    |
| 4721 | Harelbeke, Belgium                            |       nan    |
| 4722 | Menen, Belgium                                |       nan    |
| 4723 | Namur, Belgium                                |       nan    |
| 4724 | Roeselare, Belgium                            |       nan    |
| 4725 | Laibin, China                                 |       nan    |
| 4726 | Qitai, China                                  |       nan    |
| 4727 | Ardabil, Iran                                 |       nan    |
| 4728 | Salmas, Iran                                  |       nan    |
| 4729 | Nikko, Japan                                  |       nan    |
| 4730 | Toledo, Philippines                           |       nan    |
| 4731 | Targu Mures, Romania                          |       nan    |
| 4732 | Slobodskoy, Russia                            |       nan    |
| 4733 | Sam Phran, Thailand                           |       nan    |
| 4734 | Tororo, Uganda                                |       nan    |
| 4735 | Khmil'nyk, Ukraine                            |       nan    |
| 4736 | Radomyshl, Ukraine                            |       nan    |
| 4737 | Tul'chyn, Ukraine                             |       nan    |
| 4738 | Magas, Russia                                 |       nan    |
| 4739 | East London, South Africa                     |       nan    |
| 4740 | George, South Africa                          |       nan    |
| 4741 | Skelleftea, Sweden                            |       nan    |
| 4742 | Bang Mun Nak, Thailand                        |       nan    |
| 4743 | Chumphon, Thailand                            |       nan    |
| 4744 | Kolomyya, Ukraine                             |       nan    |
| 4745 | Stanmore, United Kingdom                      |       nan    |
| 4746 | Liege, Belgium                                |       nan    |
| 4747 | Seraing, Belgium                              |       nan    |
| 4748 | Chengjiao, China                              |       nan    |
| 4749 | Marand, Iran                                  |       nan    |
| 4750 | Nasukarasuyama, Japan                         |       nan    |
| 4751 | Utsunomiya, Japan                             |       nan    |
| 4752 | Tokoroa, New Zealand                          |       nan    |
| 4753 | Shakargarh, Pakistan                          |       nan    |
| 4754 | Alaminos, Philippines                         |       nan    |
| 4755 | Lodwar, Kenya                                 |       nan    |
| 4756 | Vushtrri, Kosovo                              |       nan    |
| 4757 | Tulsipur, Nepal                               |       nan    |
| 4758 | Makati City, Philippines                      |       nan    |
| 4759 | Lokeren, Belgium                              |       nan    |
| 4760 | Mortsel, Belgium                              |       nan    |
| 4761 | Sint Niklaas, Belgium                         |       nan    |
| 4762 | Stavelot, Belgium                             |       nan    |
| 4763 | North Battleford, Canada                      |       nan    |
| 4764 | Lanxi, China                                  |       nan    |
| 4765 | Xinhualu, China                               |       nan    |
| 4766 | Mont De Marsan, France                        |       nan    |
| 4767 | Kanifing, Gambia                              |       nan    |
| 4768 | Kemerovo, Russia                              |       nan    |
| 4769 | Novosibirsk, Russia                           |       nan    |
| 4770 | Pak Thong Chai, Thailand                      |       nan    |
| 4771 | Marmaris, Turkey                              |       nan    |
| 4772 | Sloviansk, Ukraine                            |       nan    |
| 4773 | Aspen, United States                          |       nan    |
| 4774 | Tarrant, United States                        |       nan    |
| 4775 | Williamston, United States                    |       nan    |
| 4776 | Huambo, Angola                                |       nan    |
| 4777 | Herentals, Belgium                            |       nan    |
| 4778 | Mechelen, Belgium                             |       nan    |
| 4779 | Saskatoon, Canada                             |       nan    |
| 4780 | Licheng, China                                |       nan    |
| 4781 | Sukabumi, Indonesia                           |       nan    |
| 4782 | Kefar Sava, Israel                            |       nan    |
| 4783 | Merida, Mexico                                |       nan    |
| 4784 | Taupo, New Zealand                            |       nan    |
| 4785 | Horezu, Romania                               |       nan    |
| 4786 | Ob', Russia                                   |       nan    |
| 4787 | Ul'yanovsk, Russia                            |       nan    |
| 4788 | Krathum Baen, Thailand                        |       nan    |
| 4789 | Bobrynets', Ukraine                           |       nan    |
| 4790 | Vaslui, Romania                               |       nan    |
| 4791 | Segezha, Russia                               |       nan    |
| 4792 | Osecina, Serbia                               |       nan    |
| 4793 | Lebowakgomo, South Africa                     |       nan    |
| 4794 | Phangnga, Thailand                            |       nan    |
| 4795 | Surin, Thailand                               |       nan    |
| 4796 | Kamianske, Ukraine                            |       nan    |
| 4797 | Kosiv, Ukraine                                |       nan    |
| 4798 | Pavlohrad, Ukraine                            |       nan    |
| 4799 | Zhovkva, Ukraine                              |       nan    |
| 4800 | Berkeley, United States                       |       nan    |
| 4801 | Spitak, Armenia                               |       nan    |
| 4802 | Kaifeng Chengguanzhen, China                  |       nan    |
| 4803 | Qingping, China                               |       nan    |
| 4804 | Taozhou, China                                |       nan    |
| 4805 | Yicheng, China                                |       nan    |
| 4806 | Liberty Lake, United States                   |       nan    |
| 4807 | Nashville, United States                      |       nan    |
| 4808 | Dong Hoi, Vietnam                             |       nan    |
| 4809 | Nha Trang, Vietnam                            |       nan    |
| 4810 | Benevento, Italy                              |       nan    |
| 4811 | Mosgiel, New Zealand                          |       nan    |
| 4812 | Gjovik, Norway                                |       nan    |
| 4813 | Poso, Indonesia                               |       nan    |
| 4814 | Qiryat Shemona, Israel                        |       nan    |
| 4815 | Varese, Italy                                 |       nan    |
| 4816 | Chikusei, Japan                               |       nan    |
| 4817 | Yamaga, Japan                                 |       nan    |
| 4818 | Carnikava, Latvia                             |       nan    |
| 4819 | Te Awamutu, New Zealand                       |       nan    |
| 4820 | Luanda, Angola                                |       nan    |
| 4821 | Praia, Cabo Verde                             |       nan    |
| 4822 | Fuyang, China                                 |       nan    |
| 4823 | Hotan, China                                  |       nan    |
| 4824 | Yongcheng, China                              |       nan    |
| 4825 | Zhumadian, China                              |       nan    |
| 4826 | Pamplona, Colombia                            |       nan    |
| 4827 | Vila Nova De Gaia, Portugal                   |       nan    |
| 4828 | Sangeorz Bai, Romania                         |       nan    |
| 4829 | Zarnesti, Romania                             |       nan    |
| 4830 | Elektrostal', Russia                          |       nan    |
| 4831 | Roi Et, Thailand                              |       nan    |
| 4832 | Laventille, Trinidad And Tobago               |       nan    |
| 4833 | Tolleson, United States                       |       nan    |
| 4834 | Hue, Vietnam                                  |       nan    |
| 4835 | Hidden Valley Lake, United States             |       nan    |
| 4836 | Paradise, United States                       |       nan    |
| 4837 | Susanville, United States                     |       nan    |
| 4838 | Jiangshan, China                              |       nan    |
| 4839 | Shuizhai, China                               |       nan    |
| 4840 | Kinshasa, Congo (Kinshasa)                    |       nan    |
| 4841 | Afula, Israel                                 |       nan    |
| 4842 | Toamasina, Madagascar                         |       nan    |
| 4843 | Itahari, Nepal                                |       nan    |
| 4844 | Northcote, New Zealand                        |       nan    |
| 4845 | Lucena, Philippines                           |       nan    |
| 4846 | Si Satchanalai, Thailand                      |       nan    |
| 4847 | Horley, United Kingdom                        |       nan    |
| 4848 | Spitalfields, United Kingdom                  |       nan    |
| 4849 | Crescent City, United States                  |       nan    |
| 4850 | Berdsk, Russia                                |       nan    |
| 4851 | Iskitim, Russia                               |       nan    |
| 4852 | Masaka, Uganda                                |       nan    |
| 4853 | Polegate, United Kingdom                      |       nan    |
| 4854 | East Peoria, United States                    |       nan    |
| 4855 | Danjiangkou, China                            |       nan    |
| 4856 | Huazhou, China                                |       nan    |
| 4857 | Yueqing, China                                |       nan    |
| 4858 | Santa Ana, Costa Rica                         |       nan    |
| 4859 | Hung Yen, Vietnam                             |       nan    |
| 4860 | Caserta, Italy                                |       nan    |
| 4861 | Pinki, Latvia                                 |       nan    |
| 4862 | Pokhara, Nepal                                |       nan    |
| 4863 | Gibraltar, Gibraltar                          |       nan    |
| 4864 | Kalamata, Greece                              |       nan    |
| 4865 | Karmi'el, Israel                              |       nan    |
| 4866 | Ferrara, Italy                                |       nan    |
| 4867 | Giugliano In Campania, Italy                  |       nan    |
| 4868 | Modena, Italy                                 |       nan    |
| 4869 | Olbia, Italy                                  |       nan    |
| 4870 | Ravenna, Italy                                |       nan    |
| 4871 | Olaine, Latvia                                |       nan    |
| 4872 | Ulaangom, Mongolia                            |       nan    |
| 4873 | Cambridge, New Zealand                        |       nan    |
| 4874 | Jedlicze, Poland                              |       nan    |
| 4875 | Lubango, Angola                               |       nan    |
| 4876 | Salihorsk, Belarus                            |       nan    |
| 4877 | Eupen, Belgium                                |       nan    |
| 4878 | Vilvoorde, Belgium                            |       nan    |
| 4879 | Sao Filipe, Cabo Verde                        |       nan    |
| 4880 | Wutong, China                                 |       nan    |
| 4881 | Zhuji, China                                  |       nan    |
| 4882 | Sint Michiel, Curacao                         |       nan    |
| 4883 | Kerpen, Germany                               |       nan    |
| 4884 | Sandomierz, Poland                            |       nan    |
| 4885 | Ponte De Lima, Portugal                       |       nan    |
| 4886 | Satu Mare, Romania                            |       nan    |
| 4887 | Pietermaritzburg, South Africa                |       nan    |
| 4888 | Ban Chang, Thailand                           |       nan    |
| 4889 | Nova Kakhovka, Ukraine                        |       nan    |
| 4890 | Marvin, United States                         |       nan    |
| 4891 | Lakewood, United States                       |       nan    |
| 4892 | Nampa, United States                          |       nan    |
| 4893 | Upland, United States                         |       nan    |
| 4894 | Hrodna, Belarus                               |       nan    |
| 4895 | Sal Rei, Cabo Verde                           |       nan    |
| 4896 | Shanhu, China                                 |       nan    |
| 4897 | Wenling, China                                |       nan    |
| 4898 | Xiashi, China                                 |       nan    |
| 4899 | Yiwu, China                                   |       nan    |
| 4900 | Zhugang, China                                |       nan    |
| 4901 | Puteaux, France                               |       nan    |
| 4902 | Rimini, Italy                                 |       nan    |
| 4903 | Thames, New Zealand                           |       nan    |
| 4904 | Fundulea, Romania                             |       nan    |
| 4905 | Turnu Magurele, Romania                       |       nan    |
| 4906 | Abinsk, Russia                                |       nan    |
| 4907 | Anapa, Russia                                 |       nan    |
| 4908 | Nogliki, Russia                               |       nan    |
| 4909 | Okha, Russia                                  |       nan    |
| 4910 | Yeysk, Russia                                 |       nan    |
| 4911 | Buchs, Switzerland                            |       nan    |
| 4912 | Chaiyaphum, Thailand                          |       nan    |
| 4913 | Pathum Thani, Thailand                        |       nan    |
| 4914 | Bilhorod Dnistrovs'kyy, Ukraine               |       nan    |
| 4915 | Poltava, Ukraine                              |       nan    |
| 4916 | Milanowek, Poland                             |       nan    |
| 4917 | Ustka, Poland                                 |       nan    |
| 4918 | Draganesti Olt, Romania                       |       nan    |
| 4919 | Uricani, Romania                              |       nan    |
| 4920 | Kurganinsk, Russia                            |       nan    |
| 4921 | Magnitogorsk, Russia                          |       nan    |
| 4922 | Nadym, Russia                                 |       nan    |
| 4923 | Novokuznetsk, Russia                          |       nan    |
| 4924 | Cha am, Thailand                              |       nan    |
| 4925 | Sambir, Ukraine                               |       nan    |
| 4926 | Caseros, Argentina                            |       nan    |
| 4927 | Oberwart, Austria                             |       nan    |
| 4928 | Espargos, Cabo Verde                          |       nan    |
| 4929 | Mindelo, Cabo Verde                           |       nan    |
| 4930 | Baisha, China                                 |       nan    |
| 4931 | Dongyang, China                               |       nan    |
| 4932 | Zaoyang, China                                |       nan    |
| 4933 | Medford, United States                        |       nan    |
| 4934 | Luanshya, Zambia                              |       nan    |
| 4935 | Bologna, Italy                                |       nan    |
| 4936 | Piacenza, Italy                               |       nan    |
| 4937 | Pisa, Italy                                   |       nan    |
| 4938 | Priverno, Italy                               |       nan    |
| 4939 | Kasama, Japan                                 |       nan    |
| 4940 | Dharan, Nepal                                 |       nan    |
| 4941 | Manukau City, New Zealand                     |       nan    |
| 4942 | Masterton, New Zealand                        |       nan    |
| 4943 | Olongapo, Philippines                         |       nan    |
| 4944 | Florence, Italy                               |       nan    |
| 4945 | Forli, Italy                                  |       nan    |
| 4946 | Rome, Italy                                   |       nan    |
| 4947 | Verona, Italy                                 |       nan    |
| 4948 | Svencionys, Lithuania                         |       nan    |
| 4949 | Heroica Matamoros, Mexico                     |       nan    |
| 4950 | Herceg Novi, Montenegro                       |       nan    |
| 4951 | Lower Hutt, New Zealand                       |       nan    |
| 4952 | Upper Hutt, New Zealand                       |       nan    |
| 4953 | Wellington, New Zealand                       |       nan    |
| 4954 | Konstancin Jeziorna, Poland                   |       nan    |
| 4955 | Godoy Cruz, Argentina                         |       nan    |
| 4956 | Iguacu, Brazil                                |       nan    |
| 4957 | Rio de Janeiro, Brazil                        |       nan    |
| 4958 | Vila Velha, Brazil                            |       nan    |
| 4959 | Porto Novo, Cabo Verde                        |       nan    |
| 4960 | Guli, China                                   |       nan    |
| 4961 | Linxia Chengguanzhen, China                   |       nan    |
| 4962 | Catano, Puerto Rico                           |       nan    |
| 4963 | Tulcea, Romania                               |       nan    |
| 4964 | Aleksandrovsk Sakhalinskiy, Russia            |       nan    |
| 4965 | Kumertau, Russia                              |       nan    |
| 4966 | Primorsko Akhtarsk, Russia                    |       nan    |
| 4967 | Zhigulevsk, Russia                            |       nan    |
| 4968 | Becej, Serbia                                 |       nan    |
| 4969 | Sombor, Serbia                                |       nan    |
| 4970 | Sa Kaeo, Thailand                             |       nan    |
| 4971 | Sadao, Thailand                               |       nan    |
| 4972 | Wang Nam Yen, Thailand                        |       nan    |
| 4973 | Uman, Ukraine                                 |       nan    |
| 4974 | Tottenham, United Kingdom                     |       nan    |
| 4975 | Cloverdale, United States                     |       nan    |
| 4976 | Gunnison, United States                       |       nan    |
| 4977 | Idaho Falls, United States                    |       nan    |
| 4978 | Selah, United States                          |       nan    |
| 4979 | Yosemite Lakes, United States                 |       nan    |
| 4980 | Placerville, United States                    |       nan    |
| 4981 | Raytown, United States                        |       nan    |
| 4982 | Visalia, United States                        |       nan    |
| 4983 | Benguela, Angola                              |       nan    |
| 4984 | Corowa, Australia                             |       nan    |
| 4985 | Nouna, Burkina Faso                           |       nan    |
| 4986 | Dingxi, China                                 |       nan    |
| 4987 | Lucheng, China                                |       nan    |
| 4988 | Koforidua, Ghana                              |       nan    |
| 4989 | Xanthi, Greece                                |       nan    |
| 4990 | Szeged, Hungary                               |       nan    |
| 4991 | Mojokerto, Indonesia                          |       nan    |
| 4992 | Khomeyni Shahr, Iran                          |       nan    |
| 4993 | Parma, Italy                                  |       nan    |
| 4994 | Reggio Emilia, Italy                          |       nan    |
| 4995 | Kiambu, Kenya                                 |       nan    |
| 4996 | Sigulda, Latvia                               |       nan    |
| 4997 | Ciudad Lerdo, Mexico                          |       nan    |
| 4998 | Walcz, Poland                                 |       nan    |
| 4999 | Deva, Romania                                 |       nan    |
| 5000 | Zalau, Romania                                |       nan    |
| 5001 | Izhevsk, Russia                               |       nan    |
| 5002 | Kommunar, Russia                              |       nan    |
| 5003 | Krymsk, Russia                                |       nan    |
| 5004 | Pak Phanang, Thailand                         |       nan    |
| 5005 | Fethiye, Turkey                               |       nan    |
| 5006 | Bududa, Uganda                                |       nan    |
| 5007 | Baranivka, Ukraine                            |       nan    |
| 5008 | Drohobych, Ukraine                            |       nan    |
| 5009 | Fortuna, United States                        |       nan    |
| 5010 | Gallup, United States                         |       nan    |
| 5011 | Opole, Poland                                 |       nan    |
| 5012 | Przemysl, Poland                              |       nan    |
| 5013 | Starogard Gdanski, Poland                     |       nan    |
| 5014 | Goryachiy Klyuch, Russia                      |       nan    |
| 5015 | Tuapse, Russia                                |       nan    |
| 5016 | Acquaviva, San Marino                         |       nan    |
| 5017 | Al Qurayyat, Saudi Arabia                     |       nan    |
| 5018 | Mecca, Saudi Arabia                           |       nan    |
| 5019 | Kanal, Slovenia                               |       nan    |
| 5020 | Miren, Slovenia                               |       nan    |
| 5021 | Yatagan, Turkey                               |       nan    |
| 5022 | Kremenets', Ukraine                           |       nan    |
| 5023 | Cosham, United Kingdom                        |       nan    |
| 5024 | Harahan, United States                        |       nan    |
| 5025 | Byaroza, Belarus                              |       nan    |
| 5026 | Niteroi, Brazil                               |       nan    |
| 5027 | Powell River, Canada                          |       nan    |
| 5028 | Longquan, China                               |       nan    |
| 5029 | Mohelnice, Czechia                            |       nan    |
| 5030 | Hyeres, France                                |       nan    |
| 5031 | Quimper, France                               |       nan    |
| 5032 | Sens, France                                  |       nan    |
| 5033 | Vail, United States                           |       nan    |
| 5034 | Can Tho, Vietnam                              |       nan    |
| 5035 | Psachna, Greece                               |       nan    |
| 5036 | Encs, Hungary                                 |       nan    |
| 5037 | Gyor, Hungary                                 |       nan    |
| 5038 | Kazincbarcika, Hungary                        |       nan    |
| 5039 | Putnok, Hungary                               |       nan    |
| 5040 | Sajoszentpeter, Hungary                       |       nan    |
| 5041 | Salgotarjan, Hungary                          |       nan    |
| 5042 | Tiszaujvaros, Hungary                         |       nan    |
| 5043 | Najafabad, Iran                               |       nan    |
| 5044 | Kildare, Ireland                              |       nan    |
| 5045 | Amelia, Italy                                 |       nan    |
| 5046 | Eraclea, Italy                                |       nan    |
| 5047 | Gorizia, Italy                                |       nan    |
| 5048 | Latina, Italy                                 |       nan    |
| 5049 | Livorno, Italy                                |       nan    |
| 5050 | Udine, Italy                                  |       nan    |
| 5051 | Chrzanow, Poland                              |       nan    |
| 5052 | Kalisz, Poland                                |       nan    |
| 5053 | Ajka, Hungary                                 |       nan    |
| 5054 | Budakeszi, Hungary                            |       nan    |
| 5055 | Budaors, Hungary                              |       nan    |
| 5056 | Budapest, Hungary                             |       nan    |
| 5057 | Dorog, Hungary                                |       nan    |
| 5058 | Dunaharaszti, Hungary                         |       nan    |
| 5059 | Dunakeszi, Hungary                            |       nan    |
| 5060 | Dunaujvaros, Hungary                          |       nan    |
| 5061 | Eger, Hungary                                 |       nan    |
| 5062 | Esztergom, Hungary                            |       nan    |
| 5063 | Fot, Hungary                                  |       nan    |
| 5064 | Gyal, Hungary                                 |       nan    |
| 5065 | Kecskemet, Hungary                            |       nan    |
| 5066 | Kerekegyhaza, Hungary                         |       nan    |
| 5067 | Miskolc, Hungary                              |       nan    |
| 5068 | Szazhalombatta, Hungary                       |       nan    |
| 5069 | Szekesfehervar, Hungary                       |       nan    |
| 5070 | Szolnok, Hungary                              |       nan    |
| 5071 | Tatabanya, Hungary                            |       nan    |
| 5072 | Vac, Hungary                                  |       nan    |
| 5073 | Kashan, Iran                                  |       nan    |
| 5074 | Tirat Karmel, Israel                          |       nan    |
| 5075 | Trieste, Italy                                |       nan    |
| 5076 | Meycauayan, Philippines                       |       nan    |
| 5077 | Jesus Nazareno, Argentina                     |       nan    |
| 5078 | Andamooka, Australia                          |       nan    |
| 5079 | Fuan, China                                   |       nan    |
| 5080 | Luocheng, China                               |       nan    |
| 5081 | Macheng, China                                |       nan    |
| 5082 | Ruian, China                                  |       nan    |
| 5083 | Broumov, Czechia                              |       nan    |
| 5084 | Lovosice, Czechia                             |       nan    |
| 5085 | Vejle, Denmark                                |       nan    |
| 5086 | Cuenca, Ecuador                               |       nan    |
| 5087 | Mons En Baroeul, France                       |       nan    |
| 5088 | Saint Jean De Braye, France                   |       nan    |
| 5089 | Kutaisi, Georgia                              |       nan    |
| 5090 | Nowy Targ, Poland                             |       nan    |
| 5091 | Pilawa Gorna, Poland                          |       nan    |
| 5092 | Ceiba, Puerto Rico                            |       nan    |
| 5093 | Zlatna, Romania                               |       nan    |
| 5094 | Guryevsk, Russia                              |       nan    |
| 5095 | Kaliningrad, Russia                           |       nan    |
| 5096 | Kargopol', Russia                             |       nan    |
| 5097 | Kirishi, Russia                               |       nan    |
| 5098 | Samara, Russia                                |       nan    |
| 5099 | Tarko Sale, Russia                            |       nan    |
| 5100 | Serravalle, San Marino                        |       nan    |
| 5101 | Yanbu, Saudi Arabia                           |       nan    |
| 5102 | Medzilaborce, Slovakia                        |       nan    |
| 5103 | Scarborough, Trinidad And Tobago              |       nan    |
| 5104 | Bakhmut, Ukraine                              |       nan    |
| 5105 | Mariupol, Ukraine                             |       nan    |
| 5106 | Antioch, United States                        |       nan    |
| 5107 | Corvallis, United States                      |       nan    |
| 5108 | Long Beach, United States                     |       nan    |
| 5109 | Mission, United States                        |       nan    |
| 5110 | Oroville, United States                       |       nan    |
| 5111 | Roseburg, United States                       |       nan    |
| 5112 | Signal Hill, United States                    |       nan    |
| 5113 | South Hill, United States                     |       nan    |
| 5114 | St Helena, United States                      |       nan    |
| 5115 | Winters, United States                        |       nan    |
| 5116 | Quy Nhon, Vietnam                             |       nan    |
| 5117 | Ocean Shores, United States                   |       nan    |
| 5118 | Orland, United States                         |       nan    |
| 5119 | San Luis Obispo, United States                |       nan    |
| 5120 | Sandersville, United States                   |       nan    |
| 5121 | Santa Maria, United States                    |       nan    |
| 5122 | Sheffield Lake, United States                 |       nan    |
| 5123 | Shorewood, United States                      |       nan    |
| 5124 | Sioux Falls, United States                    |       nan    |
| 5125 | Wapato, United States                         |       nan    |
| 5126 | Warrensville Heights, United States           |       nan    |
| 5127 | Wright, United States                         |       nan    |
| 5128 | Son Tay, Vietnam                              |       nan    |
| 5129 | Mendoza, Argentina                            |       nan    |
| 5130 | Healesville, Australia                        |       nan    |
| 5131 | Kiama Downs, Australia                        |       nan    |
| 5132 | Port Augusta, Australia                       |       nan    |
| 5133 | Sankt Veit An Der Glan, Austria               |       nan    |
| 5134 | Navapolatsk, Belarus                          |       nan    |
| 5135 | Svyetlahorsk, Belarus                         |       nan    |
| 5136 | Canela, Brazil                                |       nan    |
| 5137 | Beidao, China                                 |       nan    |
| 5138 | Fangting, China                               |       nan    |
| 5139 | Fuding, China                                 |       nan    |
| 5140 | Golmud, China                                 |       nan    |
| 5141 | Qincheng, China                               |       nan    |
| 5142 | Puerto Baquerizo Moreno, Ecuador              |       nan    |
| 5143 | Montauban, France                             |       nan    |
| 5144 | Villeurbanne, France                          |       nan    |
| 5145 | Gladbeck, Germany                             |       nan    |
| 5146 | Debrecen, Hungary                             |       nan    |
| 5147 | Kapuvar, Hungary                              |       nan    |
| 5148 | Mosonmagyarovar, Hungary                      |       nan    |
| 5149 | Nyiregyhaza, Hungary                          |       nan    |
| 5150 | Pecs, Hungary                                 |       nan    |
| 5151 | Szentgotthard, Hungary                        |       nan    |
| 5152 | Szombathely, Hungary                          |       nan    |
| 5153 | Varpalota, Hungary                            |       nan    |
| 5154 | Veszprem, Hungary                             |       nan    |
| 5155 | Arezzo, Italy                                 |       nan    |
| 5156 | Siena, Italy                                  |       nan    |
| 5157 | Terni, Italy                                  |       nan    |
| 5158 | Ashiya, Japan                                 |       nan    |
| 5159 | Katsuura, Japan                               |       nan    |
| 5160 | Kitaku, Japan                                 |       nan    |
| 5161 | Nakama, Japan                                 |       nan    |
| 5162 | Okayama, Japan                                |       nan    |
| 5163 | Susaki, Japan                                 |       nan    |
| 5164 | Yashiki, Japan                                |       nan    |
| 5165 | Tula De Allende, Mexico                       |       nan    |
| 5166 | Bender, Moldova                               |       nan    |
| 5167 | The Bottom, Netherlands                       |       nan    |
| 5168 | Levanger, Norway                              |       nan    |
| 5169 | Iligan, Philippines                           |       nan    |
| 5170 | Urdaneta, Philippines                         |       nan    |
| 5171 | Alesd, Romania                                |       nan    |
| 5172 | Bratsk, Russia                                |       nan    |
| 5173 | Saratov, Russia                               |       nan    |
| 5174 | Chiesanuova, San Marino                       |       nan    |
| 5175 | Gelnica, Slovakia                             |       nan    |
| 5176 | Volksrust, South Africa                       |       nan    |
| 5177 | Weinfelden, Switzerland                       |       nan    |
| 5178 | Kathu, Thailand                               |       nan    |
| 5179 | Heniches'k, Ukraine                           |       nan    |
| 5180 | Horlivka, Ukraine                             |       nan    |
| 5181 | Kramatorsk, Ukraine                           |       nan    |
| 5182 | Oster, Ukraine                                |       nan    |
| 5183 | Rivne, Ukraine                                |       nan    |
| 5184 | Snovsk, Ukraine                               |       nan    |
| 5185 | Tetiyiv, Ukraine                              |       nan    |
| 5186 | Yuzhne, Ukraine                               |       nan    |
| 5187 | Bangor, United Kingdom                        |       nan    |
| 5188 | Llangefni, United Kingdom                     |       nan    |
| 5189 | Olton, United Kingdom                         |       nan    |
| 5190 | Penarth, United Kingdom                       |       nan    |
| 5191 | August, United States                         |       nan    |
| 5192 | Boise, United States                          |       nan    |
| 5193 | Carbondale, United States                     |       nan    |
| 5194 | Eureka, United States                         |       nan    |
| 5195 | Half Moon Bay, United States                  |       nan    |
| 5196 | Healdsburg, United States                     |       nan    |
| 5197 | Henderson, United States                      |       nan    |
| 5198 | Calarasi, Romania                             |       nan    |
| 5199 | Iernut, Romania                               |       nan    |
| 5200 | Ludus, Romania                                |       nan    |
| 5201 | Slobozia, Romania                             |       nan    |
| 5202 | Aniva, Russia                                 |       nan    |
| 5203 | Arkhangel'sk, Russia                          |       nan    |
| 5204 | Blagoveshchensk, Russia                       |       nan    |
| 5205 | Chekhov, Russia                               |       nan    |
| 5206 | Dzerzhinsk, Russia                            |       nan    |
| 5207 | Korsakov, Russia                              |       nan    |
| 5208 | Kstovo, Russia                                |       nan    |
| 5209 | Makarov, Russia                               |       nan    |
| 5210 | Poronaysk, Russia                             |       nan    |
| 5211 | Sochi, Russia                                 |       nan    |
| 5212 | Uglegorsk, Russia                             |       nan    |
| 5213 | Voronezh, Russia                              |       nan    |
| 5214 | Yakutsk, Russia                               |       nan    |
| 5215 | Zhirnovsk, Russia                             |       nan    |
| 5216 | Faetano, San Marino                           |       nan    |
| 5217 | Al Wajh, Saudi Arabia                         |       nan    |
| 5218 | At Ta'if, Saudi Arabia                        |       nan    |
| 5219 | Medina, Saudi Arabia                          |       nan    |
| 5220 | Ubombo, South Africa                          |       nan    |
| 5221 | Fastiv, Ukraine                               |       nan    |
| 5222 | Kalush, Ukraine                               |       nan    |
| 5223 | Shepetivka, Ukraine                           |       nan    |
| 5224 | Vil'nohirs'k, Ukraine                         |       nan    |
| 5225 | Carlisle, United Kingdom                      |       nan    |
| 5226 | Cumbernauld, United Kingdom                   |       nan    |
| 5227 | Cwmbran, United Kingdom                       |       nan    |
| 5228 | Downham Market, United Kingdom                |       nan    |
| 5229 | Kings Lynn, United Kingdom                    |       nan    |
| 5230 | Paisley, United Kingdom                       |       nan    |
| 5231 | Pontypridd, United Kingdom                    |       nan    |
| 5232 | Renfrew, United Kingdom                       |       nan    |
| 5233 | Baltimore, United States                      |       nan    |
| 5234 | Bartlesville, United States                   |       nan    |
| 5235 | Carpinteria, United States                    |       nan    |
| 5236 | Derby, United States                          |       nan    |
| 5237 | Evanston, United States                       |       nan    |
| 5238 | Fort Wayne, United States                     |       nan    |
| 5239 | French Valley, United States                  |       nan    |
| 5240 | Fruita, United States                         |       nan    |
| 5241 | Glenwood Springs, United States               |       nan    |
| 5242 | Globe, United States                          |       nan    |
| 5243 | Green River, United States                    |       nan    |
| 5244 | Bahia Blanca, Argentina                       |       nan    |
| 5245 | Batemans Bay, Australia                       |       nan    |
| 5246 | Chinchilla, Australia                         |       nan    |
| 5247 | Katoomba, Australia                           |       nan    |
| 5248 | Ulladulla, Australia                          |       nan    |
| 5249 | Wollert, Australia                            |       nan    |
| 5250 | Traismauer, Austria                           |       nan    |
| 5251 | Louvain La Neuve, Belgium                     |       nan    |
| 5252 | Vitoria, Brazil                               |       nan    |
| 5253 | Petawawa, Canada                              |       nan    |
| 5254 | Quesnel, Canada                               |       nan    |
| 5255 | Saint Raymond, Canada                         |       nan    |
| 5256 | Sault Ste. Marie, Canada                      |       nan    |
| 5257 | Korla, China                                  |       nan    |
| 5258 | Rongwo, China                                 |       nan    |
| 5259 | Zhangye, China                                |       nan    |
| 5260 | Aalborg, Denmark                              |       nan    |
| 5261 | Rakvere, Estonia                              |       nan    |
| 5262 | Beaune, France                                |       nan    |
| 5263 | Boulogne Billancourt, France                  |       nan    |
| 5264 | Herouville Saint Clair, France                |       nan    |
| 5265 | Mantes la Ville, France                       |       nan    |
| 5266 | Montereau Faut Yonne, France                  |       nan    |
| 5267 | Glauchau, Germany                             |       nan    |
| 5268 | Ingolstadt, Germany                           |       nan    |
| 5269 | Oschatz, Germany                              |       nan    |
| 5270 | Hood River, United States                     |       nan    |
| 5271 | Kihei, United States                          |       nan    |
| 5272 | Lakeport, United States                       |       nan    |
| 5273 | Lakeview, United States                       |       nan    |
| 5274 | Live Oak, United States                       |       nan    |
| 5275 | Maysville, United States                      |       nan    |
| 5276 | Napa, United States                           |       nan    |
| 5277 | Newark, United States                         |       nan    |
| 5278 | Paducah, United States                        |       nan    |
| 5279 | Pine Manor, United States                     |       nan    |
| 5280 | Salton City, United States                    |       nan    |
| 5281 | Seven Oaks, United States                     |       nan    |
| 5282 | Sheridan, United States                       |       nan    |
| 5283 | Sonora, United States                         |       nan    |
| 5284 | Valdosta, United States                       |       nan    |
| 5285 | Vermillion, United States                     |       nan    |
| 5286 | Willits, United States                        |       nan    |
| 5287 | Youngstown, United States                     |       nan    |
| 5288 | Grafarvogur, Iceland                          |       nan    |
| 5289 | Selfoss, Iceland                              |       nan    |
| 5290 | Bonab, Iran                                   |       nan    |
| 5291 | Sligo, Ireland                                |       nan    |
| 5292 | Bergamo, Italy                                |       nan    |
| 5293 | Busto Arsizio, Italy                          |       nan    |
| 5294 | Genoa, Italy                                  |       nan    |
| 5295 | Milan, Italy                                  |       nan    |
| 5296 | Monza, Italy                                  |       nan    |
| 5297 | Fuchu, Japan                                  |       nan    |
| 5298 | Hakodate, Japan                               |       nan    |
| 5299 | Hokuto, Japan                                 |       nan    |
| 5300 | Mashiko, Japan                                |       nan    |
| 5301 | Oyama, Japan                                  |       nan    |
| 5302 | Shibetsu, Japan                               |       nan    |
| 5303 | Tokoname, Japan                               |       nan    |
| 5304 | Oaxaca, Mexico                                |       nan    |
| 5305 | San Antonino Castillo Velasco, Mexico         |       nan    |
| 5306 | Cromwell, New Zealand                         |       nan    |
| 5307 | Palmerston North, New Zealand                 |       nan    |
| 5308 | Narvik, Norway                                |       nan    |
| 5309 | Baguio City, Philippines                      |       nan    |
| 5310 | Binan, Philippines                            |       nan    |
| 5311 | Puerto Princesa, Philippines                  |       nan    |
| 5312 | Zamboanga City, Philippines                   |       nan    |
| 5313 | Egilsstadhir, Iceland                         |       nan    |
| 5314 | Avigliano, Italy                              |       nan    |
| 5315 | Abira, Japan                                  |       nan    |
| 5316 | Iida, Japan                                   |       nan    |
| 5317 | Ishizaki, Japan                               |       nan    |
| 5318 | Otawara, Japan                                |       nan    |
| 5319 | Tendo, Japan                                  |       nan    |
| 5320 | Yuza, Japan                                   |       nan    |
| 5321 | Swakopmund, Namibia                           |       nan    |
| 5322 | Arecibo, Puerto Rico                          |       nan    |
| 5323 | Ponce, Puerto Rico                            |       nan    |
| 5324 | Dolinsk, Russia                               |       nan    |
| 5325 | Kholmsk, Russia                               |       nan    |
| 5326 | Murmansk, Russia                              |       nan    |
| 5327 | Nevel'sk, Russia                              |       nan    |
| 5328 | Abha, Saudi Arabia                            |       nan    |
| 5329 | Al Bahah, Saudi Arabia                        |       nan    |
| 5330 | Buraydah, Saudi Arabia                        |       nan    |
| 5331 | Ha'il, Saudi Arabia                           |       nan    |
| 5332 | Jazan, Saudi Arabia                           |       nan    |
| 5333 | Riyadh, Saudi Arabia                          |       nan    |
| 5334 | Tabuk, Saudi Arabia                           |       nan    |
| 5335 | Unayzah, Saudi Arabia                         |       nan    |
| 5336 | Haparanda, Sweden                             |       nan    |
| 5337 | Vasteras, Sweden                              |       nan    |
| 5338 | Schlieren, Switzerland                        |       nan    |
| 5339 | Boulder City, United States                   |       nan    |
| 5340 | Cheyenne, United States                       |       nan    |
| 5341 | Enterprise, United States                     |       nan    |
| 5342 | Estes Park, United States                     |       nan    |
| 5343 | Kenai, United States                          |       nan    |
| 5344 | Las Vegas, United States                      |       nan    |
| 5345 | Midlothian, United States                     |       nan    |
| 5346 | Mount Shasta, United States                   |       nan    |
| 5347 | Pearl City, United States                     |       nan    |
| 5348 | Rosamond, United States                       |       nan    |
| 5349 | Shasta Lake, United States                    |       nan    |
| 5350 | Silver City, United States                    |       nan    |
| 5351 | Silverthorne, United States                   |       nan    |
| 5352 | Spring Valley, United States                  |       nan    |
| 5353 | Summerlin South, United States                |       nan    |
| 5354 | Tamuning, United States                       |       nan    |
| 5355 | Waikoloa Village, United States               |       nan    |
| 5356 | Woodland Park, United States                  |       nan    |
| 5357 | South Grafton, Australia                      |       nan    |
| 5358 | Hallein, Austria                              |       nan    |
| 5359 | Cochabamba, Bolivia                           |       nan    |
| 5360 | Bonnyville, Canada                            |       nan    |
| 5361 | Canmore, Canada                               |       nan    |
| 5362 | Peace River, Canada                           |       nan    |
| 5363 | Prince Albert, Canada                         |       nan    |
| 5364 | Redcliff, Canada                              |       nan    |
| 5365 | Regina, Canada                                |       nan    |
| 5366 | Swift Current, Canada                         |       nan    |
| 5367 | Thompson, Canada                              |       nan    |
| 5368 | Gyegu, China                                  |       nan    |
| 5369 | Xichang, China                                |       nan    |
| 5370 | Santa Tecla, El Salvador                      |       nan    |
| 5371 | Heinola, Finland                              |       nan    |
| 5372 | Hyvinkaa, Finland                             |       nan    |
| 5373 | Joensuu, Finland                              |       nan    |
| 5374 | Mikkeli, Finland                              |       nan    |
| 5375 | Tornio, Finland                               |       nan    |
| 5376 | Beausoleil, France                            |       nan    |

The operation is transform data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec | Temperature_Category   |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:-----------------------|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 | High                   |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 | High                   |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 | High                   |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 | High                   |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 | High                   |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 | Moderate               |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 | Moderate               |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 | Moderate               |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 | Moderate               |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 | Moderate               |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is describe data

The truncated output is: 

|    | summary   |    rank | city                |       avg |       jan |       feb |       mar |       apr |       may |       jun |       jul |       aug |       sep |       oct |       nov |       dec |
|---:|:----------|--------:|:--------------------|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|
|  0 | count     | 5377    | 5377                | 5377      | 4835      | 4833      | 4875      | 4840      | 4825      | 4784      | 4754      | 4739      | 4637      | 4699      | 5364      | 5373      |
|  1 | mean      | 2689    |                     |   32.1717 |   44.6443 |   42.767  |   40.3586 |   38.706  |   33.1822 |   32.5677 |   27.9424 |   28.4851 |   27.9672 |   31.4741 |   35.8331 |   39.566  |
|  2 | stddev    | 1552.35 |                     |   27.0752 |   52.1882 |   41.2054 |   37.3938 |   34.2302 |   22.6295 |   21.2726 |   19.1713 |   21.9076 |   19.2934 |   27.4785 |   39.9561 |   43.7187 |
|  3 | min       |    1    | A Coruna, Spain     |    1      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |
|  4 | max       | 5377    | Zwolle, Netherlands |  223      |  418      |  344      |  534      |  412      |  306      |  338      |  286      |  545      |  463      |  357      |  405      |  406      |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is query data

The query is SELECT city, avg FROM city_temperatures WHERE avg > 200

The truncated output is: 

|    | city             |   avg |
|---:|:-----------------|------:|
|  0 | Begusarai, India |   223 |
|  1 | Patna, India     |   212 |
|  2 | Saharsa, India   |   207 |
|  3 | New Delhi, India |   205 |
|  4 | Noida, India     |   201 |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is transform data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec | Temperature_Category   |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:-----------------------|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 | High                   |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 | High                   |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 | High                   |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 | High                   |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 | High                   |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 | Moderate               |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 | Moderate               |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 | Moderate               |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 | Moderate               |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 | Moderate               |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is describe data

The truncated output is: 

|    | summary   |    rank | city                |       avg |       jan |       feb |       mar |       apr |       may |       jun |       jul |       aug |       sep |       oct |       nov |       dec |
|---:|:----------|--------:|:--------------------|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|
|  0 | count     | 5377    | 5377                | 5377      | 4835      | 4833      | 4875      | 4840      | 4825      | 4784      | 4754      | 4739      | 4637      | 4699      | 5364      | 5373      |
|  1 | mean      | 2689    |                     |   32.1717 |   44.6443 |   42.767  |   40.3586 |   38.706  |   33.1822 |   32.5677 |   27.9424 |   28.4851 |   27.9672 |   31.4741 |   35.8331 |   39.566  |
|  2 | stddev    | 1552.35 |                     |   27.0752 |   52.1882 |   41.2054 |   37.3938 |   34.2302 |   22.6295 |   21.2726 |   19.1713 |   21.9076 |   19.2934 |   27.4785 |   39.9561 |   43.7187 |
|  3 | min       |    1    | A Coruna, Spain     |    1      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |    0      |
|  4 | max       | 5377    | Zwolle, Netherlands |  223      |  418      |  344      |  534      |  412      |  306      |  338      |  286      |  545      |  463      |  357      |  405      |  406      |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is query data

The query is SELECT city, avg FROM city_temperatures WHERE avg > 200

The truncated output is: 

|    | city             |   avg |
|---:|:-----------------|------:|
|  0 | Begusarai, India |   223 |
|  1 | Patna, India     |   212 |
|  2 | Saharsa, India   |   207 |
|  3 | New Delhi, India |   205 |
|  4 | Noida, India     |   201 |

The operation is load data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 |

The operation is transform data

The truncated output is: 

|    |   rank | city             |   avg |   jan |   feb |   mar |   apr |   may |   jun |   jul |   aug |   sep |   oct |   nov |   dec | Temperature_Category   |
|---:|-------:|:-----------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:-----------------------|
|  0 |      1 | Begusarai, India |   223 |   413 |   337 |   250 |   258 |   209 |   205 |   131 |   115 |   100 |   114 |   298 |   249 | High                   |
|  1 |      2 | Patna, India     |   212 |   354 |   297 |   225 |   230 |   169 |   183 |    82 |   100 |    84 |   136 |   402 |   277 | High                   |
|  2 |      3 | Saharsa, India   |   207 |   418 |   344 |   238 |   220 |   167 |   149 |    85 |    93 |    91 |   110 |   282 |   292 | High                   |
|  3 |      4 | New Delhi, India |   205 |   325 |   244 |   167 |   181 |   175 |   124 |    70 |   110 |    91 |   210 |   405 |   352 | High                   |
|  4 |      5 | Noida, India     |   201 |   304 |   212 |   154 |   187 |   176 |   129 |    70 |   125 |   118 |   237 |   367 |   338 | High                   |
|  5 |      6 | Kashgar, China   |   197 |   283 |   175 |   288 |   285 |   184 |    99 |   106 |   135 |   126 |   118 |   206 |   355 | Moderate               |
|  6 |      7 | Ghaziabad, India |   190 |   302 |   216 |   155 |   175 |   164 |   124 |    68 |   101 |    98 |   185 |   360 |   332 | Moderate               |
|  7 |      8 | Faridabad, India |   186 |   295 |   210 |   149 |   155 |   143 |   118 |    72 |   100 |    93 |   198 |   356 |   337 | Moderate               |
|  8 |      9 | Aksu, China      |   185 |   210 |   141 |   285 |   412 |   105 |    84 |    76 |    85 |   100 |   103 |   210 |   406 | Moderate               |
|  9 |     10 | Purnea, India    |   182 |   398 |   305 |   218 |   187 |   109 |   101 |    57 |    72 |    70 |   131 |   252 |   280 | Moderate               |

