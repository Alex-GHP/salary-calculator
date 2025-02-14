from constants import PAID_HOURS_PER_SHIFT, NIGHT_MULTIPLIER, WEEKEND_MULTIPLIER, NIGHT_AND_WEEKEND_MULTIPLIER

class Day():
    def __init__(self, day, shift, hourly_rate):
        self.day = day
        self.shift = shift
        self.hourly_rate = hourly_rate
    
    def get_money(self):
        pass

class Weekday(Day):
    def __init__(self, day, shift, hourly_rate):
        super().__init__(day, shift, hourly_rate)

    def get_money(self):
        night_hourly_rate = self.hourly_rate * NIGHT_MULTIPLIER
        match self.shift:
            case "NORMAL":
                return self.hourly_rate * PAID_HOURS_PER_SHIFT
            case "MORNING":
                return self.hourly_rate * PAID_HOURS_PER_SHIFT
            case "NIGHT":
                return night_hourly_rate * 8 + self.hourly_rate
            case "LATE":
                return self.hourly_rate * 8 + night_hourly_rate

class WeekendDay(Day):
    def __init__(self, day, shift, hourly_rate):
        super().__init__(day, shift, hourly_rate)
    
    def get_money(self):
        night_hourly_rate = self.hourly_rate * NIGHT_MULTIPLIER
        weekend_hourly_rate = self.hourly_rate * WEEKEND_MULTIPLIER
        night_and_weekend_hourly_rate = self.hourly_rate * NIGHT_AND_WEEKEND_MULTIPLIER

        if self.day == "friday" or self.day == "fridayph":
            match self.shift:
                case "NORMAL":
                    return weekend_hourly_rate * PAID_HOURS_PER_SHIFT
                case "MORNING":
                    return weekend_hourly_rate * PAID_HOURS_PER_SHIFT
                case "NIGHT":
                    return night_and_weekend_hourly_rate * 6 + night_hourly_rate * 2 + self.hourly_rate
                case "LATE":
                    return self.hourly_rate * 8 + night_and_weekend_hourly_rate
        elif self.day == "saturday" or self.day == "saturdayph":
            match self.shift:
                case "NORMAL":
                    return weekend_hourly_rate * PAID_HOURS_PER_SHIFT
                case "MORNING":
                    return weekend_hourly_rate * PAID_HOURS_PER_SHIFT
                case "NIGHT":
                    return night_and_weekend_hourly_rate * 8 + weekend_hourly_rate
                case "LATE":
                    return weekend_hourly_rate * 8 + night_and_weekend_hourly_rate
        else:
            match self.shift:
                case "NORMAL":
                    return weekend_hourly_rate * PAID_HOURS_PER_SHIFT
                case "MORNING":
                    return weekend_hourly_rate * PAID_HOURS_PER_SHIFT
                case "NIGHT":
                    return night_and_weekend_hourly_rate * 2 + night_hourly_rate * 6 + self.hourly_rate
                case "LATE":
                    return weekend_hourly_rate * 8 + night_and_weekend_hourly_rate
    