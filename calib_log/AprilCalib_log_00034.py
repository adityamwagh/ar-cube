# AprilCalib log 34
# CalibRig::mode=2d
# @ Fri Dec  3 18:21:39 2021

from numpy import array
U=array([[67.60031127929688, 101.0477981567383, 28.23227310180664, 106.8010711669922, 73.51309204101562, 34.37742233276367, 112.6806335449219, 79.6436767578125, 40.62628173828125, 118.7626266479492, 85.86853790283203, 46.7624626159668],
       [279.2743835449219, 279.2854309082031, 279.4700317382812, 328.9277648925781, 332.9791259765625, 337.6369934082031, 379.6130981445312, 387.5948791503906, 396.9052429199219, 430.9837341308594, 442.9171447753906, 457.2646789550781]], dtype='float64');
Xw=array([[299.5044555664062, 99.50446319580078, 499.5044555664062, 99.50446319580078, 299.5044555664062, 499.5044555664062, 99.50446319580078, 299.5044555664062, 499.5044555664062, 99.50446319580078, 299.5044555664062, 499.5044555664062],
       [899.5044555664062, 899.5044555664062, 899.5044555664062, 699.5044555664062, 699.5044555664062, 699.5044555664062, 499.5044555664062, 499.5044555664062, 499.5044555664062, 299.5044555664062, 299.5044555664062, 299.5044555664062],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='float64');
# After LM:
K=array([[641.4169280828904, 0, 316.456142621744],
       [0, 639.7679400765754, 245.2761062562514],
       [0, 0, 1]], dtype='float64');
distCoeffs=array([-0.0453453809968622,
       -0.0006614797752481172,
       0.005663206833712109,
       -0.004253418448602931,
       0], dtype='float64');
CovK=array([[0.0841087199666621, 0.08034152784195801, 0.01395072169713437, -0.05078630677284362, -8.728365355933131e-06, 0.0007055853631381062, -1.686852962353313e-05, 3.693832242684181e-06, -0.00142023351057712],
       [0.08034152784173719, 0.08441378015711756, 0.01925250798745199, -0.0419757758329537, 2.421558991443074e-05, 0.0005914996677087278, -2.058125661211821e-05, 4.958010371005379e-06, -0.001214864126115625],
       [0.0139507216795259, 0.0192525079699352, 0.254729097747946, -0.00895910687947753, -1.213726788161629e-06, 0.0003842101788981538, -6.820001336303195e-06, 0.0001044044047081185, -0.0008568318274089991],
       [-0.05078630677012928, -0.04197577583020823, -0.008959106884072383, 0.1789128161418828, -8.067754934450343e-05, -0.000265144345363225, 6.462824078617944e-05, -6.721965353964163e-06, 0.00079801238891054],
       [-8.728365354764607e-06, 2.421558991572545e-05, -1.213726772378184e-06, -8.06775493522315e-05, 4.398811178816316e-06, -2.626273222386175e-05, -1.121347186904136e-07, -6.112508053361904e-09, 5.04847651234925e-05],
       [0.0007055853631066907, 0.0005914996676780946, 0.0003842101789420787, -0.0002651443453302828, -2.626273222390587e-05, 0.0001843211053241711, 1.833803813419326e-07, 2.023786791003312e-07, -0.0003736467483360075],
       [-1.686852962229773e-05, -2.058125661085619e-05, -6.820001337296271e-06, 6.462824078613577e-05, -1.121347186874724e-07, 1.833803813316521e-07, 3.873301118658755e-08, -3.784139523603237e-09, -2.454244442512692e-07],
       [3.693832235349513e-06, 4.958010363705242e-06, 0.0001044044047076939, -6.721965351828261e-06, -6.112508060392335e-09, 2.023786790834719e-07, -3.784139523090374e-09, 4.644526353040687e-08, -4.347480671422963e-07],
       [-0.00142023351050726, -0.001214864126047138, -0.0008568318275140257, 0.000798012388848087, 5.048476512359432e-05, -0.0003736467483360757, -2.454244442701196e-07, -4.347480671845851e-07, 0.0007841709405823349]], dtype='float64');
# rms=0.223453
r0=array([-0.3812710370840092,
       -0.004121940145802318,
       0.05135741256991685], dtype='float64');
t0=array([276.1854183708055,
       -51.54362517172392,
       3246.588668370592], dtype='float64');
Covr0=array([[6.011279986712239e-07, -3.588422239266046e-08, -8.766228999839351e-08],
       [-3.588422239084525e-08, 1.096620171354001e-06, 6.354675374362499e-08],
       [-8.766228999838e-08, 6.354675374473695e-08, 2.976600999752312e-08]], dtype='float64');
Covt0=array([[6.632699638977663, -0.1004461853608126, -0.4768060615818558],
       [-0.1004461854684592, 4.549101116981171, 1.510114069729684],
       [-0.4768060620176331, 1.510114069770621, 2.465922875290536]], dtype='float64');
r1=array([-0.370955791868426,
       0.1467864406568103,
       -0.08848026269836114], dtype='float64');
t1=array([-726.0358622600775,
       46.27154973492615,
       4385.441291010106], dtype='float64');
Covr1=array([[6.739575265063759e-07, 1.937073765379774e-08, 4.359945610711374e-09],
       [1.937073765199693e-08, 8.227005839173588e-07, 7.851001786656583e-08],
       [4.359945608809068e-09, 7.851001786784725e-08, 2.114175139799444e-08]], dtype='float64');
Covt1=array([[11.80908483674444, -0.3061215837238088, 1.071575697953634],
       [-0.3061215839433757, 8.390451610855635, 2.54678313855708],
       [1.071575697116876, 2.546783138723614, 3.872367042740807]], dtype='float64');
r2=array([-0.03115203690299114,
       -0.001074627761795967,
       -0.1363230215351661], dtype='float64');
t2=array([-1027.890358201736,
       -41.74623727331775,
       3494.337730676689], dtype='float64');
Covr2=array([[9.690537405711821e-07, -2.93933200980666e-08, 2.010680545237912e-08],
       [-2.939332009330102e-08, 8.121659997607596e-07, -3.449355037316212e-08],
       [2.010680545215371e-08, -3.449355037300222e-08, 7.238397402007966e-09]], dtype='float64');
Covt2=array([[7.574866767322103, -0.1943144972680439, 1.253068993345078],
       [-0.1943144974064117, 5.494106901885816, 1.733712524447342],
       [1.253068992797161, 1.733712524562467, 3.452574006853276]], dtype='float64');
r3=array([-0.2261723814404477,
       -1.122334572672278,
       0.1202456379152542], dtype='float64');
t3=array([-661.6501903923946,
       -374.2592639759544,
       470.8061657467416], dtype='float64');
Covr3=array([[4.173876271559928e-07, 3.194045233592467e-08, -1.664521554886896e-07],
       [3.1940452329597e-08, 5.780808089174347e-07, 3.716818695982839e-08],
       [-1.664521554893126e-07, 3.716818695665207e-08, 1.062159407122914e-07]], dtype='float64');
Covt3=array([[0.2135819286666869, -0.01700092904868945, 0.06097635126460109],
       [-0.01700092905331495, 0.14741188530464, 0.1941889656136445],
       [0.06097635123232793, 0.1941889656213787, 0.6760172058320266]], dtype='float64');
r4=array([-0.2468114474167683,
       -0.8785008895308425,
       0.1102861009540249], dtype='float64');
t4=array([-1277.409735236418,
       -207.9136115575481,
       1449.020601650063], dtype='float64');
Covr4=array([[4.890292140529579e-07, 2.610047316965392e-10, -9.577293159137906e-08],
       [2.610047175172652e-10, 6.147943046872552e-07, 2.363811183114712e-08],
       [-9.577293159052715e-08, 2.363811183019839e-08, 5.888773305975337e-08]], dtype='float64');
Covt4=array([[1.678537767696587, -0.0785090552969171, 0.4463738825715655],
       [-0.07850905532719005, 1.194697554992879, 0.7442641993013727],
       [0.4463738823616958, 0.7442641993502943, 2.179585330951226]], dtype='float64');
r5=array([1.041721133234426,
       -0.04893693260016655,
       -0.05776599892664386], dtype='float64');
t5=array([-1039.166020297583,
       -407.8362381524425,
       3152.973802976589], dtype='float64');
Covr5=array([[5.884200780912695e-07, 2.54469898742858e-08, -2.027901867298602e-08],
       [2.544698986144924e-08, 6.26439890905837e-07, -2.862365208443522e-07],
       [-2.027901866517982e-08, -2.862365208455249e-07, 1.840253390974366e-07]], dtype='float64');
Covt5=array([[6.262519271588371, -0.2467977494073628, 1.336882754489335],
       [-0.2467977495132562, 4.362772137091096, 1.622515208675862],
       [1.336882753998979, 1.622515208787879, 3.68848907624311]], dtype='float64');
r6=array([0.01884153533026743,
       -0.58826655143076,
       -1.020071257881051], dtype='float64');
t6=array([-796.6059512791693,
       771.0815314711999,
       2879.017005281877], dtype='float64');
Covr6=array([[5.333042570935719e-07, -9.408316377449384e-08, -7.540445093092348e-08],
       [-9.408316378589668e-08, 7.27706460995982e-07, -9.917920540010392e-08],
       [-7.540445092912943e-08, -9.917920540218708e-08, 4.745053294637284e-08]], dtype='float64');
Covt6=array([[5.397470673982252, -0.09448798749762349, 0.7336717147885456],
       [-0.09448798759752473, 3.777176898036276, 0.5098785609701074],
       [0.7336717143655782, 0.5098785610606691, 2.541962560498018]], dtype='float64');
r7=array([-0.8152142971044098,
       0.1533552182768715,
       0.08956894777446323], dtype='float64');
t7=array([-449.9150172691324,
       355.217301326794,
       3777.577902294724], dtype='float64');
Covr7=array([[4.220276477983312e-07, 2.438647371657074e-08, 2.056811758690275e-08],
       [2.438647371274527e-08, 5.860983848886482e-07, 1.784538608586644e-07],
       [2.056811758544058e-08, 1.784538608590641e-07, 6.722440766037811e-08]], dtype='float64');
Covt7=array([[8.789577666767155, -0.1830615848225285, 0.415942653520758],
       [-0.183061584974219, 6.284354396582341, 1.630638181657039],
       [0.4159426529644606, 1.63063818175443, 2.400039128776666]], dtype='float64');
r8=array([-0.9814665529149068,
       0.3128133829135843,
       0.4449846558389971], dtype='float64');
t8=array([-469.3501790812673,
       290.5340019289497,
       5090.585089369873], dtype='float64');
Covr8=array([[5.981869140482108e-07, 2.813327919825625e-10, 9.669517827210256e-08],
       [2.813327899775265e-10, 6.992686596785467e-07, 2.41693753833189e-07],
       [9.669517827137729e-08, 2.416937538331688e-07, 1.399839795098199e-07]], dtype='float64');
Covt8=array([[15.90582380262805, -0.3254444951816721, 0.434464370468201],
       [-0.3254444954323066, 11.5314519752581, 2.932914691075473],
       [0.4344643695276649, 2.932914691236967, 4.197097809857731]], dtype='float64');
r9=array([-0.5193696120954843,
       0.1164001676843406,
       1.386859724866452], dtype='float64');
t9=array([-1366.637085371855,
       -233.5014755625704,
       5044.037886433222], dtype='float64');
Covr9=array([[1.28292208598303e-06, 3.624500200254468e-07, 2.462776372409795e-07],
       [3.62450020027662e-07, 1.251460405063122e-06, -7.017771570461661e-08],
       [2.462776372381809e-07, -7.017771570761265e-08, 1.066093655523743e-07]], dtype='float64');
Covt9=array([[16.43092040261535, -0.8868010649656758, 1.124690734578463],
       [-0.8868010652512737, 11.38412232749438, 4.237248003467773],
       [1.124690733355031, 4.237248003709542, 7.033561332205167]], dtype='float64');
r10=array([-0.4173062076898897,
       -0.1395831884845205,
       -0.1562703941114525], dtype='float64');
t10=array([-1011.685940821189,
       680.8881017300238,
       5499.174298473994], dtype='float64');
Covr10=array([[6.897491879506379e-06, -1.59876761814807e-06, 4.456751133724385e-07],
       [-1.598767618163531e-06, 4.675841272482012e-06, -2.637566666749561e-07],
       [4.456751133782937e-07, -2.63756666686554e-07, 1.197001436279629e-07]], dtype='float64');
Covt10=array([[18.97252975125335, -0.6437989017973577, 0.8519023351968332],
       [-0.6437989019926095, 14.41071427662103, 5.809535188833138],
       [0.8519023342985022, 5.809535189592923, 14.89758779283151]], dtype='float64');
r11=array([0.566784504099037,
       -0.08650531735755596,
       0.01843723704766494], dtype='float64');
t11=array([-982.8638068508766,
       574.5781479893653,
       4568.495997622417], dtype='float64');
Covr11=array([[1.250422533613167e-06, 4.451823327391553e-08, 3.636918174521688e-08],
       [4.451823327064595e-08, 1.013439442296746e-06, -3.714361210970045e-07],
       [3.636918174641126e-08, -3.714361210975916e-07, 1.978788533341088e-07]], dtype='float64');
Covt11=array([[13.08146371505243, -0.3177736999524778, 1.321205997569878],
       [-0.3177737001993985, 9.597632199829761, 3.006714393348163],
       [1.321205996577103, 3.006714393551658, 7.42004735063155]], dtype='float64');
r12=array([-0.3719695225440838,
       -0.9495114957434209,
       -0.118104291338754], dtype='float64');
t12=array([-1300.677450315394,
       -31.48452224942395,
       749.1470270988528], dtype='float64');
Covr12=array([[6.945220594004246e-07, -3.431461729845353e-08, -1.047073683175143e-07],
       [-3.431461730678203e-08, 8.378321594884157e-07, 5.798591336776675e-08],
       [-1.047073683183052e-07, 5.798591336641493e-08, 1.0702257339914e-07]], dtype='float64');
Covt12=array([[0.9751503727421299, -0.1045293566059257, -0.1545123308491183],
       [-0.104529356618654, 0.542015571678121, 0.4190761493477801],
       [-0.1545123309379297, 0.419076149372088, 2.117249100089805]], dtype='float64');
r13=array([-0.3563644631581013,
       1.003144040374912,
       -0.03212727376046347], dtype='float64');
t13=array([671.940841384081,
       230.7158520074332,
       3184.873619402209], dtype='float64');
Covr13=array([[9.485758407104187e-07, 4.387752748092188e-08, -7.750606572626309e-08],
       [4.387752747711253e-08, 1.033472689400249e-06, -5.295282245486052e-08],
       [-7.750606572702636e-08, -5.295282245719186e-08, 2.258187195273203e-07]], dtype='float64');
Covt13=array([[6.481408496882164, -0.1120677296828909, -1.004617034643491],
       [-0.1120677298014861, 4.716406499785924, 1.709239461875404],
       [-1.004617035113492, 1.709239461921769, 3.767370640445943]], dtype='float64');
r14=array([-0.8386854925877358,
       0.7790109249012527,
       1.171112879864149], dtype='float64');
t14=array([930.8562825105475,
       897.1651677708634,
       4195.577893756595], dtype='float64');
Covr14=array([[8.545470052432179e-07, 1.38313063681845e-07, 2.572301645184195e-07],
       [1.38313063680952e-07, 1.042077026821817e-06, 1.171533418922812e-07],
       [2.572301645185472e-07, 1.171533418938304e-07, 1.735708274490658e-07]], dtype='float64');
Covt14=array([[11.18121856931844, -0.5368625568735762, -3.05451737280294],
       [-0.5368625570648013, 8.364592141445041, 2.130705350965284],
       [-3.0545173735581, 2.130705351057981, 4.942674054346198]], dtype='float64');
r15=array([-1.099699174609968,
       0.4837408765141907,
       0.5235037182566282], dtype='float64');
t15=array([1695.790075803299,
       628.6227282594343,
       4000.777229606126], dtype='float64');
Covr15=array([[9.054786375806167e-07, -1.154175600995563e-08, 1.500070811160519e-07],
       [-1.154175601084225e-08, 1.586988169611957e-06, -1.825242420558248e-07],
       [1.500070811155989e-07, -1.825242420534859e-07, 5.038371047275609e-07]], dtype='float64');
Covt15=array([[11.4592345013821, -0.08173111600671457, -1.753305149677647],
       [-0.08173111617575388, 8.217307360153271, 3.831510990704117],
       [-1.753305150405204, 3.831510990762091, 14.37201977799239]], dtype='float64');
r16=array([-0.5766787632414445,
       0.8418630742159453,
       0.4779277171621328], dtype='float64');
t16=array([1022.924530488033,
       129.2088674988839,
       2853.380255433854], dtype='float64');
Covr16=array([[1.002710812517364e-06, -1.365228235267127e-07, 1.500535970956254e-07],
       [-1.365228235270527e-07, 1.320394612592858e-06, 1.513476928065252e-08],
       [1.500535970951176e-07, 1.513476928072503e-08, 1.611209415799396e-07]], dtype='float64');
Covt16=array([[5.265191510752859, -0.1190372210890313, -1.819479816337771],
       [-0.1190372211760075, 3.927363872277471, 1.513539397424784],
       [-1.819479816699813, 1.513539397455478, 3.074813722670629]], dtype='float64');
r17=array([0.04436543968880281,
       1.456956108717391,
       0.07951311682614857], dtype='float64');
t17=array([797.2429195977286,
       -121.0495444634482,
       2139.537479213146], dtype='float64');
Covr17=array([[6.969267874981401e-07, 8.196564740869899e-08, 2.610245812394494e-07],
       [8.196564740493667e-08, 8.494952878364741e-07, -2.665962285745861e-08],
       [2.610245812398627e-07, -2.665962285759369e-08, 1.966531198259333e-07]], dtype='float64');
Covt17=array([[3.106056180448167, -0.079929984602129, -0.8390100240000458],
       [-0.07992998465482296, 2.182795216696753, 0.9452317112447262],
       [-0.8390100242239904, 0.9452317112661263, 1.847406174469021]], dtype='float64');
r18=array([0.0129174718677541,
       1.402968496344929,
       -0.003747831505132478], dtype='float64');
t18=array([541.4715823829761,
       -75.73934273788407,
       2353.243184575836], dtype='float64');
Covr18=array([[3.992173426621595e-07, 5.800799202644317e-08, 1.709989480367081e-07],
       [5.800799202344283e-08, 6.055214475549791e-07, -2.786062329194008e-08],
       [1.709989480372444e-07, -2.786062329120173e-08, 1.470251901402359e-07]], dtype='float64');
Covt18=array([[3.517885265663606, -0.1214206420156841, -0.7416829788238519],
       [-0.1214206420673733, 2.447548986711407, 0.7550673090187884],
       [-0.7416829790246836, 0.755067309039905, 1.100132219766515]], dtype='float64');
r19=array([0.00715846052786669,
       1.22706301364349,
       -0.01219617072913802], dtype='float64');
t19=array([-277.2588285886476,
       12.86169812667333,
       2410.227173939591], dtype='float64');
Covr19=array([[4.503085942062853e-07, 4.769642189363605e-08, 1.417347973235324e-07],
       [4.769642188554206e-08, 6.481930400556947e-07, -3.109661854725013e-08],
       [1.41734797324227e-07, -3.109661854736284e-08, 1.913412567652035e-07]], dtype='float64');
Covt19=array([[3.587565399823929, -0.0796302653509621, 0.2679056707602203],
       [-0.07963026539627502, 2.461547190379904, 0.4298497190738735],
       [0.2679056706395704, 0.4298497191028541, 0.5334732755039764]], dtype='float64');
r20=array([-0.5185196975513366,
       -0.2549289380066243,
       0.03291347335688095], dtype='float64');
t20=array([-1558.97516947396,
       312.6371668754752,
       2049.310078917552], dtype='float64');
Covr20=array([[3.975273531794048e-06, 6.966867602903942e-07, 3.833095676923048e-07],
       [6.966867602836462e-07, 2.999069350167313e-06, 5.750077716086425e-08],
       [3.833095676905748e-07, 5.750077715927775e-08, 9.40176406472318e-08]], dtype='float64');
Covt20=array([[2.948168669278799, -0.2013421457838172, 0.7495425872193736],
       [-0.2013421458359687, 2.480789356900605, 1.475856735825658],
       [0.7495425869752195, 1.475856735888355, 4.789450657566579]], dtype='float64');
r21=array([-0.4399479678940764,
       -0.9382455176992931,
       0.08891902816559302], dtype='float64');
t21=array([-1206.604181044733,
       -147.6548445674413,
       1375.203390267457], dtype='float64');
Covr21=array([[5.015630933120063e-07, 2.510412317307967e-08, -8.99906395549778e-08],
       [2.510412316702093e-08, 6.038672385567235e-07, 6.881753412207813e-08],
       [-8.999063955502608e-08, 6.881753412087634e-08, 8.802568168423167e-08]], dtype='float64');
Covt21=array([[1.509962525070453, -0.07909032950012802, 0.4078183203269535],
       [-0.07909032953015534, 1.082930861385432, 0.6851982956420394],
       [0.407818320169792, 0.6851982956800157, 1.895505458995184]], dtype='float64');
r22=array([-0.4801104972720235,
       -0.961204991871794,
       0.0009264855569909999], dtype='float64');
t22=array([-1331.016558275883,
       -71.17501998055629,
       1441.470840454781], dtype='float64');
Covr22=array([[5.784914321717212e-07, 1.295167208895979e-08, -8.97866875815707e-08],
       [1.295167208257258e-08, 6.819772854378551e-07, 7.318699027681124e-08],
       [-8.978668758262806e-08, 7.318699027558537e-08, 1.129190949158599e-07]], dtype='float64');
Covt22=array([[1.788088845461443, -0.1360454218966211, 0.3393448475845981],
       [-0.1360454219311639, 1.256288666177988, 0.8244970613392073],
       [0.3393448474040929, 0.82449706138441, 2.4890216617391]], dtype='float64');
r23=array([-0.527494894325198,
       -0.1797361907197184,
       0.7517841635937867], dtype='float64');
t23=array([-604.9581848211234,
       -576.896994928942,
       1975.2228100526], dtype='float64');
Covr23=array([[7.718343159616097e-07, 1.234125450113865e-07, 8.444523223768901e-08],
       [1.234125450055607e-07, 6.157636819247416e-07, 8.616870688173325e-08],
       [8.444523223700688e-08, 8.616870688138683e-08, 4.282194559844026e-08]], dtype='float64');
Covt23=array([[2.331548341332095, -0.08493146115591019, 0.288482432008325],
       [-0.08493146119605964, 1.700925923409432, 0.9464416491811857],
       [0.2884824318439079, 0.9464416492158433, 1.313831900671845]], dtype='float64');
r24=array([-1.260836148779284,
       0.1886345255904497,
       0.04202694843306504], dtype='float64');
t24=array([-512.3311702227404,
       487.5485486431803,
       3485.669921074007], dtype='float64');
Covr24=array([[4.094354077759149e-07, 9.926585861572835e-10, 2.951014769460324e-08],
       [9.926585844080524e-10, 5.582199580074166e-07, 3.135784762532885e-07],
       [2.951014769321126e-08, 3.135784762529247e-07, 1.965494677577408e-07]], dtype='float64');
Covt24=array([[7.590170226535567, -0.1042763659776513, 0.6347158647524924],
       [-0.1042763660915659, 5.321549689048537, 0.9858792937038179],
       [0.6347158643338476, 0.9858792937776627, 1.626437685832251]], dtype='float64');
r25=array([-0.9190011258296057,
       0.1159383770816332,
       0.1245150909898184], dtype='float64');
t25=array([-667.9152185595588,
       236.7426035577354,
       3303.902852619121], dtype='float64');
Covr25=array([[3.989427580988349e-07, 3.749393664828621e-08, 3.69978015581797e-08],
       [3.749393664378918e-08, 5.620848456329426e-07, 2.098587452590861e-07],
       [3.699780155639437e-08, 2.098587452601727e-07, 8.835162450318149e-08]], dtype='float64');
Covt25=array([[6.684698836453528, -0.1268430690395835, 0.8373578043731119],
       [-0.1268430691572946, 4.816204406006451, 1.263912495348146],
       [0.8373578039480793, 1.263912495429682, 1.894177754677242]], dtype='float64');
r26=array([-0.2416720971504453,
       -0.02695087419286225,
       0.1061778959169095], dtype='float64');
t26=array([-812.0186726994287,
       -551.4955286034068,
       2998.425270488666], dtype='float64');
Covr26=array([[5.982072837403563e-07, 3.920773398795473e-08, 1.050084892578591e-08],
       [3.920773397631768e-08, 6.471204665760755e-07, 6.519733902384968e-08],
       [1.050084892450829e-08, 6.519733902397215e-08, 1.104413935308555e-08]], dtype='float64');
Covt26=array([[5.562848046806315, -0.2112266600753243, 0.8502772725875275],
       [-0.2112266601779003, 3.9390535250776, 1.740622458856529],
       [0.8502772721784118, 1.740622458944671, 2.646165304590621]], dtype='float64');
r27=array([-0.9020373330947404,
       0.1377124070443699,
       -0.1542197523418052], dtype='float64');
t27=array([-1616.910898556401,
       661.2498540368022,
       5106.720342875509], dtype='float64');
Covr27=array([[1.67577743329128e-06, -2.358987528824948e-07, 5.659525089841547e-08],
       [-2.358987528829075e-07, 1.703157001192205e-06, 4.547383019068333e-07],
       [5.659525089754345e-08, 4.547383019056665e-07, 1.912094963683013e-07]], dtype='float64');
Covt27=array([[16.66819304361259, 0.07892665743013033, 3.897223188812315],
       [0.07892665716372146, 12.60181458861418, 3.157522676956],
       [3.897223187736513, 3.157522677194956, 6.728547187218537]], dtype='float64');
r28=array([-0.8842313747438612,
       0.1443089684654372,
       1.266969989103861], dtype='float64');
t28=array([-1241.926742043405,
       519.6167232547931,
       5584.960585578524], dtype='float64');
Covr28=array([[1.985871709065843e-06, 1.828552234671916e-07, 4.578117253194853e-07],
       [1.828552234643649e-07, 1.601891628763349e-06, -5.490748182626824e-08],
       [4.578117253157381e-07, -5.490748182749611e-08, 2.47936723445097e-07]], dtype='float64');
Covt28=array([[19.78757134540679, -1.057643914664795, 1.212374583130293],
       [-1.057643915004601, 14.54306521830187, 4.238826765735091],
       [1.212374581802642, 4.238826766002787, 7.966824114100604]], dtype='float64');
r29=array([-1.000414683245395,
       0.3260422275558818,
       1.387321455152042], dtype='float64');
t29=array([-1108.548261393515,
       602.5277818892471,
       6039.130250588111], dtype='float64');
Covr29=array([[1.512199518168675e-06, 1.578616290776009e-07, 4.668144790782116e-07],
       [1.578616290786215e-07, 1.600897202731298e-06, -7.87223416591354e-08],
       [4.6681447907633e-07, -7.872234165894382e-08, 3.428220094711911e-07]], dtype='float64');
Covt29=array([[23.10942834434167, -1.099644072970921, 0.8329970132884629],
       [-1.099644073359908, 16.88871633692974, 4.566954990769307],
       [0.8329970118100511, 4.566954991061963, 9.197246445149608]], dtype='float64');
r30=array([-0.5652361085880865,
       0.4280475090714435,
       0.7798938528039063], dtype='float64');
t30=array([1294.617225171797,
       446.4218435420221,
       6149.507672918819], dtype='float64');
Covr30=array([[4.731133337207618e-06, -6.550146877779478e-08, -1.396439946966637e-07],
       [-6.550146877649071e-08, 4.528250324976086e-06, -1.988721819905717e-07],
       [-1.396439946958288e-07, -1.988721819860757e-07, 2.308170689700778e-07]], dtype='float64');
Covt30=array([[24.84007200426989, 0.4343371139936602, -3.189198306241317],
       [0.4343371135605094, 19.26705795495097, 8.627719871666079],
       [-3.189198307926213, 8.627719871845979, 17.07850408218541]], dtype='float64');
r31=array([-0.2790886201485103,
       0.3036906676982584,
       0.5719677524114022], dtype='float64');
t31=array([1088.3842956224,
       59.80979744847425,
       5272.265205801485], dtype='float64');
Covr31=array([[2.341126218272573e-06, -3.230338648826934e-08, -3.584021895231721e-07],
       [-3.230338647987984e-08, 2.120225685332314e-06, -4.100719045391524e-09],
       [-3.584021895227375e-07, -4.100719042573919e-09, 8.567976991952158e-08]], dtype='float64');
Covt31=array([[17.7161082327493, -0.2892320406672713, -3.227701041213805],
       [-0.2892320409759045, 12.3856888687695, 4.326078666415595],
       [-3.227701042491838, 4.326078666548305, 7.801074920707788]], dtype='float64');
r32=array([-0.707624686112974,
       0.08743714413682563,
       1.647100606396716], dtype='float64');
t32=array([-472.8755834639414,
       -157.617818163435,
       3197.993797420428], dtype='float64');
Covr32=array([[1.205696717780546e-06, 9.547924820070785e-08, 2.837144047600259e-07],
       [9.547924819569151e-08, 1.055864259439861e-06, -1.597950075388751e-08],
       [2.837144047559444e-07, -1.59795007539601e-08, 1.23967646434006e-07]], dtype='float64');
Covt32=array([[6.410883141293284, -0.3510854376863329, -0.04865834965417136],
       [-0.3510854378009589, 4.46394644572541, 1.670536756128737],
       [-0.04865835009180423, 1.670536756209114, 2.385769066040984]], dtype='float64');
r33=array([-0.2908434336418523,
       0.1310433233117684,
       1.947551043235955], dtype='float64');
t33=array([-57.57327935894237,
       -121.213726411779,
       1510.227342967656], dtype='float64');
Covr33=array([[4.523272426218318e-06, 9.70729755439291e-08, 5.74263732751284e-07],
       [9.707297552787713e-08, 2.101591170898715e-06, -2.437057021351739e-07],
       [5.74263732752693e-07, -2.437057021319505e-07, 1.486650367974961e-07]], dtype='float64');
Covt33=array([[1.482379669498358, -0.05969859406907446, -0.2527474859771249],
       [-0.05969859409450475, 0.9773597530576236, 0.3786925202770875],
       [-0.2527474860763282, 0.3786925202911097, 0.8298609197105166]], dtype='float64');
r34=array([-1.810626760342218,
       0.2644653695957726,
       2.478388558749697], dtype='float64');
t34=array([-695.9476497904724,
       1024.904343108443,
       2567.706932917307], dtype='float64');
Covr34=array([[1.060113188443646e-06, -3.458992988271246e-08, 6.953200021746014e-07],
       [-3.458992989675035e-08, 1.188194465330983e-06, 1.395874156424274e-07],
       [6.953200021741335e-07, 1.395874156524998e-07, 5.673862540870702e-07]], dtype='float64');
Covt34=array([[4.652587002319423, -0.01975592300417882, 0.208413778094166],
       [-0.01975592308050705, 3.004418831766619, -0.06392631930984827],
       [0.2084137777955756, -0.06392631924761628, 1.603404948921211]], dtype='float64');
