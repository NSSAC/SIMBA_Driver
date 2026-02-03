import os
import sys
import argparse
import json

from pathlib import Path
from datetime import datetime
from abc import ABC, abstractmethod


class SimbaModule(ABC):
    def __init__(self):
        parser = argparse.ArgumentParser(description="SIMBA python module class.")
        parser.add_argument(
            "configuration",
            nargs=1,
            help="The configuration provided by SIMBA when called.",
        )

        arguments = parser.parse_args()
        self.configuration = Path(arguments.configuration[0])

        if (not self.configuration.is_absolute()) and Path.cwd().joinpath(
            self.configuration
        ).exists():
            self.configuration = Path.cwd().joinpath(self.configuration).absolute()

        self.load()

    def load(self):
        try:
            jsonFile = open(self.configuration, "r")

        except:
            sys.exit("ERROR: File '" + self.configuration + "' does not exist.")  # type: ignore

        dictionary = json.load(jsonFile)
        jsonFile.close()

        if not "mode" in dictionary:
            sys.exit(f"ERROR: Missing attribute mode in '{str(self.configuration)}'.")

        self.mode = dictionary["mode"]

        if not self.mode in ["start", "step", "end"]:
            sys.exit(f"ERROR: Invalid mode: '{self.mode}'.")

        if not "currentTick" in dictionary:
            sys.exit(
                f"ERROR: Missing attribute currentTick in '{str(self.configuration)}'."
            )

        self.currentTick = int(dictionary["currentTick"])

        if not "currentTime" in dictionary:
            sys.exit(
                f"ERROR: Missing attribute currentTime in '{str(self.configuration)}'."
            )

        self.currentTime = datetime.fromisoformat(dictionary["currentTime"])

        if not "tickFormat" in dictionary:
            sys.exit(f"ERROR: Missing attribute tickFormat in '{self.configuration}'.")

        self.tickFormat = dictionary["tickFormat"]

        if not "outputDirectory" in dictionary:
            sys.exit(
                f"ERROR: Missing attribute outputDirectory in '{self.configuration}'."
            )

        self.outputDirectory = Path(dictionary["outputDirectory"])

        self.statusFile = Path(
            str(str(self.configuration)).replace("module_", "status_")
        )

        if "statusFile" in dictionary:
            self.statusFile = Path(dictionary["statusFile"])

            if not self.statusFile.is_absolute():
                if self.configuration.parent.joinpath(self.statusFile).parent.exists():
                    self.statusFile = self.configuration.parent.joinpath(
                        self.statusFile
                    )
                else:
                    if Path.cwd().joinpath(self.statusFile).parent.exists():
                        self.statusFile = Path.cwd().joinpath(self.statusFile)

        self.lastRunTick = self.lastRunTick = (
            int(dictionary["lastRunTick"]) if "lastRunTick" in dictionary else None
        )

        if self.mode != "start" and not self.lastRunTick:
            sys.exit(f"ERROR: Missing attribute lastRunTick in '{self.configuration}'.")

        self.lastRunTime = (
            datetime.fromisoformat(dictionary["lastRunTime"])
            if "lastRunTime" in dictionary
            else None
        )

        if self.mode != "start" and not self.lastRunTime:
            sys.exit(f"ERROR: Missing attribute lastRunTime in '{self.configuration}'.")

        self.targetTick = (
            int(dictionary["targetTick"]) if "targetTick" in dictionary else None
        )

        if self.mode == "step" and not self.targetTick:
            sys.exit(f"ERROR: Missing attribute targetTick in '{self.configuration}'.")

        self.targetTime = (
            datetime.fromisoformat(dictionary["targetTime"])
            if "targetTime" in dictionary
            else None
        )

        if self.mode == "step" and not self.targetTime:
            sys.exit(f"ERROR: Missing attribute targetTime in '{self.configuration}'.")

        self.commonData = (
            dictionary["commonData"] if "commonData" in dictionary else None
        )
        self.moduleData = (
            dictionary["moduleData"] if "moduleData" in dictionary else None
        )

    def execute(self) -> bool:
        self.init()
        success = False
        if self.mode == "start":
            success = self.start()
        else:
            if self.mode == "step":
                success = self.step()
            else:
                if self.mode == "end":
                    success = self.step()

        dictionary = {}

        if self.statusFile.exists():
            try:
                jsonFile = open(self.statusFile, "r")

            except:
                sys.exit("ERROR: File '" + self.statusFile + "' does not exist.")  # type: ignore

            dictionary = json.load(jsonFile)
            jsonFile.close()

        dictionary["status"] = "success" if success else "failure"
        jsonFile = self.statusFile.open(mode="w")
        json.dump(dictionary, jsonFile, indent=2)
        jsonFile.close()

        return success

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def start(self) -> bool:
        return False

    @abstractmethod
    def step(self) -> bool:
        return False

    @abstractmethod
    def end(self) -> bool:
        return False
