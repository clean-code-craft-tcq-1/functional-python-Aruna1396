import check_battery_limits as checker

if __name__ == '__main__':
    """ Test Function: is_battery_charging_health_status_normal """
    assert (checker.is_battery_charging_health_status_normal({'charging_temperature': 25, 'state_of_charge': 70,
                                                              'charge_rate': 0.8}) is True)
    assert (checker.is_battery_charging_health_status_normal({'charging_temperature': 125, 'state_of_charge': 70,
                                                              'charge_rate': 0.8}) is False)
    assert (checker.is_battery_charging_health_status_normal({'charging_temperature': 25, 'state_of_charge': 470,
                                                              'charge_rate': 0.8}) is False)
    assert (checker.is_battery_charging_health_status_normal({'charging_temperature': 25, 'state_of_charge': 70,
                                                              'charge_rate': 6.8}) is False)
    assert (checker.is_battery_charging_health_status_normal({'charging_temperature': 125, 'state_of_charge': 170,
                                                              'charge_rate': 0.8}) is False)
    assert (checker.is_battery_charging_health_status_normal({'charging_temperature': 125, 'state_of_charge': 170,
                                                              'charge_rate': 1.8}) is False)
    """ Test Function: collect_out_of_range_battery_parameters """

    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': 25, 'state_of_charge': 170,
                                                             'charge_rate': 1.8}) == ['state_of_charge', 'charge_rate'])
    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': 25, 'state_of_charge': 170,
                                                             'charge_rate': 0.8}) == ['state_of_charge'])
    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': 125, 'state_of_charge': 70,
                                                             'charge_rate': 0.8}) == ['charging_temperature'])
    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': 125, 'state_of_charge': 170,
                                                             'charge_rate': 1.8}) == ['charging_temperature',
                                                                                      'state_of_charge', 'charge_rate'])
    """ Test Function: check_is_battery_parameter_out_of_range """
    out_of_range_parameters = []
    checker.check_is_battery_parameter_out_of_range(out_of_range_parameters, 'charging_temperature', 125,
                                                    checker.battery_parameters_normal_range['charging_temperature'])
    assert (out_of_range_parameters == ['charging_temperature'])
    out_of_range_parameters = []
    checker.check_is_battery_parameter_out_of_range(out_of_range_parameters, 'charge_rate', 9.8,
                                                    checker.battery_parameters_normal_range['charge_rate'])
    assert (out_of_range_parameters == ['charge_rate'])
    out_of_range_parameters = []
    checker.check_is_battery_parameter_out_of_range(out_of_range_parameters, 'state_of_charge', 170,
                                                    checker.battery_parameters_normal_range['state_of_charge'])
    assert (out_of_range_parameters == ['state_of_charge'])
