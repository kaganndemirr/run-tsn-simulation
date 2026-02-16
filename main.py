import json
import logging
import os
import argparse

import constants
import topology_files

parser = argparse.ArgumentParser(prog='run_tsn_simulation')
parser.add_argument('-debug', help='Enable debug mode', type=bool)
parser.add_argument('-scenario', help='Scenarios (Choices: mcdm_2_3_4, springer, ijcs)')

args = parser.parse_args()

debug = args.debug
scenario = args.scenario

# opening the JSON file
data = open('input.json')

# deserializing the data
data = json.load(data)

os.chdir(os.path.join(os.path.expanduser("~"), "tsn-simulation"))

logging.basicConfig(level=logging.INFO)


logger = logging.getLogger()


scenario_dict = dict

if scenario == constants.MCDM_2_3_4:
    scenario_dict = topology_files.mcdm_2_3_4
elif scenario == constants.SPRINGER:
    scenario_dict = topology_files.springer
elif scenario == constants.ijcs:
    scenario_dict = topology_files.ijcs

for key, value in data.items():
    for experiment in value:
        if "Shortest_Path" == experiment['name']:
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
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wsmNormalization {experiment['wsmNormalization']} -wSRT {experiment['wSRT'][w_index]} -wTT {experiment['wTT'][w_index]} -wLength {experiment['wLength'][w_index]} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -lwr {experiment['lwr']}"
                            if logger.isEnabledFor(logging.DEBUG):
                                logging.debug(run_string)
                            else:
                                os.system(run_string)

        if "LWR_WPM_v1" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        for w_index in range(len(experiment['wSRT'])):
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -wSRT {experiment['wSRT'][w_index]} -wTT {experiment['wTT'][w_index]} -wLength {experiment['wLength'][w_index]} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -lwr {experiment['lwr']}"
                            if logger.isEnabledFor(logging.DEBUG):
                                logging.debug(run_string)
                            else:
                                os.system(run_string)

        if "LWR_WPM_v2" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        for w_index in range(len(experiment['wSRT'])):
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']} -wSRT {experiment['wSRT'][w_index]} -wTT {experiment['wTT'][w_index]} -wLength {experiment['wLength'][w_index]} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -lwr {experiment['lwr']}"
                            if logger.isEnabledFor(logging.DEBUG):
                                logging.debug(run_string)
                            else:
                                os.system(run_string)

        if "CWR_WSM" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wsmNormalization {experiment['wsmNormalization']} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -cwr {experiment['cwr']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "CWR_WPM_v1" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -cwr {experiment['cwr']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "CWR_WPM_v2" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -cwr {experiment['cwr']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "LWR_CWR_WSM" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wsmNormalization {experiment['wsmNormalization']} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -lwr {experiment['lwr']} -cwr {experiment['cwr']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "LWR_CWR_WPM_v1" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -lwr {experiment['lwr']} -cwr {experiment['cwr']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "LWR_CWR_WPM_v2" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -unicastCandidateSortingMethod {experiment['unicastCandidateSortingMethod']} -mcdmObjective {experiment['mcdmObjective']} -mcdmName {experiment['mcdmName']} -wpmVersion {experiment['wpmVersion']} -wpmValueType {experiment['wpmValueType']} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']} -lwr {experiment['lwr']} -cwr {experiment['cwr']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "MTR_v1_Average" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -mtrName {experiment['mtrName']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)

        if "MTR_Hierarchical_KMeans" == experiment['name']:
            for topology_key, application_value in scenario_dict.items():
                for application in application_value:
                    for k in experiment['k']:
                        if experiment['vtNumber'] is None:
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -mtrName {experiment['mtrName']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']}"
                        else:
                            run_string = f"java -jar target/tsn-simulation-1.0-SNAPSHOT-jar-with-dependencies.jar -net {topology_key} -app {application} -rate {experiment['rate']} -routing {experiment['routing']} -mtrName {experiment['mtrName']} -vtNumber {experiment['vtNumber']} -pathFindingMethod {experiment['pathFindingMethod']} -algorithm {experiment['algorithm']} -idleSlope {experiment['idleSlope']} -tsnSimulationVersion {experiment['tsnSimulationVersion']} -evaluatorName {experiment['evaluatorName']} -k {k} -threadNumber {experiment['threadNumber']} -timeout {experiment['timeout']} -metaheuristicName {experiment['metaheuristicName']}"
                        if logger.isEnabledFor(logging.DEBUG):
                            logging.debug(run_string)
                        else:
                            os.system(run_string)