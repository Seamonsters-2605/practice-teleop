import wpilib
import ctre

class CompetitionBot(wpilib.IterativeRobot):

    def robotInit(self):
        self.frontLeft = ctre.CANTalon(2)
        self.frontRight = ctre.CANTalon(1)
        self.backLeft = ctre.CANTalon(0)
        self.backRight = ctre.CANTalon(3)

        self.climber = ctre.CANTalon(4)
        self.flywheel = ctre.CANTalon(5)
        self.feeder = ctre.CANTalon(7)

        self.joystick = wpilib.Joystick(0)

        self.gearLight1 = wpilib.DigitalOutput(0)
        self.gearLight2 = wpilib.DigitalOutput(1)

    def teleopPeriodic(self):
        pass # your code goes here!

if __name__ == "__main__":
    wpilib.run(CompetitionBot, physics_enabled=True)
