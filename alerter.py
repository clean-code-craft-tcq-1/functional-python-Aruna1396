
"""
    This function is to create an alert (Email/Logger) with a detailed report and
    define next actions based on the battery health status
"""


def report_severity_of_battery_health_breach(out_of_range_battery_parameters):
    if len(out_of_range_battery_parameters) >= 2:
        print('\n Battery Breach Critical Alert', ' \n Severity_level : High',
              ' \n Abnormal readings obtained for parameters:\t', ','.join(out_of_range_battery_parameters),
              '\n BMS detected abnormal conditions, Charging Stopped immediately')
    else:
        print('\n Battery Breach Alert', ' \n Severity_level : Low',
              ' \n Abnormal readings obtained for parameter:\t', ','.join(out_of_range_battery_parameters),
              '\n BMS detected abnormal condition, Notified the authorized personnel')


def report_normal_health_status():
    print("Battery Health is Good. No breach occurred")
