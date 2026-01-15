PERMITTIVITY_DICT ={
    'bug' : {    
        5.6 :
        {
            'Re_body':43,
            'Im_body':19,
            'Re_appendage' : 5.1,
            'Im_appendage' : 0.12, 
        },
        9.4 :
        {
            'Re_body':34,
            'Im_body':19,
            'Re_appendage' : 5.2,
            'Im_appendage' : 0.12, 
        },
        3.0 :
        {
            'Re_body':53,
            'Im_body':19,
            'Re_appendage' : 5,
            'Im_appendage' : 0.12, 
        },
        35 :
        {
            'Re_body':15,
            'Im_body':19,
            'Re_appendage' : 4.8,
            'Im_appendage' : 0.13, 
        },
        94 :
        {
            'Re_body':15, #Interpolation breaks, same as 35
            'Im_body':19,
            'Re_appendage' : 4.8,
            'Im_appendage' : 0.13, 
        },
    },
    'bird' : {    
        5.6 :
        {
            'Re_body':56,
            'Im_body':15,
            'Re_appendage' : 56,
            'Im_appendage' : 15, 
        },
        9.4 :
        {
            'Re_body':43,
            'Im_body':18,
            'Re_appendage' : 43,
            'Im_appendage' : 18, 
        },
        3.0 :
        {
            'Re_body':52,
            'Im_body':13,
            'Re_appendage' : 52,
            'Im_appendage' : 13, 
        },
        35 :
        {
            'Re_body':20, 
            'Im_body':20,
        },
        94 :
        {
            'Re_body':9,
            'Im_body':11.7,
        },
    },
}

full_insect_pitches = [-90,-70,-50,-30,-10,0,5,10,15,20,25,30,50,70,90]

full_size_sweep = [5,10,15,20,30,50,75,125,200]
finer_size_sweep = [2,4,6,8,10,12,14,16,18,20,25,35,45,50,75,125,200]


