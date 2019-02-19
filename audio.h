#ifndef AUDIO_H
#define AUDIO_H

#ifdef __cplusplus
extern "C" {
#endif

int isReady(void);
void setChannels(int i_nchannels);


const int *getCurLetterTimes(int *o_size);

#ifdef __cplusplus
}
#endif

#endif
