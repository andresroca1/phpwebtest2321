<?php

use \yii\web\Request;

$baseUrl = str_replace('/web', '', (new Request)->getBaseUrl());

$params = require(__DIR__ . '/params.php');

$config = [
    'id' => 'basic',
    'basePath' => dirname(__DIR__),
    'bootstrap' => ['log'],
    'components' => [
			'session' => array(
			  'class' => 'yii\web\DbSession',
			  'timeout' => 1800,
		   ),
	
	'awssdk' => [
            'class' => 'fedemotta\awssdk\AwsSdk',
            'credentials' => [ //you can use a different method to grant access
                'key' => 'AKIAJGI4MPJQD5IKGXXQ',
                'secret' => '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',
            ],
            'region' => 'us-west-2', //i.e.: 'us-east-1'
            'version' => 'latest', //i.e.: 'latest'
        ],
		'sendGrid' => [
	    'class' => 'bryglen\sendgrid\Mailer',
	    'username'=>'samknara',
	    'password' => 'SkyInsTech2017#@!',
	    
	    ],
		/*'recaptcha' => [
        'class' => 'richweber\recaptcha\ReCaptcha',
       // 'siteKey' => 'https://www.google.com/recaptcha/admin',
	    'siteKey' => '6LfW8SEUAAAAAF1OS44oiI2kjlu5qPxNeKCs1g9z',
        'secretKey' => '6LfW8SEUAAAAACaKajMB5Tam810bYUlo8PCHiYoN',
        'errorMessage' => 'Are you robot?',
		],*/
		'reCaptcha' => [
        'name' => 'reCaptcha',
        'class' => 'himiklab\yii2\recaptcha\ReCaptcha',
        //'siteKey' => 'your siteKey',
        //'secret' => 'your secret key',
		'siteKey' => '6LfW8SEUAAAAAF1OS44oiI2kjlu5qPxNeKCs1g9z',
        'secret' => '6LfW8SEUAAAAACaKajMB5Tam810bYUlo8PCHiYoN',
		],
		 'assetManager' => [
		    'linkAssets' => false,
		    'appendTimestamp' => true, // timestamp for cache busting assets
		    'hashCallback' => function ($path) { //for autoscaling in different servers
		   		 return hash('md4', $path);
		    },
			'bundles' => [
            'yii\bootstrap\BootstrapPluginAsset' => [
                'js'=>[]
            ],
        ],
	    ],
		
        'request' => [
            // !!! insert a secret key in the following (if it is empty) - this is required by cookie validation
            'cookieValidationKey' => 'WbgPGcx5OL4WatyoVsHv-kgX2jLVe9Xw',
			'baseUrl' => $baseUrl,
			'enableCsrfValidation' => false,
        ],
		 
        'cache' => [
            'class' => 'yii\caching\FileCache',
        ],
        'AccessRule' => [
        	'class' => 'app\components\AccessRuleComponent',
        ],
        'SessionCheck' => [
        'class' => 'app\components\SessionCheckComponent',
        ],
		 'EncryptDecrypt' => [
        'class' => 'app\components\EncryptDecryptComponent',
        ],
        'user' => [
			 'class' => 'listfixer\remember\RememberMe',
            'identityClass' => 'app\models\User',
            'enableAutoLogin' => true,
			'loginUrl' => ['site/login'],
		 ],
		 
        'errorHandler' => [
            'errorAction' => 'site/error',
			'maxSourceLines' => 20,
        ],
		'customMail' => [
        'class' => 'app\components\MailComponent',
        ],
        'mailer' => [
            'class' => 'yii\swiftmailer\Mailer',
            // send all mails to a file by default. You have to set
            // 'useFileTransport' to false and configure a transport
            // for the mailer to send real emails.
            'useFileTransport' => true,
        ],
         'log' => [
            'traceLevel' => YII_DEBUG ? 3 : 0,
            'targets' => [
               'file' => [
                    'class' => 'yii\log\FileTarget',
                    'levels' => ['error', 'warning'],
                    'except' => ['yii\web\HttpException:404'],
                    'logFile' => '@runtime/logs/404.log',
                ],
                'email' => [
                                 'class' => 'yii\log\EmailTarget',
                                 'mailer' => 'mailer',
                                 'except' => ['yii\web\HttpException:404'],
                                 'levels' => ['error', 'warning'],
                                 'message' => [
                                     	'from' => ['admin@bc.com'],
                                      	'to' => ['banelasainath@gmail.com', 'ankamranjithkumar@gmail.com'],
                                      	'subject' => 'Log message',
                                  ],
                ],
            ],
        ],
        'db' => require(__DIR__ . '/db.php'),
        
        'urlManager' => [
            'enablePrettyUrl' => true,
            'showScriptName' => false,
            'rules' => [
			'<alias:index|about|contact|login|logout|forgot-password|verification|verify-mail>' => 'site/<alias>',
            ],
        ],
        
		
	
	
	
	
    ],
    'modules' => [
	    'admin' => [
	    	'class' => 'app\modules\admin\Module',
	    ],
	    'firm' => [
	    	'class' => 'app\modules\firm\Module',
	    ],
	    'client' => [
	    	'class' => 'app\modules\client\Module',
	    ],
		 'designmodule' => [
	    	'class' => 'app\modules\designmodule\Module',
	    ],
		'gridview'=> [
			'class'=>'\kartik\grid\Module'
					// other module settings
			],
			'design' => [
	    	'class' => 'app\modules\design\Module',
	    ],
    ],
    'params' => $params,
];

if (YII_ENV_DEV) {
    // configuration adjustments for 'dev' environment
    $config['bootstrap'][] = 'debug';
    $config['modules']['debug'] = [
        'class' => 'yii\debug\Module',
        // uncomment the following to add your IP if you are not connecting from localhost.
        //'allowedIPs' => ['127.0.0.1', '::1'],
    ];

    $config['bootstrap'][] = 'gii';
    $config['modules']['gii'] = [
        'class' => 'yii\gii\Module',
        // uncomment the following to add your IP if you are not connecting from localhost.
        //'allowedIPs' => ['127.0.0.1', '::1'],
    ];
}

return $config;
