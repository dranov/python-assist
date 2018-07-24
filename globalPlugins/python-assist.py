import globalPluginHandler
import api
import tones
import ui
import textInfos
from logHandler import log

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_lineNumber(self, gesture):
		focus = api.getFocusObject()
		textInfo = focus.makeTextInfo(textInfos.POSITION_CARET)
		textInfo.expand(textInfos.UNIT_LINE)

		lines = 1
		canDecrement = True
		while canDecrement:
			log.info("{} lines / obj {}".format(lines, textInfo))
			r = textInfo.move(textInfos.UNIT_LINE, -1)
			if r == 0:
				canDecrement = False
			else:
				lines += 1

		ui.message(str(lines))

	__gestures={
		"kb:NVDA+g": "lineNumber",
	}

	