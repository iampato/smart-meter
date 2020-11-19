from config.connect import SmartMeterConfig


def main():
    smartMeterConfig = SmartMeterConfig()
    print(smartMeterConfig.database_user)


if __name__ == "__main__":
    main()
