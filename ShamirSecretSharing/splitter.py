#!/usr/bin/env python

import sys
import argparse

from core import *

if sys.version_info > (3,):
    long = int

# An 8192 bit prime that is used as a default prime
DEFAULT_PRIME = 950687172821200540428729809153981241192606941085199889710006512529799315561656564788637203101376144614649190146776378362001933636271697777317137481911233025291081331157135314582760768668046936978951230131371278628451555794052066356238840168982528971519323334381994143826200392654688774136120844941887558297071490087973944885778003973836311019785751636542119444349041852180595146239058424861988708991060298944680661305392492285898022705075814390941667822309754536610263449507491311215196067928669134842614154655850281748314529232542980764185554607592605321212081871630106290126123668106453941684604069442637972979374182617204123679546880646955063471680804611387541602675808433185504968764805413712115090234016146947180827040328391684056285942239977920347896230959546196177226139807640271414022569186565510341302134143539867133746492544472279859740722443892721076576952182274117616122050429733446090321598356954337536610713395670667775788540830077914016236382546944507664840405622352934380411525395863579062612404875578114927946272686172750421522119335879522375883064090902859635110578120928185659759792150776022992518497479844711483878613494426215867980856381040745252296584054718251345106582780587533445417441424957999212662923937862802426711722066998062574441680275377501049078991123518677027512513302350533057609106549686502083785061647562269181863107725160293272971931807381453849850066056697913028167183570392948696346480930400320904644898839942228059188904225142187444604612121676565893284697317106343998167640380023972222033520190994951064491572372368101650142992876761420785551386138148283615194775971673577063363049929945959258097086463812469068598955485574579363616634109593903116561526921965491646400040600138481505369027344295330767163087489333402201631708610718911106905154471963379233672543874307197342217544783263700843246351822145605839955798639016346308363889766574606793652730311687899415585873892778899179927359964882217066947566799298173326850382334054179474389651499891117938361854701587568363867264590395711833275763832842002504433841816245069655064326325306033334336469743800464944131049874472540605264250854258280373869113420817955012823462838351481855289027030577957168468047751024562853260494808998446682723835213272609799649864902376137320638444968430858790173696935815430513690803796736064125183005539073920032869713201073105497655763097638587404309062750746064609677994654409535743453776560694719663801069746654445359756195253816544699551

def main():
    parser = argparse.ArgumentParser(description="Secret Splitter")
    parser.add_argument('--number', type=int, required=True,
           help='Number of shares to which the secret will be split')
    parser.add_argument('--threshold', type=int, required=True,
           help='Minimum number of shares needed to reconstruct the secret')
    parser.add_argument('--secret', type=long, required=True,
           help='The secret to be split (used only in the split mode)')
    parser.add_argument('--prime', type=long,
           default=DEFAULT_PRIME,
           help='Prime used as the basis of Galois field')
    
    args = parser.parse_args()
  
    shares = split_secret(args.secret,
                          args.number,
                          args.threshold,
                          args.prime)
    if shares == None:
        sys.stderr.write("Error: Unable to split secret!\n")
    else:
        print_shares(shares)
        

if __name__ == "__main__":
    main()
    sys.exit(0)
