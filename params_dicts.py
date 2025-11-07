PERMITTIVITY_DICT ={
    'bug' : {    
        5.6 :
        {
            'Re_body':43,
            'Im_body':19,
        },
        9.4 :
        {
            'Re_body':34,
            'Im_body':19,
        },
        3.0 :
        {
            'Re_body':53,
            'Im_body':19,
        },
    },
}


# Add optional Chitin parts
PARAMS_DICTS = {
    "hoverfly_test" : 
        {
            "frequencies" : [5.6],
            "lengths" : [12],
            "slants" : [0],
            "pitches" : [0]
        },
    "12mm_hoverfly_full" : 
        {
            "frequencies" : [5.6],
            "lengths" : [2,8,10,12,14,16,30],
            "slants" : [0],
            "pitches" : [0]
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
    "new_bug_standard" : 
        {
            "type" : "bug",
            "frequencies" : [5.6,9.4],
            "lengths" : [5,12,20],
            "slants" : [0],
            "pitches" : [0]
        }

}