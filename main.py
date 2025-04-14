# importing the module
import json
import os
import logging

import topology_files

# opening the JSON file
data = open('input.json')

# deserializing the data
data = json.load(data)

os.chdir(os.path.join(os.path.expanduser("~"), "tsn-simulation"))

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

for key, value in data.items():
    for experiment in value:
        if "shortestPath" == experiment['pathFindingMethod']:
            for topology_key, application_value in topology_files.topology_application_dict_2_3_4.items():
                for application in application_value:
                    run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -rate {experiment['rate']}"
                    if logger.isEnabledFor(logging.DEBUG):
                        logging.debug(run_string)
                    else:
                        os.system(run_string)


        if "U" == experiment['algorithm']:
            for topology_key, application_value in topology_files.topology_application_dict_2_3_4.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -rate {experiment['rate']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)


        if "RO" == experiment['algorithm']:
            for topology_key, application_value in topology_files.topology_application_dict_2_3_4.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -rate {experiment['rate']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        # if "PHYWSMCWR" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 if applicationvalue == "ABB_T22":
        #                     run_string = f"java -Dorg.slf4j.simpleLogger.defaultLogLevel=debug -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mcdmObjective {experiment['mcdmObjective']} -cwr {experiment['cwr']} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -tsnSimulationVersion {experiment['tsnSimulationVersion']}"
        #                 else:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mcdmObjective {experiment['mcdmObjective']} -cwr {experiment['cwr']} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -tsnSimulationVersion {experiment['tsnSimulationVersion']}"
        #                 if logger.isEnabledFor(logging.DEBUG):
        #                     logging.debug(run_string)
        #                 else:
        #                     os.system(run_string)

        # if "PHYWPMCWR" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mcdmObjective {experiment['mcdmObjective']} -cwr {experiment['cwr']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']}"
        #                 if logger.isEnabledFor(logging.DEBUG):
        #                     logging.debug(run_string)
        #                 else:
        #                     os.system(run_string)

        # elif "PHYWSM" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 for iii in experiment['wValues']:
        #                     if applicationvalue == "ABB_T22":
        #                         run_string = f"java -Dorg.slf4j.simpleLogger.defaultLogLevel=debug -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -mcdmObjective {experiment['mcdmObjective']} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -tsnSimulationVersion {experiment['tsnSimulationVersion']}"
        #                     else:
        #                         run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -mcdmObjective {experiment['mcdmObjective']} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -tsnSimulationVersion {experiment['tsnSimulationVersion']}"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)

        # elif "PHYWPM" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 for iii in experiment['wValues']:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -mcdmObjective {experiment['mcdmObjective']} -wSRT {iii["wSRT"]} -wTT {iii["wTT"]} -wLength {iii["wLength"]} -wUtil {iii["wUtil"]} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']}"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)



        # elif "PHYWSMLWR" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 for iii in experiment['wValues']:
        #                     if applicationvalue == "ABB_T22":
        #                         run_string = f"java -Dorg.slf4j.simpleLogger.defaultLogLevel=debug -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mcdmObjective {experiment['mcdmObjective']} -lwr {experiment['lwr']} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -tsnSimulationVersion {experiment['tsnSimulationVersion']}"
        #                     else:
        #                         run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mcdmObjective {experiment['mcdmObjective']} -lwr {experiment['lwr']} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -tsnSimulationVersion {experiment['tsnSimulationVersion']}"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)

        # elif "PHYWPMLWR" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 for iii in experiment['wValues']:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -mcdmObjective {experiment['mcdmObjective']} -wSRT {iii["wSRT"]} -wTT {iii["wTT"]} -wLength {iii["wLength"]} -wUtil {iii["wUtil"]} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']} -lwr {experiment['lwr']}"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)
        #
        # elif "PHYWPMLWRCWR" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 for iii in experiment['wValues']:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -mcdmObjective {experiment['mcdmObjective']} -wSRT {iii["wSRT"]} -wTT {iii["wTT"]} -wLength {iii["wLength"]} -wUtil {iii["wUtil"]} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']} -cwr {experiment['cwr']} -lwr {experiment['lwr']}"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)

        # elif "mtrmcdm" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 for iii in experiment['wValues']:
        #                     if experiment['overload']:
        #                         run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -cObjective {experiment['cObjective']} -wSRT {iii["wSRT"]} -wTT {iii["wTT"]} -wLength {iii["wLength"]} -wUtil {iii["wUtil"]} -mtrname {experiment['mtrname']} -overload"
        #                         if logger.isEnabledFor(logging.DEBUG):
        #                             logging.debug(run_string)
        #                         else:
        #                             os.system(run_string)
        #                     else:
        #                         run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -cObjective {experiment['cObjective']} -wSRT {iii["wSRT"]} -wTT {iii["wTT"]} -wLength {iii["wLength"]} -wUtil {iii["wUtil"]} -mtrname {experiment['mtrname']}"
        #                         if logger.isEnabledFor(logging.DEBUG):
        #                             logging.debug(run_string)
        #                         else:
        #                             os.system(run_string)
        #
        # elif "mtrlwr" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 for iii in experiment['wValues']:
        #                     if experiment['overload']:
        #                         run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -cObjective {experiment['cObjective']} -wSRT {iii["wSRT"]} -wTT {iii["wTT"]} -wLength {iii["wLength"]} -wUtil {iii["wUtil"]} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mtrname {experiment["mtrname"]} -randomizationlwr {experiment['randomizationlwr']} -overload"
        #                         if logger.isEnabledFor(logging.DEBUG):
        #                             logging.debug(run_string)
        #                         else:
        #                             os.system(run_string)
        #                     else:
        #                         run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -cObjective {experiment['cObjective']} -wSRT {iii["wSRT"]} -wTT {iii["wTT"]} -wLength {iii["wLength"]} -wUtil {iii["wUtil"]} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mtrname {experiment["mtrname"]} -randomizationlwr {experiment['randomizationlwr']}"
        #                         if logger.isEnabledFor(logging.DEBUG):
        #                             logging.debug(run_string)
        #                         else:
        #                             os.system(run_string)
        #
        # elif "mtrcwr" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 if experiment['overload']:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -cObjective {experiment['cObjective']} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mtrname {experiment["mtrname"]} -randomizationcwr {experiment['randomizationcwr']} -overload"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)
        #                 else:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -cObjective {experiment['cObjective']} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mtrname {experiment["mtrname"]} -randomizationcwr {experiment['randomizationcwr']}"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)
        #
        # elif "mtrlwrcwr" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 if experiment['overload']:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -cObjective {experiment['cObjective']} -randomizationcwr {experiment['randomizationcwr']} -randomizationlwr {experiment['randomizationlwr']} -mtrname {experiment["mtrname"]} -overload"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)
        #                 else:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -cObjective {experiment['cObjective']} -randomizationcwr {experiment['randomizationcwr']} -randomizationlwr {experiment['randomizationlwr']} -mtrname {experiment["mtrname"]} -overload"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)
        #
        # elif "mtrv1" == experiment['experimentType']:
        #     for topologykey, applicationvalue in topology_files.topology_application_dict_2_3_4.items():
        #         for i in applicationvalue:
        #             for ii in experiment['kValues']:
        #                 if experiment['overload']:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mtrname {experiment["mtrname"]} -overload"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)
        #                 else:
        #                     run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topologykey} -app {i} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -k {ii} -ba {experiment['ba']} -timeout {experiment['timeout']} -threadNumber {experiment['threadNumber']} -mtrname {experiment["mtrname"]}"
        #                     if logger.isEnabledFor(logging.DEBUG):
        #                         logging.debug(run_string)
        #                     else:
        #                         os.system(run_string)
