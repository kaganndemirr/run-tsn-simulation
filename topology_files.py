import os

mcdm_2_3_4= {
    # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "ABB.xml"): [
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T1.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T2.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T3.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T4.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T5.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T6.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T7.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T8.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T9.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T10.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T11.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T12.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T13.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T14.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T15.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T16.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T17.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T18.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T19.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T20.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T21.xml"),
    #     # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2,3,4",
    #     #              "ABB_T22.xml")
    # ]

    # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "ORION.xml"): [
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "ORION_Unicast_AVB_Deadline", "ORION_T1.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "ORION_Unicast_AVB_Deadline", "ORION_T2.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "ORION_Unicast_AVB_Deadline", "ORION_T3.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "ORION_Unicast_AVB_Deadline", "ORION_T4.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "ORION_Unicast_AVB_Deadline", "ORION_T5.xml")],

    # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "TC", "TC1.xml"): [
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC1_T1.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC1_T2.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC1_T3.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC1_T4.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC1_T5.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC1_T6.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC1_T7.xml"), ],
    #
    # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "TC", "TC3.xml"): [
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC3_T8.xml"), ],

    os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "TC", "TC5.xml"): [
        # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
        #               "TC_Unicast", "2,3,4", "TC5_T10.xml"),
        # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
        #              "TC_Unicast", "2,3,4", "TC5_T11.xml"),
        # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
        #              "TC_Unicast", "2,3,4", "TC5_T12.xml"),
        # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
        #              "TC_Unicast", "2,3,4", "TC5_T13.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC_Unicast", "2,3,4", "TC5_T14.xml"),
        # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
        #              "TC_Unicast", "2,3,4", "TC5_T15.xml"),
        # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
        #              "TC_Unicast", "2,3,4", "TC5_T16.xml"),
        # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
        #              "TC_Unicast", "2,3,4", "TC5_T17.xml"),
    ],

    # os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "TC",  "TC7.xml"): [
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC7_T10.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC7_T15.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC7_T16.xml"),
    #     os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
    #                  "TC_Unicast", "2,3,4" "TC7_T17.xml"),
    # ],
}

springer = {
    os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "ABB.xml"): [
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T1.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T2.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T3.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T4.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T5.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T6.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T7.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T8.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T9.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T10.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T11.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T12.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T13.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T14.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T15.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T16.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T17.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T18.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T19.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T20.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T21.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application", "ABB_Unicast", "2",
                     "ABB_T22.xml")
    ],

    os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "architecture", "TC", "TC1.xml"): [
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                      "TC1_Unicast_Springer", "TC1_T1.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC1_Unicast_Springer", "TC1_T2.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC1_Unicast_Springer", "TC1_T3.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC1_Unicast_Springer", "TC1_T4.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC1_Unicast_Springer", "TC1_T5.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC1_Unicast_Springer", "TC1_T6.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC1_Unicast_Springer", "TC1_T7.xml"),
        os.path.join(os.path.expanduser("~"), "tsn-simulation", "resources", "application",
                     "TC1_Unicast_Springer", "TC1_T8.xml"),
    ]
}