# Add optional Chitin parts
PARAMS_DICTS = {
    "hoverfly_test" : 
        {
            "type" : "bug", 
            "frequencies" : [5.6],
            "lengths" : [12],
            "slants" : [0],
            "pitches" : [0]
        },
    "15mm_hoverfly_full" : 
        {
            "type" : "bug", 
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [5,10,15,20,30,50,75,125],
            "slants" : [1],
            "pitches" : [0,10]
        },

    "12mm_hoverfly_12_14_16" : 
        {
            "frequencies" : [5.6],
            "lengths" : [12,14,16],
            "slants" : [0],
            "pitches" : [0]
        },
    "decimation_testing" : 
        {
            "frequencies" : [5.6],
            "lengths" : [5,12,20],
            "slants" : [0],
            "pitches" : [0]
        },
    "decimation_testing_2" : 
        {
            "type" : "bug",
            "frequencies" : [9.4],
            "lengths" : [15,20,30],
            "slants" : [1],
            "pitches" : [10]
        },
    "new_hoverfly_full" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [5,8,12,16,20,30],
            "slants" : [0.5,1,2],
            "pitches" : [-25,-20,-15,-10,-5,0,5,10,15,20,25]
        },
    "northern_damselfly_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [25,30,35],
            "slants" : [0.5,1,2],
            "pitches" : [0,5,10,15,20]
        },
    "beetle_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [5,10,20,30],
            "slants" : [0.5,1,2],
            "pitches" : [0,5,10,15,20]
        },
    "house_martin_initial" : 
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [100,125,150],
            "slants" : [0.5,1,2],
            "pitches" : [0,10,20]
        },
    "northern_damselfly_high_f_test" : 
        {
            "type" : "bug",
            "frequencies" : [35,94],
            "lengths" : [30],
            "slants" : [0.5],
            "pitches" : [10]
        },
    "mythropa_high_f_test" : 
        {
            "type" : "bug",
            "frequencies" : [35,94],
            "lengths" : [12],
            "slants" : [0.5],
            "pitches" : [10]
        },
    "beetle_elytra_comparison" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [10,20,30],
            "slants" : [1],
            "pitches" : [0,10]
        },
    "house_martin_wing_comparison" : 
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [125],
            "slants" : [1],
            "pitches" : [0,10,20]
        },
    "damselfly_elevation_probing" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [30],
            "slants" : [0.95, 0.98, 0.99,  1, 1.01, 1.02, 1.05],
            "pitches" : [0,10,20]
        },
    "cicada_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [50],
            "slants" : [0.5,1,2],
            "pitches" : [0,5,10,15,20]
        },
    "hawkmoth_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [50],
            "slants" : [0.5,1,2],
            "pitches" : [0,5,10,15,20]
        },
    "peregrine_initial" : 
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [400, 500],
            "slants" : [0.5,1,2],
            "pitches" : [0,10,20]
        },
    "peregrine_reduced" : 
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [500],
            "slants" : [1],
            "pitches" : [0,10]
        },
    "peregrine_xband_tidy" : 
        {
            "type" : "bird",
            "frequencies" : [9.4],
            "lengths" : [400, 500],
            "slants" : [1],
            "pitches" : [0,10]
        },
    "large_red_belted_clearwing_inital" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [14],
            "slants" : [1],
            "pitches" : [0,5,10,15,20]
        },
    "darter_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [25],
            "slants" : [1],
            "pitches" : [0,5,10,15,20]
        },
    "15mm_hoverfly_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [15],
            "slants" : [1],
            "pitches" : [0,5,10,15,20]
        },
    "15mm_hoverfly_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [15],
            "slants" : [1],
            "pitches" : [0,5,10,15,20]
        },
    "12mm_hoverfly_initial" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [15],
            "slants" : [1],
            "pitches" : [0,5,10,15,20]
        },
    "spider_testing" : 
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [5],
            "slants" : [1],
            "pitches" : [-90,0,90]
        },
    "valery_bird_initial" : 
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [125,500],
            "slants" : [1],
            "pitches" : [0,10,20]
        },
    "small_insect_full_param" :
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [5],
            "slants" : [1],
            "pitches" : full_insect_pitches,
        },
    "medium_insect_full_param" :
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [15],
            "slants" : [1],
            "pitches" : full_insect_pitches,
        },
    "large_insect_full_param" :
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [35,50],
            "slants" : [1],
            "pitches" : full_insect_pitches,
        },
    "house_martin_full_param" :
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [125],
            "slants" : [1],
            "pitches" : [0,5,10,15,25,30]
        },
    "falcon_full_param" :
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : [500],
            "slants" : [1],
            "pitches" : [0,5,10,15,25,30]
        },
    "insect_full_size_sweep" :
        {
            "type" : "bug",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : full_size_sweep,
            "slants" : [1],
            "pitches" : [0,10],
        },
    "insect_xband_size_sweep" :
    {
        "type" : "bug",
        "frequencies" : [9.4],
        "lengths" : full_size_sweep,
        "slants" : [1],
        "pitches" : [0,10],
    },
    "bird_full_size_sweep" :
        {
            "type" : "bird",
            "frequencies" : [3.0,5.6,9.4],
            "lengths" : full_size_sweep,
            "slants" : [1],
            "pitches" : [0,10],
        },
    "bird_xband_size_sweep" :
        {
            "type" : "bird",
            "frequencies" : [9.4],
            "lengths" : full_size_sweep,
            "slants" : [1],
            "pitches" : [0,10],
        },
    "EarthCare_small_insect" :
        {
            "type" : "bug",
            "frequencies" : [94],
            "lengths" : [5],
            "slants" : [-90],
            "pitches" : [0,10],
        },
    "EarthCare_medium_insect" :
        {
            "type" : "bug",
            "frequencies" : [94],
            "lengths" : [15],
            "slants" : [-90],
            "pitches" : [0,10],
        },
    "EarthCare_large_insect" :
        {
            "type" : "bug",
            "frequencies" : [94],
            "lengths" : [35,50],
            "slants" : [-90],
            "pitches" : [0,10],
        },
    "EarthCare_small_insect_35" :
        {
            "type" : "bug",
            "frequencies" : [35],
            "lengths" : [5],
            "slants" : [-90],
            "pitches" : [0],
        },
    "EarthCare_medium_insect_35" :
        {
            "type" : "bug",
            "frequencies" : [35],
            "lengths" : [15],
            "slants" : [-90],
            "pitches" : [0],
        },
    "EarthCare_large_insect_35" :
        {
            "type" : "bug",
            "frequencies" : [35],
            "lengths" : [35,50],
            "slants" : [-90],
            "pitches" : [0],
        },
    "EarthCare_martin_35" :
        {
            "type" : "bird",
            "frequencies" : [35],
            "lengths" : [125],
            "slants" : [-90],
            "pitches" : [0],
        },
    "EarthCare_falcon_35" :
        {
            "type" : "bird",
            "frequencies" : [35],
            "lengths" : [500],
            "slants" : [-90],
            "pitches" : [0],
        },
    "EarthCare_martin_94" :
        {
            "type" : "bird",
            "frequencies" : [94],
            "lengths" : [125],
            "slants" : [-90],
            "pitches" : [0],
        },
    "EarthCare_falcon_94" :
        {
            "type" : "bird",
            "frequencies" : [94],
            "lengths" : [500],
            "slants" : [-90],
            "pitches" : [0],
        },
    "Earthcare_spheroid" :
        {
            "type" : "bird",
            "frequencies" : [35,94],
            "lengths" : [100,200],
            "slants" : [-90],
            "pitches" : [0],
        },
    "insect_finer_size_sweep" :
    {
        "type" : "bug",
        "frequencies" : [9.4,5.6,3.0],
        "lengths" : finer_size_sweep,
        "slants" : [1],
        "pitches" : [0],
    },
    "bird_finer_size_sweep" :
        {
            "type" : "bird",
            "frequencies" : [9.4,5.6,3.0],
            "lengths" : finer_size_sweep,
            "slants" : [1],
            "pitches" : [0],
        },
}