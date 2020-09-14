from datetime import datetime

import dateutil.parser as dp
import sanic
import sanic.response

import modules.stats


async def handler(req):
    await modules.stats.updatestats(req)

    seasonend="2020-11-30T13:00:00Z"
    seasonstart="2020-08-27T13:00:00Z"

    response = {
        'status': 200,
        'message': 'Everything should work fine',
        'data': {
            'DaysLeft': int((dp.parse(seasonend).timestamp()-datetime.utcnow().timestamp())/86400),
            'DaysGone': int((datetime.utcnow().timestamp()-dp.parse(seasonstart).timestamp())/86400),
            'SeasonLength': int((dp.parse(seasonend).timestamp()-dp.parse(seasonstart).timestamp())/86400)
        }
    }

    return sanic.response.json(response)