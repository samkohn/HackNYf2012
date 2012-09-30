# -*- coding: utf-8 -*-

###############################################################################
#
# LogFood
# Log a new food entry for a particular date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LogFood(Choreography):

    """
    Create a new instance of the LogFood Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/LogFood')


    def new_input_set(self):
        return LogFoodInputSet()

    def _make_result_set(self, result, path):
        return LogFoodResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogFoodChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LogFood
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LogFoodInputSet(InputSet):
        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Amount input for this choreography. ((required, integer) The amount of food consumed formatted like X.XX. Note that this input corresponds with the UnitId input.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the ConsumerKey input for this choreography. ((required, string) The Consumer Key provided by Fitbit.)
        """
        def set_ConsumerKey(self, value):
            InputSet._set_input(self, 'ConsumerKey', value)

        """
        Set the value of the ConsumerSecret input for this choreography. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        def set_ConsumerSecret(self, value):
            InputSet._set_input(self, 'ConsumerSecret', value)

        """
        Set the value of the Date input for this choreography. ((required, date) The date that corresponds with the new log entry (in the format yyyy-MM-dd).)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Favorite input for this choreography. ((optional, boolean) Set to 1 to add food to favorites after creating log entry. Defaults to 0 for false.)
        """
        def set_Favorite(self, value):
            InputSet._set_input(self, 'Favorite', value)

        """
        Set the value of the FoodId input for this choreography. ((required, integer) The id of the food to create a log entry for.)
        """
        def set_FoodId(self, value):
            InputSet._set_input(self, 'FoodId', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) The format that you want the response to be in: xml or json. Defaults to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the MealType input for this choreography. ((required, string) The type of meal. Valid values: Breakfast, Morning Snack, Lunch, Afternoon Snack, Dinner, Anytime.)
        """
        def set_MealType(self, value):
            InputSet._set_input(self, 'MealType', value)

        """
        Set the value of the UnitId input for this choreography. ((required, integer) This id can be retrieved through other calls such as: Get Foods (Recent, Frequent, Favorite), Search Foods or Get Food Units.)
        """
        def set_UnitId(self, value):
            InputSet._set_input(self, 'UnitId', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the LogFood choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LogFoodResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Fitbit.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LogFoodChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogFoodResultSet(response, path)
