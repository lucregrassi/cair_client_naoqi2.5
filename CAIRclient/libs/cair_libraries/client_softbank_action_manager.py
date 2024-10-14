import qi
from naoqi import ALProxy
import time
import re


class ActionManager(object):
    def __init__(self, logger):
        super(ActionManager, self).__init__()
        self.memory = ALProxy("ALMemory")
        self.server_ip = self.memory.getData("CAIR/server_ip")
        self.voice_speed = self.memory.getData("CAIR/voice_speed")
        self.behavior_manager = ALProxy("ALBehaviorManager")
        self.animated_speech = ALProxy("ALAnimatedSpeech")
        self.configuration = {"bodyLanguageMode": "contextual"}
        self.tablet = True
        self.logger = logger
        try:
            self.tablet_service = ALProxy("ALTabletService")
        except:
            self.tablet = False

    def perform_action(self, item):
        action = re.findall("action=(\w+)", item)[0]
        self.logger.info(action)
        if action == "volume":
            if self.behavior_manager.isBehaviorInstalled("utility/volume"):
                level = re.findall("level=(\w+)", item)[0]
                self.logger.info(level)
                self.memory.insertData("CAIR/volume_level", level)
                self.behavior_manager.runBehavior("utility/volume")
                while self.behavior_manager.isBehaviorRunning("utility/volume"):
                    time.sleep(0.1)

        elif action == "voicespeed":
            if self.behavior_manager.isBehaviorInstalled("utility/voice_speed"):
                level = re.findall("level=(\w+)", item)[0]
                self.logger.info(level)
                self.memory.insertData("CAIR/voice_speed_level", level)
                self.behavior_manager.runBehavior("utility/voice_speed")
                while self.behavior_manager.isBehaviorRunning("utility/voice_speed"):
                    time.sleep(0.1)
                self.voice_speed = "\\RSPD=" + str(self.memory.getData("CAIR/voice_speed")) + "\\"

        elif action == "hello" or action == "attention":
            if self.behavior_manager.isBehaviorInstalled("greetings/hello"):
                self.behavior_manager.runBehavior("greetings/hello")
                while self.behavior_manager.isBehaviorRunning("greetings/hello"):
                    time.sleep(0.1)

        elif action == "namaste":
            if self.behavior_manager.isBehaviorInstalled("greetings/namaste"):
                self.behavior_manager.runBehavior("greetings/namaste")
                while self.behavior_manager.isBehaviorRunning("greetings/namaste"):
                    time.sleep(0.1)

        elif action == "konnichiwa":
            if self.behavior_manager.isBehaviorInstalled("greetings/konnichiwa"):
                self.behavior_manager.runBehavior("greetings/konnichiwa")
                while self.behavior_manager.isBehaviorRunning("greetings/konnichiwa"):
                    time.sleep(0.1)

        elif action == "time":
            if self.behavior_manager.isBehaviorInstalled("timetools/time"):
                self.behavior_manager.runBehavior("timetools/time")
                while self.behavior_manager.isBehaviorRunning("timetools/time"):
                    time.sleep(0.1)

        elif action == "date":
            if self.behavior_manager.isBehaviorInstalled("timetools/date"):
                self.behavior_manager.runBehavior("timetools/date")
                while self.behavior_manager.isBehaviorRunning("timetools/date"):
                    time.sleep(0.1)

        elif action == "weather":
            if self.behavior_manager.isBehaviorInstalled("weatherforecast/weather"):
                city = re.findall("city=(.*)", item)[0]
                self.logger.info(city)
                self.memory.insertData("CAIR/weather_city", city)
                self.behavior_manager.runBehavior("weatherforecast/weather")
                while self.behavior_manager.isBehaviorRunning("weatherforecast/weather"):
                    time.sleep(0.1)

        elif action == "playsong":
            if self.behavior_manager.isBehaviorInstalled("musicplayer/play-video"):
                title = re.findall("title=(.*)", item)[0]
                self.logger.info(title)
                self.memory.insertData("CAIR/song_title", title)
                self.memory.insertData("CAIR/server_ip", self.server_ip)
                self.behavior_manager.runBehavior("musicplayer/play-video")
                while self.behavior_manager.isBehaviorRunning("musicplayer/play-video"):
                    time.sleep(0.1)

        elif action == "playkaraoke":
            if self.behavior_manager.isBehaviorInstalled("karaokeplayer/play-karaoke"):
                title = re.findall("title=(.*)", item)[0]
                self.logger.info(title)
                self.memory.insertData("CAIR/karaoke_title", title)
                self.behavior_manager.runBehavior("karaokeplayer/play-karaoke")
                while self.behavior_manager.isBehaviorRunning("karaokeplayer/play-karaoke"):
                    time.sleep(0.1)

        elif action == "wikisearch":
            if self.behavior_manager.isBehaviorInstalled("wordtools/wikisearch"):
                what = re.findall("what=(.*)", item)[0]
                self.logger.info(what)
                self.memory.insertData("CAIR/wikisearch", what)
                self.behavior_manager.runBehavior("wordtools/wikisearch")
                while self.behavior_manager.isBehaviorRunning("wordtools/wikisearch"):
                    time.sleep(0.1)

        elif action == "translate":
            if self.behavior_manager.isBehaviorInstalled("wordtools/translator"):
                language = re.findall("language=(\w+)", item)[0]
                self.logger.info(language)
                self.memory.insertData("CAIR/translate_lan", language)
                what = re.findall("what=(.*)", item)[0]
                self.logger.info(what)
                self.memory.insertData("CAIR/translate_text", what)
                self.behavior_manager.runBehavior("wordtools/translator")
                while self.behavior_manager.isBehaviorRunning("wordtools/translator"):
                    time.sleep(0.1)

        elif action == "dictionary":
            if self.behavior_manager.isBehaviorInstalled("wordtools/dictionary"):
                what = re.findall("what=(.*)", item)[0]
                self.logger.info(what)
                self.memory.insertData("CAIR/dictionary", what)
                self.behavior_manager.runBehavior("wordtools/dictionary")
                while self.behavior_manager.isBehaviorRunning("wordtools/dictionary"):
                    time.sleep(0.1)

        elif action == "move":
            if self.behavior_manager.isBehaviorInstalled("movement/move"):
                where = re.findall("where=(\w+)", item)[0]
                self.logger.info(where)
                self.memory.insertData("CAIR/move", where)
                self.behavior_manager.runBehavior("movement/move")
                while self.behavior_manager.isBehaviorRunning("movement/move"):
                    time.sleep(0.1)

        elif action == "go":
            if self.behavior_manager.isBehaviorInstalled("movement/move"):
                where = re.findall("where=(\w+)", item)[0]
                self.logger.info(where)
                self.memory.insertData("CAIR/go", where)
                self.behavior_manager.runBehavior("movement/go")
                while self.behavior_manager.isBehaviorRunning("movement/go"):
                    time.sleep(0.1)

        elif action == "learnplace":
            if self.behavior_manager.isBehaviorInstalled("movement/learn_place"):
                where = re.findall("where=(.*)", item)[0]
                self.logger.info(where)
                self.memory.insertData("CAIR/learn_place", where)
                self.behavior_manager.runBehavior("movement/learn_place")
                while self.behavior_manager.isBehaviorRunning("movement/learn_place"):
                    time.sleep(0.1)

        elif action == "setposition":
            if self.behavior_manager.isBehaviorInstalled("movement/set_position"):
                where = re.findall("where=(.*)", item)[0]
                self.logger.info(where)
                self.memory.insertData("CAIR/set_position", where)
                self.behavior_manager.runBehavior("movement/set_position")
                while self.behavior_manager.isBehaviorRunning("movement/set_position"):
                    time.sleep(0.1)

        elif action == "goto":
            if self.behavior_manager.isBehaviorInstalled("movement/go_to"):
                where = re.findall("where=(.*)", item)[0]
                self.logger.info(where)
                self.memory.insertData("CAIR/go_to", where)
                self.behavior_manager.runBehavior("movement/go_to")
                while self.behavior_manager.isBehaviorRunning("movement/go_to"):
                    time.sleep(0.1)

        elif action == "rest":
            # Check if the docking station was in the map
            if self.memory.getData("CAIR/go_to_outcome"):
                if self.tablet:
                    if self.behavior_manager.isBehaviorInstalled("movement/rest"):
                        # Execute this behavior only on Pepper.
                        self.behavior_manager.runBehavior("movement/rest")
                        while self.behavior_manager.isBehaviorRunning("movement/rest"):
                            time.sleep(0.1)
                self.memory.removeData("CAIR/go_to_outcome")

        elif action == "wakeup":
            if self.tablet:
                if self.behavior_manager.isBehaviorInstalled("movement/wakeup"):
                    # Execute this behavior only on Pepper.
                    self.behavior_manager.runBehavior("movement/wakeup")
                    while self.behavior_manager.isBehaviorRunning("movement/wakeup"):
                        time.sleep(0.1)

        elif action == "forgetmap":
            if self.behavior_manager.isBehaviorInstalled("movement/forget_map"):
                self.behavior_manager.runBehavior("movement/forget_map")
                while self.behavior_manager.isBehaviorRunning("movement/forget_map"):
                    time.sleep(0.1)

        elif action == "hug":
            if self.behavior_manager.isBehaviorInstalled("affectivecommunication/hug"):
                self.behavior_manager.runBehavior("affectivecommunication/hug")
                while self.behavior_manager.isBehaviorRunning("affectivecommunication/hug"):
                    time.sleep(0.1)

        elif action == "handshake":
            if self.behavior_manager.isBehaviorInstalled("affectivecommunication/handshake"):
                self.behavior_manager.runBehavior("affectivecommunication/handshake")
                while self.behavior_manager.isBehaviorRunning("affectivecommunication/handshake"):
                    time.sleep(0.1)

        elif action == "privacy":
            if self.behavior_manager.isBehaviorInstalled("provideprivacy/privacy"):
                self.behavior_manager.runBehavior("provideprivacy/privacy")
                while self.behavior_manager.isBehaviorRunning("provideprivacy/privacy"):
                    time.sleep(0.1)

        elif action == "followme":
            if self.behavior_manager.isBehaviorInstalled("follow-me/."):
                self.behavior_manager.runBehavior("follow-me/.")
                while self.behavior_manager.isBehaviorRunning("follow-me/."):
                    time.sleep(0.1)

        elif action == "playmovie":
            if self.behavior_manager.isBehaviorInstalled("movieplayer/play-movie"):
                title = re.findall("title=(.*)", item)[0]
                self.logger.info(title)
                self.memory.insertData("CAIR/movie_title", title)
                self.behavior_manager.runBehavior("movieplayer/play-movie")
                while self.behavior_manager.isBehaviorRunning("movieplayer/play-movie"):
                    time.sleep(0.1)

        elif action == "showinstructions":
            if self.behavior_manager.isBehaviorInstalled("videoinstructions/show-instructions"):
                what = re.findall("what=(.*)", item)[0]
                self.logger.info(what)
                self.memory.insertData("CAIR/instructions", what)
                self.behavior_manager.runBehavior("videoinstructions/show-instructions")
                while self.behavior_manager.isBehaviorRunning("videoinstructions/show-instructions"):
                    time.sleep(0.1)

        elif action == "showexercise":
            if self.behavior_manager.isBehaviorInstalled("videoexercises/play-exercise"):
                what = re.findall("what=(.*)", item)[0]
                self.logger.info(what)
                self.memory.insertData("CAIR/exercise", what)
                self.behavior_manager.runBehavior("videoexercises/play-exercise")
                while self.behavior_manager.isBehaviorRunning("videoexercises/play-exercise"):
                    time.sleep(0.1)
