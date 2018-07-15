import wpilib
import ctre

class CompetitionBot(wpilib.IterativeRobot):

    def robotInit(self):
        self.frontLeft = ctre.WPI_TalonSRX(2)
        self.frontRight = ctre.WPI_TalonSRX(1)
        self.backLeft = ctre.WPI_TalonSRX(0)
        self.backRight = ctre.WPI_TalonSRX(3)

        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        pass # your code goes here!

if __name__ == "__main__":
    wpilib.run(CompetitionBot, physics_enabled=True)
