'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from . import cmudict
from hparams import hparams

_pad        = '_'
_eos        = '~'
_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'\"(),-.:;? '
_numbers = '123456'

phonemes_thchs30 = ['a1', 'a2', 'a3', 'a4', 'a5', 'aa', 'ai1', 'ai2', 'ai3', 'ai4', 'ai5', 'an1', 'an2', 'an3', 'an4', 'an5', 'ang1', 'ang2', 'ang3', 'ang4', 'ang5', 'ao1', 'ao2', 'ao3', 'ao4', 'ao5', 'b', 'c', 'ch', 'd', 'e1', 'e2', 'e3', 'e4', 'e5', 'ee', 'ei1', 'ei2', 'ei3', 'ei4', 'ei5', 'en1', 'en2', 'en3', 'en4', 'en5', 'eng1', 'eng2', 'eng3', 'eng4', 'eng5', 'er2', 'er3', 'er4', 'er5', 'f', 'g', 'h', 'i1', 'i2', 'i3', 'i4', 'i5', 'ia1', 'ia2', 'ia3', 'ia4', 'ia5', 'ian1', 'ian2', 'ian3', 'ian4', 'ian5', 'iang1', 'iang2', 'iang3', 'iang4', 'iang5', 'iao1', 'iao2', 'iao3', 'iao4', 'iao5', 'ie1', 'ie2', 'ie3', 'ie4', 'ie5', 'ii', 'in1', 'in2', 'in3', 'in4', 'in5', 'ing1', 'ing2', 'ing3', 'ing4', 'ing5', 'iong1', 'iong2', 'iong3', 'iong4', 'iong5', 'iu1', 'iu2', 'iu3', 'iu4', 'iu5', 'ix1', 'ix2', 'ix3', 'ix4', 'ix5', 'iy1', 'iy2', 'iy3', 'iy4', 'iy5', 'iz4', 'iz5', 'j', 'k', 'l', 'm', 'n', 'o1', 'o2', 'o3', 'o4', 'o5', 'ong1', 'ong2', 'ong3', 'ong4', 'ong5', 'oo', 'ou1', 'ou2', 'ou3', 'ou4', 'ou5', 'p', 'q', 'r', 's', 'sh', 'sil', 't', 'u1', 'u2', 'u3', 'u4', 'u5', 'ua1', 'ua2', 'ua3', 'ua4', 'ua5', 'uai1', 'uai2', 'uai3', 'uai4', 'uai5', 'uan1', 'uan2', 'uan3', 'uan4', 'uan5', 'uang1', 'uang2', 'uang3', 'uang4', 'uang5', 'ueng1', 'ueng3', 'ueng4', 'ueng5', 'ui1', 'ui2', 'ui3', 'ui4', 'ui5', 'un1', 'un2', 'un3', 'un4', 'un5', 'uo1', 'uo2', 'uo3', 'uo4', 'uo5', 'uu', 'v1', 'v2', 'v3', 'v4', 'v5', 'van1', 'van2', 'van3', 'van4', 'van5', 've1', 've2', 've3', 've4', 've5', 'vn1', 'vn2', 'vn3', 'vn4', 'vn5', 'vv', 'x', 'z', 'zh']

phonemes_aishell = ['uang1', 'ao3', 'ai3', 'uai4', 'van3', 'in2', 'ei5', 'oo', 'i3', 'eng1', 'e5', 'ang3', 'e1', 'an5', 'uan5', 'er3', 'vn1', 'ou2', 'iao5', 'iong4', 'ao2', 'vn5', 'ang5', 'ix5', 'en1', 'ing2', 'ing5', 'uo2', 've4', 'eng2', 'ong3', 'uo3', 'iao2', 'ui2', 'iy4', 'u3', 'ua5', 'van2', 'ei4', 'ian3', 'en3', 'ueng3', 'c', 'v4', 'iang5', 'ong2', 'van1', 'i1', 'iang3', 'er2', 'u5', 'ou3', 'van4', 'ian1', 'er5', 'uai1', 'u2', 'iang1', 'u4', 'i2', 'ia1', 'ia5', 'ie1', 't', 'd', 'o2', 'ao4', 'in1', 'i5', 'iu1', 'k', 'uang2', 'i4', 've3', 'u1', 'vv', 'l', 'uai3', 'e3', 'iao1', 'uang3', 'iu4', 'ing4', 'g', 'ian5', 'iy1', 'a4', 'uan1', 'ei3', 'ai1', 'zh', 'sh', 'o1', 'uang5', 'v2', 'ueng1', 'iu3', 'ui4', 'eng3', 'iao4', 'p', 'ai4', 's', 'iy3', 'x', 'er4', 'ang4', 'ui5', 'ao5', 'uo5', 'uan3', 'en4', 'v5', 'iang4', 'n', 'o5', 'j', 'iu2', 'iy2', 'a5', 'f', 'ai2', 'v3', 'uan2', 'uai5', 'iu5', 'iong3', 'in5', 'uo4', 'an1', 'eng4', 'an4', 'un2', 'an3', 'ua1', 'in3', 'ee', 'ian4', 'ie2', 'uan4', 'ui3', 'ia4', 'o4', 'e2', 'ix4', 'ueng5', 'm', 'a3', 'ong1', 've2', 'uu', 'ie4', 'ang1', 've1', 'ei2', 'ang2', 'un3', 'ian2', 'iong5', 'ix2', 'ou5', 'un4', 'sil', 'iz4', 'e4', 'b', 'ou1', 'ua2', 'ch', 'iy5', 'ie3', 'q', 'vn3', 'aa', 'ai5', 'ui1', 'van5', 'uang4', 'uo1', 'r', 'z', 'vn4', 'ueng4', 'ei1', 'en5', 'a2', 'ing3', 'a1', 've5', 'ing1', 'ia3', 'iong1', 'eng5', 'v1', 'ong4', 'un5', 'an2', 'ii', 'ix3', 'vn2', 'ua3', 'iong2', 'iao3', 'iang2', 'en2', 'ie5', 'un1', 'ong5', 'ix1', 'ia2', 'o3', 'h', 'ou4', 'in4', 'uai2', 'ua4', 'ao1']

