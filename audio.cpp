#include "audio.h"
#include <iostream>

static AlphabetPlayer alphabet_player = AlphabetPlayer();


int isReady(void) { return alphabet_player.isReady(); }

void setChannels(int i_nchannels) { alphabet_player.setChannels(i_nchannels); }

const int *getCurLetterTimes(int *o_size)
{
    const std::vector< int > &letter_times =
        alphabet_player.getCurLetterTimes();
    *o_size = letter_times.size();
    return &letter_times[0];
}
