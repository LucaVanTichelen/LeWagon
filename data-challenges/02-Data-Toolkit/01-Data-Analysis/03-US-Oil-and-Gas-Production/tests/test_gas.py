from nbresult import ChallengeResultTestCase

class TestGas(ChallengeResultTestCase):
    def test_month_column_is_a_datetime(self):
        self.assertEqual(self.result.month_type, 'datetime64[ns]')

    def test_yearly_gas_production_df_has_the_right_shape(self):
        self.assertEqual(self.result.yearly_gas, (9, 19))