cantonese_initials = ['b', 'c', 'd', 'f', 'g', 'gw', 'h', 'j', 'k', 'kw', 'l', 'm', 'n', 'ng', 'p', 's', 't', 'w', 'z']
cantonese_finals = ['aa1', 'aa2', 'aa3', 'aa4', 'aa5', 'aa6',
  'aai1', 'aai2', 'aai3', 'aai4', 'aai5', 'aai6',
  'aak1', 'aak3', 'aak6', 'aam1', 'aam2', 'aam3', 'aam4', 'aam5', 'aam6',
  'aan1', 'aan2', 'aan3', 'aan4', 'aan5', 'aan6',
  'aang1', 'aang2', 'aang3', 'aang4', 'aang5', 'aang6',
  'aap1', 'aap3', 'aap6',
  'aat1', 'aat3', 'aat6',
  'aau1', 'aau2', 'aau3', 'aau4', 'aau5', 'aau6',
  'ai1', 'ai2', 'ai3', 'ai4', 'ai5', 'ai6',
  'ak1', 'ak3', 'ak6',
  'am1', 'am2', 'am3', 'am4', 'am5', 'am6',
  'an1', 'an2', 'an3', 'an4', 'an5', 'an6',
  'ang1', 'ang2', 'ang3', 'ang4', 'ang5', 'ang6',
  'ap1', 'ap3', 'ap6', 'at1', 'at3', 'at6',
  'au1', 'au2', 'au3', 'au4', 'au5', 'au6',
  'e1', 'e2', 'e3', 'e4', 'e5', 'e6',
  'ei1', 'ei2', 'ei3', 'ei4', 'ei5', 'ei6',
  'ek1', 'ek3', 'ek6',
  'em2',
  'eng1', 'eng2', 'eng3', 'eng4', 'eng5', 'eng6',
  'eoi1', 'eoi2', 'eoi3', 'eoi4', 'eoi5', 'eoi6',
  'eon1', 'eon2', 'eon3', 'eon4', 'eon5', 'eon6',
  'eot1', 'eot6',
  'ep6', 'eu6',
  'i1', 'i2', 'i3', 'i4', 'i5', 'i6',
  'ik1', 'ik3', 'ik6',
  'im1', 'im2', 'im3', 'im4', 'im5', 'im6',
  'in1', 'in2', 'in3', 'in4', 'in5', 'in6',
  'ing1', 'ing2', 'ing3', 'ing4', 'ing5', 'ing6',
  'ip1', 'ip2', 'ip3', 'ip6',
  'it1', 'it3', 'it6',
  'iu1', 'iu2', 'iu3', 'iu4', 'iu5', 'iu6',
  'm1', 'm2', 'm4', 'm6',
  'ng2', 'ng4', 'ng5', 'ng6',
  'o1', 'o2', 'o3', 'o4', 'o5', 'o6',
  'oe1', 'oe2', 'oe3', 'oe4', 'oe5',
  'oek3', 'oek6',
  'oeng1', 'oeng2', 'oeng3', 'oeng4', 'oeng5', 'oeng6',
  'oi1', 'oi2', 'oi3', 'oi4', 'oi5', 'oi6',
  'ok1', 'ok3', 'ok6',
  'on1', 'on2', 'on3', 'on4', 'on5', 'on6',
  'ong1', 'ong2', 'ong3', 'ong4', 'ong5', 'ong6',
  'ot3', 'ot6', 'ou1', 'ou2', 'ou3', 'ou4', 'ou5', 'ou6',
  'u1', 'u2', 'u3', 'u4', 'u5', 'u6',
  'ui1', 'ui2', 'ui3', 'ui4', 'ui5', 'ui6',
  'uk1', 'uk3', 'uk6',
  'un1', 'un2', 'un3', 'un4', 'un5', 'un6',
  'ung1', 'ung2', 'ung3', 'ung4', 'ung5', 'ung6',
  'ut3', 'ut6',
  'yu1', 'yu2', 'yu3', 'yu4', 'yu5', 'yu6',
  'yun1', 'yun2', 'yun3', 'yun4', 'yun5', 'yun6',
  'yut3', 'yut6',
  'aap2', 'aak2', 'aat2', 'ap2', 'oek1', 'oek2', 'eo4', 'ok2', 'ak2', 'eot2', 'ek2', 'uk2']

# Export all symbols:
if hparams.symbol_set == 'thchs30':
  symbols = [_pad, _eos] + phonemes_thchs30
  print('Using phonemes for THCHS30 dataset as input symbols.')
elif hparams.symbol_set == 'aishell':
  symbols = [_pad, _eos] + phonemes_aishell
  print('Using phonemes for AISHELL dataset as input symbols.')
elif hparams.symbol_set == 'cantonese':
  symbols = [_pad, _eos] + ['-'] + cantonese_initials + cantonese_finals
  print('Using phonemes for Cantonese as input symbols.')
else:
  symbols = [_pad, _eos] + list(_characters) + list(_numbers)
  print('Using characters as input symbols.')
