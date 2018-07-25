import globalPluginHandler
import api
import tones
import ui
import textInfos
from logHandler import log

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	savedCaret = None
	savedLine = None

	def _getLineNum(self):
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

		return lines

	def script_lineNumber(self, gesture):
		ui.message(str(self._getLineNum()))

	def script_saveCaret(self, gesture):
		focus = api.getFocusObject()
		textInfo = focus.makeTextInfo(textInfos.POSITION_CARET)
		if textInfo is not None:
			self.savedLine = self._getLineNum()
			self.savedCaret = textInfo
			ui.message("Saved cursor on line {}".format(self.savedLine))


	def script_restoreCaret(self, gesture):
		if self.savedCaret is not None:
			self.savedCaret.updateCaret()
			ui.message("Restored cursor to line {}".format(self.savedLine))


	__gestures={
		"kb:NVDA+g": "lineNumber",
		"kb:NVDA+s": "saveCaret",
		"kb:NVDA+r": "restoreCaret"
	}

	