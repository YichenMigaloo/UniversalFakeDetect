DATASET_PATHS = [

    dict(   
        real_path= 'UniversalFakeDetect/datasets/test/progan/0_real',
        fake_path='UniversalFakeDetect/datasets/test/progan/1_fake',
        data_mode='',
        key='testtest'
    ),


    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/imagenet',
        fake_path='UniversalFakeDetect/diffusion_datasets/guided',
        data_mode='wang2020',
        key='guided'
    ),


    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='UniversalFakeDetect/diffusion_datasets/ldm_200',
        data_mode='wang2020',
        key='ldm_200'
    ),

    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='UniversalFakeDetect/diffusion_datasets/ldm_200_cfg',
        data_mode='wang2020',
        key='ldm_200_cfg'
    ),

    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='UniversalFakeDetect/diffusion_datasets/ldm_100',
        data_mode='wang2020',
        key='ldm_100'
     ),


    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='UniversalFakeDetect/diffusion_datasets/glide_100_27',
        data_mode='wang2020',
        key='glide_100_27'
    ),


    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='UniversalFakeDetect/diffusion_datasets/glide_50_27',
        data_mode='wang2020',
        key='glide_50_27'
    ),


    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='UniversalFakeDetect/diffusion_datasets/glide_100_10',
        data_mode='wang2020',
        key='glide_100_10'
    ),


    dict(
        real_path='UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='UniversalFakeDetect/diffusion_datasets/dalle',
        data_mode='wang2020',
        key='dalle'
    ),

    

    dict(
        real_path= 'UniversalFakeDetect/diffusion_datasets/imagenet',
        fake_path='UniversalFakeDetect/diffusion_datasets/ldm_100',
        data_mode='wang2020',
        key='testtest2'
    )



]
