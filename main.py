# importing the module
import json
import logging
import os

import topology_files

# opening the JSON file
data = open('input.json')

# deserializing the data
data = json.load(data)

scenario_dict = topology_files.springer_dict

os.chdir(os.path.join(os.path.expanduser("~"), "tsn-simulation"))

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()

for key, value in data.items():
    for experiment in value:
        if "shortestPath" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']}"
                    if logger.isEnabledFor(logging.DEBUG):
                        logging.debug(run_string)
                    else:
                        os.system(run_string)

        if "U" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "RO" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "MCDM_WSM" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        for w_index in range(len(experiment['wSRT'])):
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wsmNormalization {experiment['wsmNormalization']} -wSRT {experiment['wSRT'][w_index]} -wTT {experiment['wTT'][w_index]} -wLength {experiment['wLength'][w_index]}"
                            if logger.isEnabledFor(logging.DEBUG):
                                logging.debug(run_string)
                            else:
                                os.system(run_string)

        if "MCDM_WPM_v1" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        for w_index in range(len(experiment['wSRT'])):
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -wSRT {experiment['wSRT'][w_index]} -wTT {experiment['wTT'][w_index]} -wLength {experiment['wLength'][w_index]}"
                            if logger.isEnabledFor(logging.DEBUG):
                                logging.debug(run_string)
                            else:
                                os.system(run_string)

        if "MCDM_WPM_v2" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        for w_index in range(len(experiment['wSRT'])):
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']} -wSRT {experiment['wSRT'][w_index]} -wTT {experiment['wTT'][w_index]} -wLength {experiment['wLength'][w_index]}"
                            if logger.isEnabledFor(logging.DEBUG):
                                logging.debug(run_string)
                            else:
                                os.system(run_string)


        if "LWR_WSM" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        for w_index in range(len(experiment['wSRT'])):
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']} -wSRT {experiment['wSRT'][w_index]} -wTT {experiment['wTT'][w_index]} -wLength {experiment['wLength'][w_index]}"
                            if logger.isEnabledFor(logging.DEBUG):
                                logging.debug(run_string)
                            else:
                                os.system(run_string)