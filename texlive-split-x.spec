%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-x
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tools.tar.xz
Source1426:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tools.doc.tar.xz
Source1517:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turabian-formatting.tar.xz
Source1518:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turabian-formatting.doc.tar.xz
Source2084:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tpslifonts.tar.xz
Source2085:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tpslifonts.doc.tar.xz
Source2087:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trajan.tar.xz
Source2088:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trajan.doc.tar.xz
Source2090:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txfontsb.tar.xz
Source2091:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txfontsb.doc.tar.xz
Source2093:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typicons.tar.xz
Source2094:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typicons.doc.tar.xz
Source2149:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/times.tar.xz
Source2150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tipa.tar.xz
Source2151:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tipa.doc.tar.xz
Source2152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txfonts.tar.xz
Source2153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txfonts.doc.tar.xz
Source2332:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tracklang.tar.xz
Source2333:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tracklang.doc.tar.xz
Source2475:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thalie.tar.xz
Source2476:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thalie.doc.tar.xz
Source2478:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tree-dvips.tar.xz
Source2479:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tree-dvips.doc.tar.xz
Source2506:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tram.tar.xz
Source2507:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tram.doc.tar.xz
Source2660:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlepages.doc.tar.xz
Source2661:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tlc2.doc.tar.xz
Source2705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turkmen.tar.xz
Source2706:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turkmen.doc.tar.xz
Source2735:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-array-fr.doc.tar.xz
Source2736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-dcolumn-fr.doc.tar.xz
Source2737:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-natbib-fr.doc.tar.xz
Source2738:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-tabbing-fr.doc.tar.xz
Source2781:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tipa-de.doc.tar.xz
Source2782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-arsclassica-de.doc.tar.xz
Source2783:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-biblatex-de.doc.tar.xz
Source2784:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-chemsym-de.doc.tar.xz
Source2785:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-ecv-de.doc.tar.xz
Source2786:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-enumitem-de.doc.tar.xz
Source2787:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-europecv-de.doc.tar.xz
Source2788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-filecontents-de.doc.tar.xz
Source2789:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translation-moreverb-de.doc.tar.xz
Source3103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typehtml.tar.xz
Source3104:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typehtml.doc.tar.xz
Source3292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ticollege.tar.xz
Source3293:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ticollege.doc.tar.xz
Source3294:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tipfr.doc.tar.xz
Source3295:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-3dplot.tar.xz
Source3296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-3dplot.doc.tar.xz
Source3297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-bayesnet.tar.xz
Source3298:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-bayesnet.doc.tar.xz
Source3299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-cd.tar.xz
Source3300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-cd.doc.tar.xz
Source3301:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-dependency.tar.xz
Source3302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-dependency.doc.tar.xz
Source3303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-dimline.tar.xz
Source3304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-dimline.doc.tar.xz
Source3305:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-inet.tar.xz
Source3306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-inet.doc.tar.xz
Source3307:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-opm.tar.xz
Source3308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-opm.doc.tar.xz
Source3309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-palattice.tar.xz
Source3310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-palattice.doc.tar.xz
Source3311:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-qtree.tar.xz
Source3312:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-qtree.doc.tar.xz
Source3313:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-timing.tar.xz
Source3314:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-timing.doc.tar.xz
Source3319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzinclude.tar.xz
Source3320:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzinclude.doc.tar.xz
Source3322:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzmark.tar.xz
Source3323:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzmark.doc.tar.xz
Source3325:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzorbital.tar.xz
Source3326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzorbital.doc.tar.xz
Source3327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzpagenodes.tar.xz
Source3328:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzpagenodes.doc.tar.xz
Source3330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzpfeile.tar.xz
Source3331:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzpfeile.doc.tar.xz
Source3333:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzposter.tar.xz
Source3334:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzposter.doc.tar.xz
Source3336:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzscale.tar.xz
Source3337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzscale.doc.tar.xz
Source3339:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzsymbols.tar.xz
Source3340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzsymbols.doc.tar.xz
Source3342:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/timing-diagrams.tar.xz
Source3343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/timing-diagrams.doc.tar.xz
Source3344:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tqft.tar.xz
Source3345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tqft.doc.tar.xz
Source3347:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-base.tar.xz
Source3348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-base.doc.tar.xz
Source3349:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-berge.tar.xz
Source3350:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-berge.doc.tar.xz
Source3351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-doc.tar.xz
Source3352:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-doc.doc.tar.xz
Source3353:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-euclide.tar.xz
Source3354:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-euclide.doc.tar.xz
Source3355:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-fct.tar.xz
Source3356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-fct.doc.tar.xz
Source3357:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-graph.tar.xz
Source3358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-graph.doc.tar.xz
Source3359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-kiviat.tar.xz
Source3360:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-kiviat.doc.tar.xz
Source3361:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-linknodes.tar.xz
Source3362:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-linknodes.doc.tar.xz
Source3363:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-orm.tar.xz
Source3364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-orm.doc.tar.xz
Source3365:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-tab.tar.xz
Source3366:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tkz-tab.doc.tar.xz
Source3367:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tsemlines.tar.xz
Source3368:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tufte-latex.tar.xz
Source3369:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tufte-latex.doc.tar.xz
Source5485:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/theoremref.tar.xz
Source5486:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/theoremref.doc.tar.xz
Source5487:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thinsp.tar.xz
Source5488:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thinsp.doc.tar.xz
Source5489:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thmtools.tar.xz
Source5490:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thmtools.doc.tar.xz
Source5492:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threadcol.tar.xz
Source5493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threadcol.doc.tar.xz
Source5495:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threeparttable.tar.xz
Source5496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threeparttable.doc.tar.xz
Source5497:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threeparttablex.tar.xz
Source5498:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threeparttablex.doc.tar.xz
Source5499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumb.tar.xz
Source5500:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumb.doc.tar.xz
Source5502:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumbs.tar.xz
Source5503:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumbs.doc.tar.xz
Source5505:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumby.tar.xz
Source5506:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumby.doc.tar.xz
Source5507:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ticket.tar.xz
Source5508:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ticket.doc.tar.xz
Source5509:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlecaps.tar.xz
Source5510:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlecaps.doc.tar.xz
Source5511:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlefoot.tar.xz
Source5512:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlepic.tar.xz
Source5513:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlepic.doc.tar.xz
Source5514:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titleref.tar.xz
Source5515:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titleref.doc.tar.xz
Source5516:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlesec.tar.xz
Source5517:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titlesec.doc.tar.xz
Source5518:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titling.tar.xz
Source5519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/titling.doc.tar.xz
Source5521:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocbibind.tar.xz
Source5522:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocbibind.doc.tar.xz
Source5524:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocloft.tar.xz
Source5525:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocloft.doc.tar.xz
Source5527:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocvsec2.tar.xz
Source5528:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocvsec2.doc.tar.xz
Source5530:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/todo.tar.xz
Source5531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/todo.doc.tar.xz
Source5533:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/todonotes.tar.xz
Source5534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/todonotes.doc.tar.xz
Source5536:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tokenizer.tar.xz
Source5537:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tokenizer.doc.tar.xz
Source5538:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/toolbox.tar.xz
Source5539:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/toolbox.doc.tar.xz
Source5541:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/topfloat.tar.xz
Source5542:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/topfloat.doc.tar.xz
Source5543:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/totcount.tar.xz
Source5544:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/totcount.doc.tar.xz
Source5546:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/totpages.tar.xz
Source5547:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/totpages.doc.tar.xz
Source5549:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translations.tar.xz
Source5550:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translations.doc.tar.xz
Source5551:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trfsigns.tar.xz
Source5552:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trfsigns.doc.tar.xz
Source5554:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trimspaces.tar.xz
Source5555:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trimspaces.doc.tar.xz
Source5557:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trivfloat.tar.xz
Source5558:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trivfloat.doc.tar.xz
Source5560:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trsym.tar.xz
Source5561:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trsym.doc.tar.xz
Source5563:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/truncate.tar.xz
Source5564:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/truncate.doc.tar.xz
Source5565:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tucv.tar.xz
Source5566:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tucv.doc.tar.xz
Source5568:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turnthepage.tar.xz
Source5569:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turnthepage.doc.tar.xz
Source5570:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/twoinone.tar.xz
Source5571:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/twoinone.doc.tar.xz
Source5572:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/twoup.tar.xz
Source5573:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/twoup.doc.tar.xz
Source5575:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txgreeks.tar.xz
Source5576:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txgreeks.doc.tar.xz
Source5578:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/type1cm.tar.xz
Source5579:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/type1cm.doc.tar.xz
Source5581:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typeface.tar.xz
Source5582:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typeface.doc.tar.xz
Source5584:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typogrid.tar.xz
Source5585:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typogrid.doc.tar.xz
Source5929:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thmbox.tar.xz
Source5930:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thmbox.doc.tar.xz
Source5932:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turnstile.tar.xz
Source5933:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turnstile.doc.tar.xz
Source6022:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threeddice.tar.xz
Source6023:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/threeddice.doc.tar.xz
Source6113:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/timetable.tar.xz
Source6114:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/treetex.tar.xz
Source6115:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/treetex.doc.tar.xz
Source6546:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thesis-ekf.tar.xz
Source6547:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thesis-ekf.doc.tar.xz
Source6549:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thesis-titlepage-fhac.tar.xz
Source6550:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thesis-titlepage-fhac.doc.tar.xz
Source6552:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thuthesis.tar.xz
Source6553:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thuthesis.doc.tar.xz
Source6555:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/toptesi.tar.xz
Source6556:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/toptesi.doc.tar.xz
Source6558:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tudscr.tar.xz
Source6559:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tudscr.doc.tar.xz
Source6561:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tugboat.tar.xz
Source6562:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tugboat.doc.tar.xz
Source6564:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tugboat-plain.tar.xz
Source6565:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tugboat-plain.doc.tar.xz
Source6566:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turabian.tar.xz
Source6567:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/turabian.doc.tar.xz
Source6568:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tui.tar.xz
Source6569:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tui.doc.tar.xz
Source6733:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/t-angles.tar.xz
Source6734:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/t-angles.doc.tar.xz
Source7528:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-feynman.tar.xz
Source7529:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-feynman.doc.tar.xz
Source7530:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tipfr.tar.xz
Source7531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typed-checklist.tar.xz
Source7532:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typed-checklist.doc.tar.xz
Source7968:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thaienum.tar.xz
Source7969:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thaienum.doc.tar.xz
Source7970:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-kalender.tar.xz
Source7971:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-kalender.doc.tar.xz
Source7972:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-optics.tar.xz
Source7973:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-optics.doc.tar.xz
Source7974:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzcodeblocks.tar.xz
Source7975:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzcodeblocks.doc.tar.xz
Source7976:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzducks.tar.xz
Source7977:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzducks.doc.tar.xz
Source7978:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzpeople.tar.xz
Source7979:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzpeople.doc.tar.xz
Source7984:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocdata.tar.xz
Source7985:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tocdata.doc.tar.xz
Source7986:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txuprcal.tar.xz
Source7987:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/txuprcal.doc.tar.xz
Source7988:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typoaid.tar.xz
Source7989:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typoaid.doc.tar.xz
Source8032:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translator.tar.xz
Source8033:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/translator.doc.tar.xz
Source8034:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-page.tar.xz
Source8035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-page.doc.tar.xz
Source8048:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trigonometry.doc.tar.xz
Source8049:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/trigonometry.tar.xz
Source8342:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thaispec.tar.xz
Source8343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thaispec.doc.tar.xz
Source8344:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thesis-gwu.tar.xz
Source8345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thesis-gwu.doc.tar.xz
Source8346:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thucoursework.tar.xz
Source8347:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thucoursework.doc.tar.xz
Source8348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-karnaugh.tar.xz
Source8349:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-karnaugh.doc.tar.xz
Source8350:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-ladder.tar.xz
Source8351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-ladder.doc.tar.xz
Source8352:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-layers.tar.xz
Source8353:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-layers.doc.tar.xz
Source8354:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzmarmots.tar.xz
Source8355:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikzmarmots.doc.tar.xz
Source8356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-nef.tar.xz
Source8357:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-nef.doc.tar.xz
Source8358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-network.tar.xz
Source8359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-network.doc.tar.xz
Source8360:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-relay.tar.xz
Source8361:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-relay.doc.tar.xz
Source8362:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-sfc.tar.xz
Source8363:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tikz-sfc.doc.tar.xz
Source8364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/timbreicmc.tar.xz
Source8365:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/timbreicmc.doc.tar.xz
Source8366:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tinos.tar.xz
Source8367:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tinos.doc.tar.xz
Source8368:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tlc-article.tar.xz
Source8369:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tlc-article.doc.tar.xz
Source8370:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/topletter.tar.xz
Source8371:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/topletter.doc.tar.xz
Source8374:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typewriter.tar.xz
Source8375:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typewriter.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-tools
Provides:       tex-tools = %{tl_version}
License:        LPPL 1.3
Summary:        The LaTeX standard tools bundle
Version:        svn47671
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(color.sty)
Provides:       tex(.tex) = %{tl_version}, tex(afterpage.sty) = %{tl_version}
Provides:       tex(array.sty) = %{tl_version}, tex(bm.sty) = %{tl_version}
Provides:       tex(calc.sty) = %{tl_version}, tex(dcolumn.sty) = %{tl_version}
Provides:       tex(delarray.sty) = %{tl_version}, tex(e.tex) = %{tl_version}
Provides:       tex(enumerate.sty) = %{tl_version}, tex(fontsmpl.sty) = %{tl_version}
Provides:       tex(fontsmpl.tex) = %{tl_version}, tex(ftnright.sty) = %{tl_version}
Provides:       tex(h.tex) = %{tl_version}, tex(hhline.sty) = %{tl_version}
Provides:       tex(indentfirst.sty) = %{tl_version}, tex(layout.sty) = %{tl_version}
Provides:       tex(longtable.sty) = %{tl_version}, tex(multicol.sty) = %{tl_version}
Provides:       tex(q.tex) = %{tl_version}, tex(r.tex) = %{tl_version}
Provides:       tex(rawfonts.sty) = %{tl_version}, tex(s.tex) = %{tl_version}
Provides:       tex(showkeys.sty) = %{tl_version}, tex(somedefs.sty) = %{tl_version}
Provides:       tex(tabularx.sty) = %{tl_version}, tex(thb.sty) = %{tl_version}
Provides:       tex(thc.sty) = %{tl_version}, tex(thcb.sty) = %{tl_version}
Provides:       tex(theorem.sty) = %{tl_version}, tex(thm.sty) = %{tl_version}
Provides:       tex(thmb.sty) = %{tl_version}, tex(thp.sty) = %{tl_version}
Provides:       tex(trace.sty) = %{tl_version}, tex(varioref.sty) = %{tl_version}
Provides:       tex(verbatim.sty) = %{tl_version}, tex(verbtest.tex) = %{tl_version}
Provides:       tex(x.tex) = %{tl_version}, tex(xr.sty) = %{tl_version}
Provides:       tex(xspace.sty) = %{tl_version}

%description -n texlive-tools
A collection of (variously) simple tools provided as part of
the LaTeX required tools distribution, comprising the packages:
afterpage, array, bm, calc, dcolumn, delarray, enumerate,
fileerr, fontsmpl, ftnright, hhline, indentfirst, layout,
longtable, multicol, rawfonts, showkeys, somedefs, tabularx,
theorem, trace, varioref, verbatim, xr, and xspace.

%package -n texlive-tools-doc
Summary:        Documentation for tools
Version:        svn47671
Provides:       tex-tools-doc
AutoReqProv:    No

%description -n texlive-tools-doc
Documentation for tools

%package -n texlive-turabian-formatting
Provides:       tex-turabian-formatting = %{tl_version}
License:        LPPL 1.3
Summary:        Formatting based on Turabian's Manual
Version:        svn48330
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(setspace.sty), tex(xifthen.sty), tex(etoolbox.sty), tex(geometry.sty)
Requires:       tex(nowidow.sty), tex(url.sty), tex(footmisc.sty), tex(fancyhdr.sty)
Requires:       tex(titlesec.sty), tex(quoting.sty), tex(flafter.sty), tex(caption.sty)
Requires:       tex(endnotes.sty)
Provides:       tex(turabian-formatting.sty) = %{tl_version}
Provides:       tex(turabian-researchpaper.cls) = %{tl_version}
Provides:       tex(turabian-thesis.cls) = %{tl_version}

%description -n texlive-turabian-formatting
The turabian-formatting package provides Chicago-style
formatting based on Kate L. Turabian's "A Manual for Writers of
Research Papers, Theses, and Dissertations: Chicago Style for
Students and Researchers" (8th edition).

%package -n texlive-turabian-formatting-doc
Summary:        Documentation for turabian-formatting
Version:        svn48330
Provides:       tex-turabian-formatting-doc
AutoReqProv:    No

%description -n texlive-turabian-formatting-doc
Documentation for turabian-formatting

%package -n texlive-tpslifonts
Provides:       tex-tpslifonts = %{tl_version}
License:        GPL+
Summary:        A LaTeX package for configuring presentation fonts
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(cmbright.sty), tex(eulervm.sty), tex(t1cmr.fd)
Requires:       tex(t1cmfr.fd), tex(t1cmdh.fd), tex(t1cmfib.fd), tex(t1cmss.fd)
Requires:       tex(t1cmtt.fd)
Provides:       tex(tpslifonts.sty) = %{tl_version}

%description -n texlive-tpslifonts
This package aims to improve of font readability in
presentations, especially with maths. The standard cm maths
fonts at large design sizes are difficult to read from far
away, especially at low resolutions and low contrast color
choice. Using this package leads to much better overall
readability of some font combinations. The package offers a
couple of 'harmonising' combinations of text and maths fonts
from the (distant) relatives of computer modern fonts, with a
couple of extras for optimising readability. Text fonts from
computer modern roman, computer modern sans serif, SliTeX
computer modern sans serif, computer modern bright, or concrete
roman are available, in addition to maths fonts from computer
modern maths, computer modern bright maths, or Euler fonts. The
package is part of the TeXPower bundle.

%package -n texlive-tpslifonts-doc
Summary:        Documentation for tpslifonts
Version:        svn42428
Provides:       tex-tpslifonts-doc
AutoReqProv:    No

%description -n texlive-tpslifonts-doc
Documentation for tpslifonts

%package -n texlive-trajan
Provides:       tex-trajan = %{tl_version}
License:        LPPL
Summary:        Fonts from the Trajan column in Rome
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(trajan.map) = %{tl_version}, tex(trjnr10.tfm) = %{tl_version}
Provides:       tex(trjnsl10.tfm) = %{tl_version}, tex(trjnr10.pfb) = %{tl_version}
Provides:       tex(trjnsl10.pfb) = %{tl_version}, tex(t1trjn.fd) = %{tl_version}
Provides:       tex(trajan.sty) = %{tl_version}

%description -n texlive-trajan
Provides fonts (both as Metafont source and in Adobe Type 1
format) based on the capitals carved on the Trajan column in
Rome in 114 AD, together with macros to access the fonts. Many
typographers think these rank first among the Roman's artistic
legacy. The font is uppercase letters together with some
punctuation and analphabetics; no lowercase or digits.

%package -n texlive-trajan-doc
Summary:        Documentation for trajan
Version:        svn15878.1.1

Provides:       tex-trajan-doc
AutoReqProv:    No

%description -n texlive-trajan-doc
Documentation for trajan

%package -n texlive-tram
Provides:       tex-tram = %{tl_version}
License:        LPPL
Summary:        Typeset tram boxes in LaTeX
Version:        svn29803.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tram.sty) = %{tl_version}

%description -n texlive-tram
Tram boxes are highlighted with patterns of dots; the package
defines an environment tram that typesets its content into a
tram box. The pattern used may be selected in an optional
argument to the environment.

%package -n texlive-tram-doc
Summary:        Documentation for tram
Version:        svn29803.0.2

Provides:       tex-tram-doc
AutoReqProv:    No

%description -n texlive-tram-doc
Documentation for tram

%package -n texlive-txfontsb
Provides:       tex-txfontsb = %{tl_version}
License:        GPL+
Summary:        Extensions to txfonts, using GNU Freefont
Version:        svn21578.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(txfonts.sty)
Provides:       tex(gptimes.enc) = %{tl_version}, tex(gptimesy.enc) = %{tl_version}
Provides:       tex(gptimes.map) = %{tl_version}, tex(gtimesb6a.tfm) = %{tl_version}
Provides:       tex(gtimesb6r.tfm) = %{tl_version}, tex(gtimesbi6a.tfm) = %{tl_version}
Provides:       tex(gtimesbi6r.tfm) = %{tl_version}, tex(gtimesg6r.tfm) = %{tl_version}
Provides:       tex(gtimesi6a.tfm) = %{tl_version}, tex(gtimesi6r.tfm) = %{tl_version}
Provides:       tex(gtimesrg6a.tfm) = %{tl_version}, tex(gtimessc6a.tfm) = %{tl_version}
Provides:       tex(gtimessc6r.tfm) = %{tl_version}, tex(gtimessco6a.tfm) = %{tl_version}
Provides:       tex(gtimessco6r.tfm) = %{tl_version}, tex(gtimesyb6a.tfm) = %{tl_version}
Provides:       tex(gtimesyb6r.tfm) = %{tl_version}, tex(gtimesybi6a.tfm) = %{tl_version}
Provides:       tex(gtimesybi6r.tfm) = %{tl_version}, tex(gtimesyg6r.tfm) = %{tl_version}
Provides:       tex(gtimesyi6a.tfm) = %{tl_version}, tex(gtimesyi6r.tfm) = %{tl_version}
Provides:       tex(gtimesyrg6a.tfm) = %{tl_version}, tex(gtimesysc6a.tfm) = %{tl_version}
Provides:       tex(gtimesysc6r.tfm) = %{tl_version}, tex(gtimesysco6a.tfm) = %{tl_version}
Provides:       tex(gtimesysco6r.tfm) = %{tl_version}, tex(timessc6a.tfm) = %{tl_version}
Provides:       tex(timessc6r.tfm) = %{tl_version}, tex(timessco6a.tfm) = %{tl_version}
Provides:       tex(timessco6r.tfm) = %{tl_version}, tex(FreeSerifb-SmallCaps.pfb) = %{tl_version}
Provides:       tex(FreeSerifb-SmallCapsAlt.pfb) = %{tl_version}
Provides:       tex(FreeSerifb.pfb) = %{tl_version}, tex(FreeSerifbBold.pfb) = %{tl_version}
Provides:       tex(FreeSerifbBoldItalic.pfb) = %{tl_version}
Provides:       tex(FreeSerifbItalic.pfb) = %{tl_version}
Provides:       tex(gtimesb6a.vf) = %{tl_version}, tex(gtimesbi6a.vf) = %{tl_version}
Provides:       tex(gtimesi6a.vf) = %{tl_version}, tex(gtimesrg6a.vf) = %{tl_version}
Provides:       tex(gtimessc6a.vf) = %{tl_version}, tex(gtimessco6a.vf) = %{tl_version}
Provides:       tex(gtimesyb6a.vf) = %{tl_version}, tex(gtimesybi6a.vf) = %{tl_version}
Provides:       tex(gtimesyi6a.vf) = %{tl_version}, tex(gtimesyrg6a.vf) = %{tl_version}
Provides:       tex(gtimesysc6a.vf) = %{tl_version}, tex(gtimesysco6a.vf) = %{tl_version}
Provides:       tex(timessc6a.vf) = %{tl_version}, tex(timessco6a.vf) = %{tl_version}
Provides:       tex(lgrtxr.fd) = %{tl_version}, tex(lgrtxrc.fd) = %{tl_version}
Provides:       tex(lgrtxry.fd) = %{tl_version}, tex(lgrtxryc.fd) = %{tl_version}
Provides:       tex(ot1txrc.fd) = %{tl_version}, tex(ot1txryc.fd) = %{tl_version}
Provides:       tex(txfontsb.sty) = %{tl_version}

%description -n texlive-txfontsb
A set of fonts that extend the txfonts bundle with small caps
and old style numbers, together with Greek support. The
extensions are made with modifications of the GNU Freefont.

%package -n texlive-txfontsb-doc
Summary:        Documentation for txfontsb
Version:        svn21578.1.1

Provides:       tex-txfontsb-doc
AutoReqProv:    No

%description -n texlive-txfontsb-doc
Documentation for txfontsb

%package -n texlive-typicons
Provides:       tex-typicons = %{tl_version}
License:        LPPL 1.3
Summary:        Font containing a set of web-related icons
Version:        svn37623.2.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(typicons.ttf) = %{tl_version}, tex(typicons.sty) = %{tl_version}

%description -n texlive-typicons
This package grants access to 336 web-related icons provided by
the included "Typicons" free font, designed by Stephen
Hutchings and released under the SIL Open Font License. See
http://www.typicons.com for more details about the font itself.
This package requires the fontspec package and either the
Xe(La)TeX or Lua(La)TeX engine to load the included ttf font.
Once the package is loaded, icons can be accessed through the
general \ticon command, which takes as argument the name of the
desired icon, or through direct commands specific to each icon.
The full list of icon designs, names and direct commands is
showcased in the manual.

%package -n texlive-typicons-doc
Summary:        Documentation for typicons
Version:        svn37623.2.0.7

Provides:       tex-typicons-doc
AutoReqProv:    No

%description -n texlive-typicons-doc
Documentation for typicons

%package -n texlive-times
Provides:       tex-times = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn35058.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(utm.map) = %{tl_version}, tex(psyro.tfm) = %{tl_version}
Provides:       tex(ptmb.tfm) = %{tl_version}, tex(ptmb7t.tfm) = %{tl_version}
Provides:       tex(ptmb8c.tfm) = %{tl_version}, tex(ptmb8r.tfm) = %{tl_version}
Provides:       tex(ptmb8t.tfm) = %{tl_version}, tex(ptmbc.tfm) = %{tl_version}
Provides:       tex(ptmbc7t.tfm) = %{tl_version}, tex(ptmbc8t.tfm) = %{tl_version}
Provides:       tex(ptmbi.tfm) = %{tl_version}, tex(ptmbi7t.tfm) = %{tl_version}
Provides:       tex(ptmbi8c.tfm) = %{tl_version}, tex(ptmbi8r.tfm) = %{tl_version}
Provides:       tex(ptmbi8t.tfm) = %{tl_version}, tex(ptmbo.tfm) = %{tl_version}
Provides:       tex(ptmbo7t.tfm) = %{tl_version}, tex(ptmbo8c.tfm) = %{tl_version}
Provides:       tex(ptmbo8r.tfm) = %{tl_version}, tex(ptmbo8t.tfm) = %{tl_version}
Provides:       tex(ptmr.tfm) = %{tl_version}, tex(ptmr7t.tfm) = %{tl_version}
Provides:       tex(ptmr8c.tfm) = %{tl_version}, tex(ptmr8r.tfm) = %{tl_version}
Provides:       tex(ptmr8rn.tfm) = %{tl_version}, tex(ptmr8t.tfm) = %{tl_version}
Provides:       tex(ptmrc.tfm) = %{tl_version}, tex(ptmrc7t.tfm) = %{tl_version}
Provides:       tex(ptmrc8t.tfm) = %{tl_version}, tex(ptmri.tfm) = %{tl_version}
Provides:       tex(ptmri7t.tfm) = %{tl_version}, tex(ptmri8c.tfm) = %{tl_version}
Provides:       tex(ptmri8r.tfm) = %{tl_version}, tex(ptmri8t.tfm) = %{tl_version}
Provides:       tex(ptmro.tfm) = %{tl_version}, tex(ptmro7t.tfm) = %{tl_version}
Provides:       tex(ptmro8c.tfm) = %{tl_version}, tex(ptmro8r.tfm) = %{tl_version}
Provides:       tex(ptmro8t.tfm) = %{tl_version}, tex(ptmrr8re.tfm) = %{tl_version}
Provides:       tex(ptmrre.tfm) = %{tl_version}, tex(ptmrrn.tfm) = %{tl_version}
Provides:       tex(zpsycmrv.tfm) = %{tl_version}, tex(zptmcm7m.tfm) = %{tl_version}
Provides:       tex(zptmcm7t.tfm) = %{tl_version}, tex(zptmcm7v.tfm) = %{tl_version}
Provides:       tex(zptmcm7y.tfm) = %{tl_version}, tex(zptmcmr.tfm) = %{tl_version}
Provides:       tex(zptmcmrm.tfm) = %{tl_version}, tex(zpzccmry.tfm) = %{tl_version}
Provides:       tex(utmb7t.tfm) = %{tl_version}, tex(utmb8c.tfm) = %{tl_version}
Provides:       tex(utmb8r.tfm) = %{tl_version}, tex(utmb8t.tfm) = %{tl_version}
Provides:       tex(utmbc7t.tfm) = %{tl_version}, tex(utmbc8t.tfm) = %{tl_version}
Provides:       tex(utmbi7t.tfm) = %{tl_version}, tex(utmbi8c.tfm) = %{tl_version}
Provides:       tex(utmbi8r.tfm) = %{tl_version}, tex(utmbi8t.tfm) = %{tl_version}
Provides:       tex(utmbo7t.tfm) = %{tl_version}, tex(utmbo8c.tfm) = %{tl_version}
Provides:       tex(utmbo8r.tfm) = %{tl_version}, tex(utmbo8t.tfm) = %{tl_version}
Provides:       tex(utmr7t.tfm) = %{tl_version}, tex(utmr8c.tfm) = %{tl_version}
Provides:       tex(utmr8r.tfm) = %{tl_version}, tex(utmr8t.tfm) = %{tl_version}
Provides:       tex(utmrc7t.tfm) = %{tl_version}, tex(utmrc8t.tfm) = %{tl_version}
Provides:       tex(utmri7t.tfm) = %{tl_version}, tex(utmri8c.tfm) = %{tl_version}
Provides:       tex(utmri8r.tfm) = %{tl_version}, tex(utmri8t.tfm) = %{tl_version}
Provides:       tex(utmro7t.tfm) = %{tl_version}, tex(utmro8c.tfm) = %{tl_version}
Provides:       tex(utmro8r.tfm) = %{tl_version}, tex(utmro8t.tfm) = %{tl_version}
Provides:       tex(utmb8a.pfb) = %{tl_version}, tex(utmbi8a.pfb) = %{tl_version}
Provides:       tex(utmr8a.pfb) = %{tl_version}, tex(utmri8a.pfb) = %{tl_version}
Provides:       tex(ptmb.vf) = %{tl_version}, tex(ptmb7t.vf) = %{tl_version}
Provides:       tex(ptmb8c.vf) = %{tl_version}, tex(ptmb8t.vf) = %{tl_version}
Provides:       tex(ptmbc.vf) = %{tl_version}, tex(ptmbc7t.vf) = %{tl_version}
Provides:       tex(ptmbc8t.vf) = %{tl_version}, tex(ptmbi.vf) = %{tl_version}
Provides:       tex(ptmbi7t.vf) = %{tl_version}, tex(ptmbi8c.vf) = %{tl_version}
Provides:       tex(ptmbi8t.vf) = %{tl_version}, tex(ptmbo.vf) = %{tl_version}
Provides:       tex(ptmbo7t.vf) = %{tl_version}, tex(ptmbo8c.vf) = %{tl_version}
Provides:       tex(ptmbo8t.vf) = %{tl_version}, tex(ptmr.vf) = %{tl_version}
Provides:       tex(ptmr7t.vf) = %{tl_version}, tex(ptmr8c.vf) = %{tl_version}
Provides:       tex(ptmr8t.vf) = %{tl_version}, tex(ptmrc.vf) = %{tl_version}
Provides:       tex(ptmrc7t.vf) = %{tl_version}, tex(ptmrc8t.vf) = %{tl_version}
Provides:       tex(ptmri.vf) = %{tl_version}, tex(ptmri7t.vf) = %{tl_version}
Provides:       tex(ptmri8c.vf) = %{tl_version}, tex(ptmri8t.vf) = %{tl_version}
Provides:       tex(ptmro.vf) = %{tl_version}, tex(ptmro7t.vf) = %{tl_version}
Provides:       tex(ptmro8c.vf) = %{tl_version}, tex(ptmro8t.vf) = %{tl_version}
Provides:       tex(ptmrre.vf) = %{tl_version}, tex(ptmrrn.vf) = %{tl_version}
Provides:       tex(zpsycmrv.vf) = %{tl_version}, tex(zptmcm7m.vf) = %{tl_version}
Provides:       tex(zptmcm7t.vf) = %{tl_version}, tex(zptmcm7v.vf) = %{tl_version}
Provides:       tex(zptmcm7y.vf) = %{tl_version}, tex(zptmcmr.vf) = %{tl_version}
Provides:       tex(zptmcmrm.vf) = %{tl_version}, tex(zpzccmry.vf) = %{tl_version}
Provides:       tex(utmb7t.vf) = %{tl_version}, tex(utmb8c.vf) = %{tl_version}
Provides:       tex(utmb8t.vf) = %{tl_version}, tex(utmbc7t.vf) = %{tl_version}
Provides:       tex(utmbc8t.vf) = %{tl_version}, tex(utmbi7t.vf) = %{tl_version}
Provides:       tex(utmbi8c.vf) = %{tl_version}, tex(utmbi8t.vf) = %{tl_version}
Provides:       tex(utmbo7t.vf) = %{tl_version}, tex(utmbo8c.vf) = %{tl_version}
Provides:       tex(utmbo8t.vf) = %{tl_version}, tex(utmr7t.vf) = %{tl_version}
Provides:       tex(utmr8c.vf) = %{tl_version}, tex(utmr8t.vf) = %{tl_version}
Provides:       tex(utmrc7t.vf) = %{tl_version}, tex(utmrc8t.vf) = %{tl_version}
Provides:       tex(utmri7t.vf) = %{tl_version}, tex(utmri8c.vf) = %{tl_version}
Provides:       tex(utmri8t.vf) = %{tl_version}, tex(utmro7t.vf) = %{tl_version}
Provides:       tex(utmro8c.vf) = %{tl_version}, tex(utmro8t.vf) = %{tl_version}
Provides:       tex(8rutm.fd) = %{tl_version}, tex(omlutm.fd) = %{tl_version}
Provides:       tex(omsutm.fd) = %{tl_version}, tex(ot1utm.fd) = %{tl_version}
Provides:       tex(t1utm.fd) = %{tl_version}, tex(ts1utm.fd) = %{tl_version}

%description -n texlive-times
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-tipa
Provides:       tex-tipa = %{tl_version}
License:        LPPL
Summary:        Fonts and macros for IPA phonetics characters
Version:        svn29349.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(tipx.sty), tex(fontenc.sty)
Provides:       tex(tipa.map) = %{tl_version}, tex(tipaprm.def) = %{tl_version}
Provides:       tex(xipaprm.def) = %{tl_version}, tex(tipa10.tfm) = %{tl_version}
Provides:       tex(tipa12.tfm) = %{tl_version}, tex(tipa17.tfm) = %{tl_version}
Provides:       tex(tipa8.tfm) = %{tl_version}, tex(tipa9.tfm) = %{tl_version}
Provides:       tex(tipab10.tfm) = %{tl_version}, tex(tipabs10.tfm) = %{tl_version}
Provides:       tex(tipabx10.tfm) = %{tl_version}, tex(tipabx12.tfm) = %{tl_version}
Provides:       tex(tipabx8.tfm) = %{tl_version}, tex(tipabx9.tfm) = %{tl_version}
Provides:       tex(tipasb10.tfm) = %{tl_version}, tex(tipasi10.tfm) = %{tl_version}
Provides:       tex(tipasl10.tfm) = %{tl_version}, tex(tipasl12.tfm) = %{tl_version}
Provides:       tex(tipasl8.tfm) = %{tl_version}, tex(tipasl9.tfm) = %{tl_version}
Provides:       tex(tipass10.tfm) = %{tl_version}, tex(tipass12.tfm) = %{tl_version}
Provides:       tex(tipass17.tfm) = %{tl_version}, tex(tipass8.tfm) = %{tl_version}
Provides:       tex(tipass9.tfm) = %{tl_version}, tex(tipats10.tfm) = %{tl_version}
Provides:       tex(tipatt10.tfm) = %{tl_version}, tex(tipatt12.tfm) = %{tl_version}
Provides:       tex(tipatt8.tfm) = %{tl_version}, tex(tipatt9.tfm) = %{tl_version}
Provides:       tex(tipx10.tfm) = %{tl_version}, tex(tipx12.tfm) = %{tl_version}
Provides:       tex(tipx17.tfm) = %{tl_version}, tex(tipx8.tfm) = %{tl_version}
Provides:       tex(tipx9.tfm) = %{tl_version}, tex(tipxb10.tfm) = %{tl_version}
Provides:       tex(tipxbs10.tfm) = %{tl_version}, tex(tipxbx10.tfm) = %{tl_version}
Provides:       tex(tipxbx12.tfm) = %{tl_version}, tex(tipxbx8.tfm) = %{tl_version}
Provides:       tex(tipxbx9.tfm) = %{tl_version}, tex(tipxsb10.tfm) = %{tl_version}
Provides:       tex(tipxsi10.tfm) = %{tl_version}, tex(tipxsl10.tfm) = %{tl_version}
Provides:       tex(tipxsl12.tfm) = %{tl_version}, tex(tipxsl8.tfm) = %{tl_version}
Provides:       tex(tipxsl9.tfm) = %{tl_version}, tex(tipxss10.tfm) = %{tl_version}
Provides:       tex(tipxss12.tfm) = %{tl_version}, tex(tipxss17.tfm) = %{tl_version}
Provides:       tex(tipxss8.tfm) = %{tl_version}, tex(tipxss9.tfm) = %{tl_version}
Provides:       tex(tipxts10.tfm) = %{tl_version}, tex(tipxtt10.tfm) = %{tl_version}
Provides:       tex(tipxtt12.tfm) = %{tl_version}, tex(tipxtt8.tfm) = %{tl_version}
Provides:       tex(tipxtt9.tfm) = %{tl_version}, tex(xipa10.tfm) = %{tl_version}
Provides:       tex(xipab10.tfm) = %{tl_version}, tex(xipabs10.tfm) = %{tl_version}
Provides:       tex(xipasb10.tfm) = %{tl_version}, tex(xipasi10.tfm) = %{tl_version}
Provides:       tex(xipasl10.tfm) = %{tl_version}, tex(xipass10.tfm) = %{tl_version}
Provides:       tex(xipx10.tfm) = %{tl_version}, tex(xipxb10.tfm) = %{tl_version}
Provides:       tex(xipxbs10.tfm) = %{tl_version}, tex(xipxsb10.tfm) = %{tl_version}
Provides:       tex(xipxsi10.tfm) = %{tl_version}, tex(xipxsl10.tfm) = %{tl_version}
Provides:       tex(xipxss10.tfm) = %{tl_version}, tex(tipa10.pfb) = %{tl_version}
Provides:       tex(tipa12.pfb) = %{tl_version}, tex(tipa17.pfb) = %{tl_version}
Provides:       tex(tipa8.pfb) = %{tl_version}, tex(tipa9.pfb) = %{tl_version}
Provides:       tex(tipab10.pfb) = %{tl_version}, tex(tipabs10.pfb) = %{tl_version}
Provides:       tex(tipabx10.pfb) = %{tl_version}, tex(tipabx12.pfb) = %{tl_version}
Provides:       tex(tipabx8.pfb) = %{tl_version}, tex(tipabx9.pfb) = %{tl_version}
Provides:       tex(tipasb10.pfb) = %{tl_version}, tex(tipasi10.pfb) = %{tl_version}
Provides:       tex(tipasl10.pfb) = %{tl_version}, tex(tipasl12.pfb) = %{tl_version}
Provides:       tex(tipasl8.pfb) = %{tl_version}, tex(tipasl9.pfb) = %{tl_version}
Provides:       tex(tipass10.pfb) = %{tl_version}, tex(tipass12.pfb) = %{tl_version}
Provides:       tex(tipass17.pfb) = %{tl_version}, tex(tipass8.pfb) = %{tl_version}
Provides:       tex(tipass9.pfb) = %{tl_version}, tex(tipats10.pfb) = %{tl_version}
Provides:       tex(tipatt10.pfb) = %{tl_version}, tex(tipatt12.pfb) = %{tl_version}
Provides:       tex(tipatt8.pfb) = %{tl_version}, tex(tipatt9.pfb) = %{tl_version}
Provides:       tex(tipx10.pfb) = %{tl_version}, tex(tipx12.pfb) = %{tl_version}
Provides:       tex(tipx17.pfb) = %{tl_version}, tex(tipx8.pfb) = %{tl_version}
Provides:       tex(tipx9.pfb) = %{tl_version}, tex(tipxb10.pfb) = %{tl_version}
Provides:       tex(tipxbs10.pfb) = %{tl_version}, tex(tipxbx10.pfb) = %{tl_version}
Provides:       tex(tipxbx12.pfb) = %{tl_version}, tex(tipxbx8.pfb) = %{tl_version}
Provides:       tex(tipxbx9.pfb) = %{tl_version}, tex(tipxsb10.pfb) = %{tl_version}
Provides:       tex(tipxsi10.pfb) = %{tl_version}, tex(tipxsl10.pfb) = %{tl_version}
Provides:       tex(tipxsl12.pfb) = %{tl_version}, tex(tipxsl8.pfb) = %{tl_version}
Provides:       tex(tipxsl9.pfb) = %{tl_version}, tex(tipxss10.pfb) = %{tl_version}
Provides:       tex(tipxss12.pfb) = %{tl_version}, tex(tipxss17.pfb) = %{tl_version}
Provides:       tex(tipxss8.pfb) = %{tl_version}, tex(tipxss9.pfb) = %{tl_version}
Provides:       tex(tipxts10.pfb) = %{tl_version}, tex(tipxtt10.pfb) = %{tl_version}
Provides:       tex(tipxtt12.pfb) = %{tl_version}, tex(tipxtt8.pfb) = %{tl_version}
Provides:       tex(tipxtt9.pfb) = %{tl_version}, tex(xipa10.pfb) = %{tl_version}
Provides:       tex(xipab10.pfb) = %{tl_version}, tex(xipabs10.pfb) = %{tl_version}
Provides:       tex(xipasb10.pfb) = %{tl_version}, tex(xipasi10.pfb) = %{tl_version}
Provides:       tex(xipasl10.pfb) = %{tl_version}, tex(xipass10.pfb) = %{tl_version}
Provides:       tex(xipx10.pfb) = %{tl_version}, tex(xipxb10.pfb) = %{tl_version}
Provides:       tex(xipxbs10.pfb) = %{tl_version}, tex(xipxsb10.pfb) = %{tl_version}
Provides:       tex(xipxsi10.pfb) = %{tl_version}, tex(xipxsl10.pfb) = %{tl_version}
Provides:       tex(xipxss10.pfb) = %{tl_version}, tex(exaccent.sty) = %{tl_version}
Provides:       tex(extraipa.sty) = %{tl_version}, tex(t3cmr.fd) = %{tl_version}
Provides:       tex(t3cmss.fd) = %{tl_version}, tex(t3cmtt.fd) = %{tl_version}
Provides:       tex(t3enc.def) = %{tl_version}, tex(t3phv.fd) = %{tl_version}
Provides:       tex(t3ptm.fd) = %{tl_version}, tex(tipa.sty) = %{tl_version}
Provides:       tex(tipx.sty) = %{tl_version}, tex(tone.sty) = %{tl_version}
Provides:       tex(ts3cmr.fd) = %{tl_version}, tex(ts3cmss.fd) = %{tl_version}
Provides:       tex(ts3cmtt.fd) = %{tl_version}, tex(ts3enc.def) = %{tl_version}
Provides:       tex(ts3phv.fd) = %{tl_version}, tex(ts3ptm.fd) = %{tl_version}
Provides:       tex(utipx.fd) = %{tl_version}, tex(utipxss.fd) = %{tl_version}
Provides:       tex(utipxtt.fd) = %{tl_version}, tex(uxipx.fd) = %{tl_version}
Provides:       tex(uxipxss.fd) = %{tl_version}, tex(vowel.sty) = %{tl_version}

%description -n texlive-tipa
These fonts are considered the 'ultimate answer' to IPA
typesetting. The encoding of these 8-bit fonts has been
registered as LaTeX standard encoding T3, and the set of
addendum symbols as encoding TS3. 'Times-like' Adobe Type 1
versions are provided for both the T3 and the TS3 fonts.

%package -n texlive-tipa-doc
Summary:        Documentation for tipa
Version:        svn29349.1.3

Provides:       tex-tipa-doc
AutoReqProv:    No

%description -n texlive-tipa-doc
Documentation for tipa

%package -n texlive-txfonts
Provides:       tex-txfonts = %{tl_version}
License:        GPL+
Summary:        Times-like fonts in support of mathematics
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(tx8r.enc) = %{tl_version}, tex(txfonts.map) = %{tl_version}
Provides:       tex(txr.map) = %{tl_version}, tex(txr1.map) = %{tl_version}
Provides:       tex(txr2.map) = %{tl_version}, tex(txr3.map) = %{tl_version}
Provides:       tex(rtcxb.tfm) = %{tl_version}, tex(rtcxbi.tfm) = %{tl_version}
Provides:       tex(rtcxbsl.tfm) = %{tl_version}, tex(rtcxbss.tfm) = %{tl_version}
Provides:       tex(rtcxbsso.tfm) = %{tl_version}, tex(rtcxi.tfm) = %{tl_version}
Provides:       tex(rtcxr.tfm) = %{tl_version}, tex(rtcxsl.tfm) = %{tl_version}
Provides:       tex(rtcxss.tfm) = %{tl_version}, tex(rtcxsssl.tfm) = %{tl_version}
Provides:       tex(rtxb.tfm) = %{tl_version}, tex(rtxbi.tfm) = %{tl_version}
Provides:       tex(rtxbmi.tfm) = %{tl_version}, tex(rtxbsc.tfm) = %{tl_version}
Provides:       tex(rtxbsl.tfm) = %{tl_version}, tex(rtxbss.tfm) = %{tl_version}
Provides:       tex(rtxbsssc.tfm) = %{tl_version}, tex(rtxbsssl.tfm) = %{tl_version}
Provides:       tex(rtxi.tfm) = %{tl_version}, tex(rtxmi.tfm) = %{tl_version}
Provides:       tex(rtxphvb.tfm) = %{tl_version}, tex(rtxphvbo.tfm) = %{tl_version}
Provides:       tex(rtxphvr.tfm) = %{tl_version}, tex(rtxphvro.tfm) = %{tl_version}
Provides:       tex(rtxptmb.tfm) = %{tl_version}, tex(rtxptmbi.tfm) = %{tl_version}
Provides:       tex(rtxptmbo.tfm) = %{tl_version}, tex(rtxptmr.tfm) = %{tl_version}
Provides:       tex(rtxptmri.tfm) = %{tl_version}, tex(rtxptmro.tfm) = %{tl_version}
Provides:       tex(rtxr.tfm) = %{tl_version}, tex(rtxsc.tfm) = %{tl_version}
Provides:       tex(rtxsl.tfm) = %{tl_version}, tex(rtxss.tfm) = %{tl_version}
Provides:       tex(rtxsssc.tfm) = %{tl_version}, tex(rtxsssl.tfm) = %{tl_version}
Provides:       tex(t1xb.tfm) = %{tl_version}, tex(t1xbi.tfm) = %{tl_version}
Provides:       tex(t1xbsc.tfm) = %{tl_version}, tex(t1xbsl.tfm) = %{tl_version}
Provides:       tex(t1xbss.tfm) = %{tl_version}, tex(t1xbsssc.tfm) = %{tl_version}
Provides:       tex(t1xbsssl.tfm) = %{tl_version}, tex(t1xbtt.tfm) = %{tl_version}
Provides:       tex(t1xbttsc.tfm) = %{tl_version}, tex(t1xbttsl.tfm) = %{tl_version}
Provides:       tex(t1xi.tfm) = %{tl_version}, tex(t1xr.tfm) = %{tl_version}
Provides:       tex(t1xsc.tfm) = %{tl_version}, tex(t1xsl.tfm) = %{tl_version}
Provides:       tex(t1xss.tfm) = %{tl_version}, tex(t1xsssc.tfm) = %{tl_version}
Provides:       tex(t1xsssl.tfm) = %{tl_version}, tex(t1xtt.tfm) = %{tl_version}
Provides:       tex(t1xttsc.tfm) = %{tl_version}, tex(t1xttsl.tfm) = %{tl_version}
Provides:       tex(tcxb.tfm) = %{tl_version}, tex(tcxbi.tfm) = %{tl_version}
Provides:       tex(tcxbsl.tfm) = %{tl_version}, tex(tcxbss.tfm) = %{tl_version}
Provides:       tex(tcxbsssl.tfm) = %{tl_version}, tex(tcxbtt.tfm) = %{tl_version}
Provides:       tex(tcxbttsl.tfm) = %{tl_version}, tex(tcxi.tfm) = %{tl_version}
Provides:       tex(tcxr.tfm) = %{tl_version}, tex(tcxsl.tfm) = %{tl_version}
Provides:       tex(tcxss.tfm) = %{tl_version}, tex(tcxsssl.tfm) = %{tl_version}
Provides:       tex(tcxtt.tfm) = %{tl_version}, tex(tcxttsl.tfm) = %{tl_version}
Provides:       tex(txb.tfm) = %{tl_version}, tex(txbex.tfm) = %{tl_version}
Provides:       tex(txbexa.tfm) = %{tl_version}, tex(txbi.tfm) = %{tl_version}
Provides:       tex(txbmi.tfm) = %{tl_version}, tex(txbmi1.tfm) = %{tl_version}
Provides:       tex(txbmia.tfm) = %{tl_version}, tex(txbsc.tfm) = %{tl_version}
Provides:       tex(txbsl.tfm) = %{tl_version}, tex(txbss.tfm) = %{tl_version}
Provides:       tex(txbsssc.tfm) = %{tl_version}, tex(txbsssl.tfm) = %{tl_version}
Provides:       tex(txbsy.tfm) = %{tl_version}, tex(txbsya.tfm) = %{tl_version}
Provides:       tex(txbsyb.tfm) = %{tl_version}, tex(txbsyc.tfm) = %{tl_version}
Provides:       tex(txbtt.tfm) = %{tl_version}, tex(txbttsc.tfm) = %{tl_version}
Provides:       tex(txbttsl.tfm) = %{tl_version}, tex(txex.tfm) = %{tl_version}
Provides:       tex(txexa.tfm) = %{tl_version}, tex(txi.tfm) = %{tl_version}
Provides:       tex(txmi.tfm) = %{tl_version}, tex(txmi1.tfm) = %{tl_version}
Provides:       tex(txmia.tfm) = %{tl_version}, tex(txr.tfm) = %{tl_version}
Provides:       tex(txsc.tfm) = %{tl_version}, tex(txsl.tfm) = %{tl_version}
Provides:       tex(txss.tfm) = %{tl_version}, tex(txsssc.tfm) = %{tl_version}
Provides:       tex(txsssl.tfm) = %{tl_version}, tex(txsy.tfm) = %{tl_version}
Provides:       tex(txsya.tfm) = %{tl_version}, tex(txsyb.tfm) = %{tl_version}
Provides:       tex(txsyc.tfm) = %{tl_version}, tex(txtt.tfm) = %{tl_version}
Provides:       tex(txttsc.tfm) = %{tl_version}, tex(txttsl.tfm) = %{tl_version}
Provides:       tex(tyxb.tfm) = %{tl_version}, tex(tyxbi.tfm) = %{tl_version}
Provides:       tex(tyxbsc.tfm) = %{tl_version}, tex(tyxbsl.tfm) = %{tl_version}
Provides:       tex(tyxbss.tfm) = %{tl_version}, tex(tyxbsssc.tfm) = %{tl_version}
Provides:       tex(tyxbsssl.tfm) = %{tl_version}, tex(tyxbtt.tfm) = %{tl_version}
Provides:       tex(tyxbttsc.tfm) = %{tl_version}, tex(tyxbttsl.tfm) = %{tl_version}
Provides:       tex(tyxi.tfm) = %{tl_version}, tex(tyxr.tfm) = %{tl_version}
Provides:       tex(tyxsc.tfm) = %{tl_version}, tex(tyxsl.tfm) = %{tl_version}
Provides:       tex(tyxss.tfm) = %{tl_version}, tex(tyxsssc.tfm) = %{tl_version}
Provides:       tex(tyxsssl.tfm) = %{tl_version}, tex(tyxtt.tfm) = %{tl_version}
Provides:       tex(tyxttsc.tfm) = %{tl_version}, tex(tyxttsl.tfm) = %{tl_version}
Provides:       tex(rtcxb.pfb) = %{tl_version}, tex(rtcxbi.pfb) = %{tl_version}
Provides:       tex(rtcxbss.pfb) = %{tl_version}, tex(rtcxi.pfb) = %{tl_version}
Provides:       tex(rtcxr.pfb) = %{tl_version}, tex(rtcxss.pfb) = %{tl_version}
Provides:       tex(rtxb.pfb) = %{tl_version}, tex(rtxbi.pfb) = %{tl_version}
Provides:       tex(rtxbmi.pfb) = %{tl_version}, tex(rtxbsc.pfb) = %{tl_version}
Provides:       tex(rtxbss.pfb) = %{tl_version}, tex(rtxbsssc.pfb) = %{tl_version}
Provides:       tex(rtxi.pfb) = %{tl_version}, tex(rtxmi.pfb) = %{tl_version}
Provides:       tex(rtxr.pfb) = %{tl_version}, tex(rtxsc.pfb) = %{tl_version}
Provides:       tex(rtxss.pfb) = %{tl_version}, tex(rtxsssc.pfb) = %{tl_version}
Provides:       tex(t1xbtt.pfb) = %{tl_version}, tex(t1xbttsc.pfb) = %{tl_version}
Provides:       tex(t1xtt.pfb) = %{tl_version}, tex(t1xttsc.pfb) = %{tl_version}
Provides:       tex(tcxbtt.pfb) = %{tl_version}, tex(tcxtt.pfb) = %{tl_version}
Provides:       tex(txbex.pfb) = %{tl_version}, tex(txbexa.pfb) = %{tl_version}
Provides:       tex(txbmia.pfb) = %{tl_version}, tex(txbsy.pfb) = %{tl_version}
Provides:       tex(txbsya.pfb) = %{tl_version}, tex(txbsyb.pfb) = %{tl_version}
Provides:       tex(txbsyc.pfb) = %{tl_version}, tex(txbtt.pfb) = %{tl_version}
Provides:       tex(txbttsc.pfb) = %{tl_version}, tex(txex.pfb) = %{tl_version}
Provides:       tex(txexa.pfb) = %{tl_version}, tex(txmia.pfb) = %{tl_version}
Provides:       tex(txsy.pfb) = %{tl_version}, tex(txsya.pfb) = %{tl_version}
Provides:       tex(txsyb.pfb) = %{tl_version}, tex(txsyc.pfb) = %{tl_version}
Provides:       tex(txtt.pfb) = %{tl_version}, tex(txttsc.pfb) = %{tl_version}
Provides:       tex(t1xb.vf) = %{tl_version}, tex(t1xbi.vf) = %{tl_version}
Provides:       tex(t1xbsc.vf) = %{tl_version}, tex(t1xbsl.vf) = %{tl_version}
Provides:       tex(t1xbss.vf) = %{tl_version}, tex(t1xbsssc.vf) = %{tl_version}
Provides:       tex(t1xbsssl.vf) = %{tl_version}, tex(t1xi.vf) = %{tl_version}
Provides:       tex(t1xr.vf) = %{tl_version}, tex(t1xsc.vf) = %{tl_version}
Provides:       tex(t1xsl.vf) = %{tl_version}, tex(t1xss.vf) = %{tl_version}
Provides:       tex(t1xsssc.vf) = %{tl_version}, tex(t1xsssl.vf) = %{tl_version}
Provides:       tex(tcxb.vf) = %{tl_version}, tex(tcxbi.vf) = %{tl_version}
Provides:       tex(tcxbsl.vf) = %{tl_version}, tex(tcxbss.vf) = %{tl_version}
Provides:       tex(tcxbsssl.vf) = %{tl_version}, tex(tcxi.vf) = %{tl_version}
Provides:       tex(tcxr.vf) = %{tl_version}, tex(tcxsl.vf) = %{tl_version}
Provides:       tex(tcxss.vf) = %{tl_version}, tex(tcxsssl.vf) = %{tl_version}
Provides:       tex(txb.vf) = %{tl_version}, tex(txbi.vf) = %{tl_version}
Provides:       tex(txbmi.vf) = %{tl_version}, tex(txbmi1.vf) = %{tl_version}
Provides:       tex(txbsc.vf) = %{tl_version}, tex(txbsl.vf) = %{tl_version}
Provides:       tex(txbss.vf) = %{tl_version}, tex(txbsssc.vf) = %{tl_version}
Provides:       tex(txbsssl.vf) = %{tl_version}, tex(txi.vf) = %{tl_version}
Provides:       tex(txmi.vf) = %{tl_version}, tex(txmi1.vf) = %{tl_version}
Provides:       tex(txr.vf) = %{tl_version}, tex(txsc.vf) = %{tl_version}
Provides:       tex(txsl.vf) = %{tl_version}, tex(txss.vf) = %{tl_version}
Provides:       tex(txsssc.vf) = %{tl_version}, tex(txsssl.vf) = %{tl_version}
Provides:       tex(tyxb.vf) = %{tl_version}, tex(tyxbi.vf) = %{tl_version}
Provides:       tex(tyxbsc.vf) = %{tl_version}, tex(tyxbsl.vf) = %{tl_version}
Provides:       tex(tyxbss.vf) = %{tl_version}, tex(tyxbsssc.vf) = %{tl_version}
Provides:       tex(tyxbsssl.vf) = %{tl_version}, tex(tyxbtt.vf) = %{tl_version}
Provides:       tex(tyxbttsc.vf) = %{tl_version}, tex(tyxbttsl.vf) = %{tl_version}
Provides:       tex(tyxi.vf) = %{tl_version}, tex(tyxr.vf) = %{tl_version}
Provides:       tex(tyxsc.vf) = %{tl_version}, tex(tyxsl.vf) = %{tl_version}
Provides:       tex(tyxss.vf) = %{tl_version}, tex(tyxsssc.vf) = %{tl_version}
Provides:       tex(tyxsssl.vf) = %{tl_version}, tex(tyxtt.vf) = %{tl_version}
Provides:       tex(tyxttsc.vf) = %{tl_version}, tex(tyxttsl.vf) = %{tl_version}
Provides:       tex(ly1txr.fd) = %{tl_version}, tex(ly1txss.fd) = %{tl_version}
Provides:       tex(ly1txtt.fd) = %{tl_version}, tex(omltxmi.fd) = %{tl_version}
Provides:       tex(omltxr.fd) = %{tl_version}, tex(omstxr.fd) = %{tl_version}
Provides:       tex(omstxsy.fd) = %{tl_version}, tex(omxtxex.fd) = %{tl_version}
Provides:       tex(ot1txr.fd) = %{tl_version}, tex(ot1txss.fd) = %{tl_version}
Provides:       tex(ot1txtt.fd) = %{tl_version}, tex(t1txr.fd) = %{tl_version}
Provides:       tex(t1txss.fd) = %{tl_version}, tex(t1txtt.fd) = %{tl_version}
Provides:       tex(ts1txr.fd) = %{tl_version}, tex(ts1txss.fd) = %{tl_version}
Provides:       tex(ts1txtt.fd) = %{tl_version}, tex(txfonts.sty) = %{tl_version}
Provides:       tex(utxexa.fd) = %{tl_version}, tex(utxmia.fd) = %{tl_version}
Provides:       tex(utxr.fd) = %{tl_version}, tex(utxss.fd) = %{tl_version}
Provides:       tex(utxsya.fd) = %{tl_version}, tex(utxsyb.fd) = %{tl_version}
Provides:       tex(utxsyc.fd) = %{tl_version}, tex(utxtt.fd) = %{tl_version}

%description -n texlive-txfonts
Txfonts supplies virtual text roman fonts using Adobe Times (or
URW NimbusRomNo9L) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Times/URW Nimbus; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set.
All the fonts are in Type 1 format (AFM and PFB files), and are
supported by TeX metrics (VF and TFM files) and macros for use
with LaTeX.

%package -n texlive-txfonts-doc
Summary:        Documentation for txfonts
Version:        svn15878.0

Provides:       tex-txfonts-doc
AutoReqProv:    No

%description -n texlive-txfonts-doc
Documentation for txfonts

%package -n texlive-tracklang
Provides:       tex-tracklang = %{tl_version}
License:        LPPL 1.3
Summary:        Language and dialect tracker
Version:        svn47704
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(tracklang.tex) = %{tl_version}, tex(tracklang.sty) = %{tl_version}

%description -n texlive-tracklang
The tracklang package is provided for package developers who
want a simple interface to find out which languages the user
has requested through packages such as babel or polyglossia.
This package does not provide any translations! Its purpose is
simply to track which languages have been requested by the
user. Generic TeX code is in tracklang.tex for non-LaTeX users.

%package -n texlive-tracklang-doc
Summary:        Documentation for tracklang
Version:        svn47704
Provides:       tex-tracklang-doc
AutoReqProv:    No

%description -n texlive-tracklang-doc
Documentation for tracklang

%package -n texlive-theoremref
Provides:       tex-theoremref = %{tl_version}
License:        LPPL
Summary:        References with automatic theorem names
Version:        svn30640.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(theoremref.sty) = %{tl_version}

%description -n texlive-theoremref
The theoremref package provides variants of the \label and \ref
commands for theorem-like environments, capable of
automatically typesetting references including the theorem name
(apart from the theorem number). The scheme is particularly
valuable if the author decides to change a lemma to a
proposition or a theorem (or whatever).

%package -n texlive-theoremref-doc
Summary:        Documentation for theoremref
Version:        svn30640.0

Provides:       tex-theoremref-doc
AutoReqProv:    No

%description -n texlive-theoremref-doc
Documentation for theoremref

%package -n texlive-thinsp
Provides:       tex-thinsp = %{tl_version}
License:        GPL+
Summary:        A stretchable \thinspace for LaTeX
Version:        svn39669

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(thinsp.sty) = %{tl_version}

%description -n texlive-thinsp
The package redefines \thinspace to have a stretch component.

%package -n texlive-thinsp-doc
Summary:        Documentation for thinsp
Version:        svn39669

Provides:       tex-thinsp-doc
AutoReqProv:    No

%description -n texlive-thinsp-doc
Documentation for thinsp

%package -n texlive-thmbox
Provides:       tex-thmbox = %{tl_version}
License:        LPPL
Summary:        Decorate theorem statements
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(thmbox.sty) = %{tl_version}

%description -n texlive-thmbox
The package defines an environment thmbox that presents
theorems, definitions and similar objects in boxes decorated
with frames and various aesthetic features. The standard macro
\newtheorem may be redefined to use the environment.

%package -n texlive-thmbox-doc
Summary:        Documentation for thmbox
Version:        svn15878.0

Provides:       tex-thmbox-doc
AutoReqProv:    No

%description -n texlive-thmbox-doc
Documentation for thmbox

%package -n texlive-turnstile
Provides:       tex-turnstile = %{tl_version}
License:        LPPL
Summary:        Typeset the (logic) turnstile notation
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(turnstile.sty) = %{tl_version}

%description -n texlive-turnstile
Among other uses, the turnstile sign is used by logicians for
denoting a consequence relation, related to a given logic,
between a collection of formulas and a derived formula.

%package -n texlive-turnstile-doc
Summary:        Documentation for turnstile
Version:        svn15878.1.0

Provides:       tex-turnstile-doc
AutoReqProv:    No

%description -n texlive-turnstile-doc
Documentation for turnstile

%package -n texlive-thmtools
Provides:       tex-thmtools = %{tl_version}
License:        LPPL 1.3
Summary:        Extensions to theorem environments
Version:        svn33624.66

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(remreset.sty), tex(keyval.sty), tex(kvsetkeys.sty), tex(etex.sty)
Requires:       tex(thmtools.sty), tex(mdframed.sty), tex(shadethm.sty), tex(thmbox.sty)
Provides:       tex(aliasctr.sty) = %{tl_version}, tex(parseargs.sty) = %{tl_version}
Provides:       tex(thm-amsthm.sty) = %{tl_version}, tex(thm-autoref.sty) = %{tl_version}
Provides:       tex(thm-beamer.sty) = %{tl_version}, tex(thm-kv.sty) = %{tl_version}
Provides:       tex(thm-listof.sty) = %{tl_version}, tex(thm-llncs.sty) = %{tl_version}
Provides:       tex(thm-ntheorem.sty) = %{tl_version}, tex(thm-patch.sty) = %{tl_version}
Provides:       tex(thm-restate.sty) = %{tl_version}, tex(thmdef-mdframed.sty) = %{tl_version}
Provides:       tex(thmdef-shaded.sty) = %{tl_version}, tex(thmdef-thmbox.sty) = %{tl_version}
Provides:       tex(thmtools.sty) = %{tl_version}, tex(unique.sty) = %{tl_version}

%description -n texlive-thmtools
The bundle provides several packages for commonly-needed
support for typesetting theorems. The packages should work with
kernel theorems (theorems 'out of the box' with LaTeX), and the
theorem and amsthm packages. Features of the bundle include: a
key-value interface to \newtheorem; a \listoftheorems command;
hyperref and autoref compatibility; a mechanism for restating
entire theorems in a single macro call.

%package -n texlive-thmtools-doc
Summary:        Documentation for thmtools
Version:        svn33624.66

Provides:       tex-thmtools-doc
AutoReqProv:    No

%description -n texlive-thmtools-doc
Documentation for thmtools

%package -n texlive-threadcol
Provides:       tex-threadcol = %{tl_version}
License:        LPPL 1.3
Summary:        Organize document columns into PDF "article thread"
Version:        svn28754.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(etoolbox.sty)
Provides:       tex(threadcol.sty) = %{tl_version}

%description -n texlive-threadcol
The package combines a document's columns into a PDF "article
thread". PDF readers that support this mechanism (probably
Adobe Acrobat/Reader only) can be instructed to scroll
automatically from column to column, which facilitates on-
screen reading of two-column documents. Even for single-column
documents, threadcol supports the creation of multiple article
threads, which help organize discontiguous but logically
related regions of text into a form that the user can scroll
through as if its contents were contiguous.

%package -n texlive-threadcol-doc
Summary:        Documentation for threadcol
Version:        svn28754.1.0

Provides:       tex-threadcol-doc
AutoReqProv:    No

%description -n texlive-threadcol-doc
Documentation for threadcol

%package -n texlive-threeddice
Provides:       tex-threeddice = %{tl_version}
License:        LPPL
Summary:        Create images of dice with one, two, or three faces showing, using MetaPost
Version:        svn20675.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-threeddice
The package provides MetaPost code to create all possible
symmetrical views (up to rotation) of a right-handed die.
Configuration is possible by editing the source code, following
the guidance in the documentation.

%package -n texlive-threeddice-doc
Summary:        Documentation for threeddice
Version:        svn20675.1.0

Provides:       tex-threeddice-doc
AutoReqProv:    No

%description -n texlive-threeddice-doc
Documentation for threeddice

%package -n texlive-threeparttable
Provides:       tex-threeparttable = %{tl_version}
License:        Threeparttable
Summary:        Tables with captions and notes all the same width
Version:        svn17383.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(3parttable.sty) = %{tl_version}, tex(threeparttable.sty) = %{tl_version}

%description -n texlive-threeparttable
Provides a scheme for tables that have a structured note
section, after the caption. This scheme provides an answer to
the old problem of putting footnotes in tables -- by making
footnotes entirely unnecessary. Note that a threeparttable is
not a float of itself; but you can place it in a table or a
table* environment, if necessary.

%package -n texlive-threeparttable-doc
Summary:        Documentation for threeparttable
Version:        svn17383.0

Provides:       tex-threeparttable-doc
AutoReqProv:    No

%description -n texlive-threeparttable-doc
Documentation for threeparttable

%package -n texlive-threeparttablex
Provides:       tex-threeparttablex = %{tl_version}
License:        LPPL
Summary:        Notes in longtables
Version:        svn34206.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(threeparttable.sty), tex(environ.sty)
Provides:       tex(threeparttablex.sty) = %{tl_version}

%description -n texlive-threeparttablex
The package provides the functionality of the threeparttable
package to tables created using the longtable package.

%package -n texlive-threeparttablex-doc
Summary:        Documentation for threeparttablex
Version:        svn34206.0.3

Provides:       tex-threeparttablex-doc
AutoReqProv:    No

%description -n texlive-threeparttablex-doc
Documentation for threeparttablex

%package -n texlive-thumb
Provides:       tex-thumb = %{tl_version}
License:        GPL+
Summary:        Thumb marks in documents
Version:        svn16549.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyhdr.sty), tex(minitoc.sty)
Provides:       tex(thumb.sty) = %{tl_version}

%description -n texlive-thumb
Place thumb marks in books, manuals and reference maunals.

%package -n texlive-thumb-doc
Summary:        Documentation for thumb
Version:        svn16549.1.0

Provides:       tex-thumb-doc
AutoReqProv:    No

%description -n texlive-thumb-doc
Documentation for thumb

%package -n texlive-thumbs
Provides:       tex-thumbs = %{tl_version}
License:        LPPL 1.3
Summary:        Create thumb indexes
Version:        svn33134.1.0q

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(atbegshi.sty), tex(xcolor.sty), tex(picture.sty)
Requires:       tex(alphalph.sty), tex(pageslts.sty), tex(pagecolor.sty), tex(rerunfilecheck.sty)
Requires:       tex(infwarerr.sty), tex(ltxcmds.sty), tex(atveryend.sty)
Provides:       tex(thumbs.sty) = %{tl_version}

%description -n texlive-thumbs
The package puts running, customizable thumb marks in the outer
margin, moving downward as the chapter number (or whatever
shall be marked by the thumb marks) increases. Additionally an
overview page/table of thumb marks can be added automatically,
which gives the names of the thumbed objects, the page where
the object/thumb mark first appears, and the thumb mark itself
at its correct position. The thumb marks are useful for large
documents (such as reference guides, anthologies, etc.), where
a quick and easy way to find (for example) a chapter is needed.

%package -n texlive-thumbs-doc
Summary:        Documentation for thumbs
Version:        svn33134.1.0q

Provides:       tex-thumbs-doc
AutoReqProv:    No

%description -n texlive-thumbs-doc
Documentation for thumbs

%package -n texlive-thumby
Provides:       tex-thumby = %{tl_version}
License:        GPLv3+
Summary:        Create thumb indexes for printed books
Version:        svn16736.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(perltex.sty), tex(bophook.sty)
Provides:       tex(thumby.sty) = %{tl_version}

%description -n texlive-thumby
The package can generate thumb indexes for your document. It
features printing thumb indexes on one- or two-sided pages,
along with background- and foreground-color selection and full
LaTeX styling of the chapter numbers in the thumb indexes. The
height of each thumb index is automatically chosen based on the
number of chapters in your document, while the width is chosen
by the user. The package is designed to work with the memoir
class, and also requires PerlTeX and tikz/

%package -n texlive-thumby-doc
Summary:        Documentation for thumby
Version:        svn16736.0.1

Provides:       tex-thumby-doc
AutoReqProv:    No

%description -n texlive-thumby-doc
Documentation for thumby

%package -n texlive-ticket
Provides:       tex-ticket = %{tl_version}
License:        LPPL
Summary:        Make labels, visiting-cards, pins with LaTeX
Version:        svn42280
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(calc.sty)
Provides:       tex(ticket.sty) = %{tl_version}

%description -n texlive-ticket
Provides an easy to handle interface to produce visiting cards,
labels for your files, stickers, pins and other stuff for your
office, conferences etc. All you need is a definition of your
'ticket' included in a ticket definition file and the two
commands \ticketdefault and \ticket.

%package -n texlive-ticket-doc
Summary:        Documentation for ticket
Version:        svn42280
Provides:       tex-ticket-doc
AutoReqProv:    No

%description -n texlive-ticket-doc
Documentation for ticket

%package -n texlive-ticollege
Provides:       tex-ticollege = %{tl_version}
License:        LPPL
Summary:        Graphical representation of keys on a standard scientific calculator
Version:        svn36306.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(newtxtt.sty), tex(tikz.sty), tex(ifthen.sty)
Requires:       tex(xkeyval.sty), tex(mathtools.sty), tex(amssymb.sty), tex(multido.sty)
Requires:       tex(multirow.sty)
Provides:       tex(ticollege.sty) = %{tl_version}

%description -n texlive-ticollege
This package provides commands to draw scientific calculator
keys with the help of TikZ. It also provides commands to draw
the content of screens and of menu items.

%package -n texlive-ticollege-doc
Summary:        Documentation for ticollege
Version:        svn36306.1.0

Provides:       tex-ticollege-doc
AutoReqProv:    No

%description -n texlive-ticollege-doc
Documentation for ticollege

%package -n texlive-tipfr-doc
Summary:        Documentation for tipfr
Version:        svn38646

Provides:       tex-tipfr-doc
AutoReqProv:    No

%description -n texlive-tipfr-doc
Documentation for tipfr

%package -n texlive-tikz-3dplot
Provides:       tex-tikz-3dplot = %{tl_version}
License:        LPPL 1.3
Summary:        Coordinate transformation styles for 3d plotting in TikZ
Version:        svn25087.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgf.sty), tex(ifthen.sty)
Provides:       tex(tikz-3dplot.sty) = %{tl_version}

%description -n texlive-tikz-3dplot
The package provides straightforward ways to define three-
dimensional coordinate frames through which to plot in TikZ.
The user can specify the orientation of the main coordinate
frame, and use standard TikZ commands and coordinates to render
their tikzfigure. A secondary coordinate frame is provided to
allow rotations and translations with respect to the main
coordinate frame. In addition, the package can also handle
plotting user-specified functions in spherical polar
coordinates, where both the radius and fill color can be
expressed as parametric functions of polar angles.

%package -n texlive-tikz-3dplot-doc
Summary:        Documentation for tikz-3dplot
Version:        svn25087.0

Provides:       tex-tikz-3dplot-doc
AutoReqProv:    No

%description -n texlive-tikz-3dplot-doc
Documentation for tikz-3dplot

%package -n texlive-tikz-bayesnet
Provides:       tex-tikz-bayesnet = %{tl_version}
License:        LPPL 1.3
Summary:        Draw Bayesian networks, graphical models and directed factor graphs
Version:        svn38295.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tikzlibrarybayesnet.code.tex) = %{tl_version}

%description -n texlive-tikz-bayesnet
The package provides a library supporting the display of
Bayesian networks, graphical models and (directed) factor
graphs in LaTeX.

%package -n texlive-tikz-bayesnet-doc
Summary:        Documentation for tikz-bayesnet
Version:        svn38295.0.1

Provides:       tex-tikz-bayesnet-doc
AutoReqProv:    No

%description -n texlive-tikz-bayesnet-doc
Documentation for tikz-bayesnet

%package -n texlive-tikz-cd
Provides:       tex-tikz-cd = %{tl_version}
License:        GPLv3+
Summary:        Create commutative diagrams with TikZ
Version:        svn35485.0.9e

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(tikzlibrarycd.code.tex) = %{tl_version}
Provides:       tex(tikz-cd.sty) = %{tl_version}

%description -n texlive-tikz-cd
The general-purpose drawing package TiKZ can be used to typeset
commutative diagrams and other kinds of mathematical pictures,
generating high-quality results. The purpose of this package is
to make the process of creation of such diagrams easier by
providing a convenient set of macros and reasonable default
settings. This package also includes an arrow tip library that
match closely the arrows present in the Computer Modern
typeface.

%package -n texlive-tikz-cd-doc
Summary:        Documentation for tikz-cd
Version:        svn35485.0.9e

Provides:       tex-tikz-cd-doc
AutoReqProv:    No

%description -n texlive-tikz-cd-doc
Documentation for tikz-cd

%package -n texlive-tikz-dependency
Provides:       tex-tikz-dependency = %{tl_version}
License:        (GPLv2 or LPPL) and (GFDL or LPPL)
Summary:        A library for drawing dependency graphs
Version:        svn42454
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(environ.sty)
Provides:       tex(tikz-dependency.sty) = %{tl_version}

%description -n texlive-tikz-dependency
The package provides a library that draws together existing
TikZ facilities to make a comfortable environment for drawing
dependency graphs. Basic facilities of the package include a
lot of styling facilities, to let you personalize the look and
feel of the graphs.

%package -n texlive-tikz-dependency-doc
Summary:        Documentation for tikz-dependency
Version:        svn42454
Provides:       tex-tikz-dependency-doc
AutoReqProv:    No

%description -n texlive-tikz-dependency-doc
Documentation for tikz-dependency

%package -n texlive-tikz-dimline
Provides:       tex-tikz-dimline = %{tl_version}
License:        WTFPL
Summary:        Technical dimension lines using PGF/TikZ
Version:        svn35805.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(pgfplots.sty), tex(ifthen.sty)
Provides:       tex(tikz-dimline.sty) = %{tl_version}

%description -n texlive-tikz-dimline
tikz-dimline helps drawing technical dimension lines in TikZ
picture environments. Its usage is similar to some
contributions posted on stackexchange.

%package -n texlive-tikz-dimline-doc
Summary:        Documentation for tikz-dimline
Version:        svn35805.1.0

Provides:       tex-tikz-dimline-doc
AutoReqProv:    No

%description -n texlive-tikz-dimline-doc
Documentation for tikz-dimline

%package -n texlive-tikz-inet
Provides:       tex-tikz-inet = %{tl_version}
License:        LPPL
Summary:        Draw interaction nets with TikZ
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty)
Provides:       tex(tikz-inet.sty) = %{tl_version}

%description -n texlive-tikz-inet
The package extends TikZ with macros to draw interaction nets.

%package -n texlive-tikz-inet-doc
Summary:        Documentation for tikz-inet
Version:        svn15878.0.1

Provides:       tex-tikz-inet-doc
AutoReqProv:    No

%description -n texlive-tikz-inet-doc
Documentation for tikz-inet

%package -n texlive-tikz-opm
Provides:       tex-tikz-opm = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset OPM diagrams
Version:        svn32769.0.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(makeshape.sty), tex(amsmath.sty)
Provides:       tex(tikz-opm.sty) = %{tl_version}

%description -n texlive-tikz-opm
Typeset OPM (Object-Process Methodology) diagrams using LaTeX
and pgf/TikZ.

%package -n texlive-tikz-opm-doc
Summary:        Documentation for tikz-opm
Version:        svn32769.0.1.1

Provides:       tex-tikz-opm-doc
AutoReqProv:    No

%description -n texlive-tikz-opm-doc
Documentation for tikz-opm

%package -n texlive-tikz-palattice
Provides:       tex-tikz-palattice = %{tl_version}
License:        LPPL 1.3
Summary:        Draw particle accelerator lattices with TikZ
Version:        svn43442
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(ifthen.sty), tex(siunitx.sty), tex(xargs.sty)
Requires:       tex(etoolbox.sty)
Provides:       tex(tikz-palattice.sty) = %{tl_version}

%description -n texlive-tikz-palattice
This package allows for drawing a map of a particle accelerator
just by giving a list of elements -- similar to lattice files
for simulation software. The package includes 12 common element
types like dipoles, quadrupoles, cavities, or screens, as well
as automatic labels with element names, a legend, a rule, and
an environment to fade out parts of the accelerator. The
coordinate of any element can be saved and used for custom tikz
drawings or annotations. Thereby, lattices can be connected to
draw injection/extraction or even a complete accelerator
facility.

%package -n texlive-tikz-palattice-doc
Summary:        Documentation for tikz-palattice
Version:        svn43442
Provides:       tex-tikz-palattice-doc
AutoReqProv:    No

%description -n texlive-tikz-palattice-doc
Documentation for tikz-palattice

%package -n texlive-tikz-qtree
Provides:       tex-tikz-qtree = %{tl_version}
License:        GPL+
Summary:        Use existing qtree syntax for trees in TikZ
Version:        svn26108.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgf.sty), tex(pgffor.sty), tex(tikz.sty)
Provides:       tex(pgfsubpic.sty) = %{tl_version}, tex(pgfsubpic.tex) = %{tl_version}
Provides:       tex(pgftree.sty) = %{tl_version}, tex(pgftree.tex) = %{tl_version}
Provides:       tex(tikz-qtree-compat.sty) = %{tl_version}
Provides:       tex(tikz-qtree.sty) = %{tl_version}, tex(tikz-qtree.tex) = %{tl_version}

%description -n texlive-tikz-qtree
The package provides a macro for drawing trees with TikZ using
the easy syntax of Alexis Dimitriadis' Qtree. It improves on
TikZ's standard tree-drawing facility by laying out tree nodes
without collisions; it improves on Qtree by adding lots of
features from TikZ (for example, edge labels, arrows between
nodes); and it improves on pst-qtree in being usable with
pdfTeX and XeTeX.

%package -n texlive-tikz-qtree-doc
Summary:        Documentation for tikz-qtree
Version:        svn26108.1.2

Provides:       tex-tikz-qtree-doc
AutoReqProv:    No

%description -n texlive-tikz-qtree-doc
Documentation for tikz-qtree

%package -n texlive-tikz-timing
Provides:       tex-tikz-timing = %{tl_version}
License:        LPPL
Summary:        Easy generation of timing diagrams as tikz pictures
Version:        svn46111
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-svn-prov, tex(svn-prov.sty), tex(pgfopts.sty), tex(array.sty)
Requires:       tex(booktabs.sty), tex(tikz.sty), tex(environ.sty), tex(amsmath.sty)
Provides:       tex(tikz-timing-advnodes.sty) = %{tl_version}
Provides:       tex(tikz-timing-arrows.sty) = %{tl_version}
Provides:       tex(tikz-timing-beamer.sty) = %{tl_version}
Provides:       tex(tikz-timing-clockarrows.sty) = %{tl_version}
Provides:       tex(tikz-timing-columntype.sty) = %{tl_version}
Provides:       tex(tikz-timing-counters.sty) = %{tl_version}
Provides:       tex(tikz-timing-either.sty) = %{tl_version}
Provides:       tex(tikz-timing-ifsym.sty) = %{tl_version}
Provides:       tex(tikz-timing-interval.sty) = %{tl_version}
Provides:       tex(tikz-timing-nicetabs.sty) = %{tl_version}
Provides:       tex(tikz-timing-overlays.sty) = %{tl_version}
Provides:       tex(tikz-timing.sty) = %{tl_version}

%description -n texlive-tikz-timing
This package provides macros and an environment to generate
timing diagrams (digital waveforms) without much effort. The
TikZ package is used to produce the graphics. The diagrams may
be inserted into text (paragraphs, \hbox, etc.) and into
tikzpictures. A tabular-like environment is provided to produce
larger timing diagrams.

%package -n texlive-tikz-timing-doc
Summary:        Documentation for tikz-timing
Version:        svn46111
Provides:       tex-tikz-timing-doc
AutoReqProv:    No
Requires:       tex-svn-prov-doc

%description -n texlive-tikz-timing-doc
Documentation for tikz-timing

%package -n texlive-titlecaps
Provides:       tex-titlecaps = %{tl_version}
License:        LPPL 1.3
Summary:        Setting rich-text input into Titling Caps
Version:        svn36170.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifnextok.sty)
Provides:       tex(titlecaps.sty) = %{tl_version}

%description -n texlive-titlecaps
The package is intended for setting rich text into titling
capitals (in which the first character of words are
capitalized). It automatically accounts for diacritical marks
(like umlauts), national symbols (like "ae"), punctuation, and
font changing commands that alter the appearance or size of the
text. It allows a list of predesignated words to be protected
as lower-cased, and also allows for titling exceptions of
various sorts.

%package -n texlive-titlecaps-doc
Summary:        Documentation for titlecaps
Version:        svn36170.1.2

Provides:       tex-titlecaps-doc
AutoReqProv:    No

%description -n texlive-titlecaps-doc
Documentation for titlecaps

%package -n texlive-titlefoot
Provides:       tex-titlefoot = %{tl_version}
License:        LPPL
Summary:        Add special material to footer of title page
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(titlefoot.sty) = %{tl_version}

%description -n texlive-titlefoot
Provides the capability of adding keywords (with a \keywords
command), a running title (\runningtitle), AMS subject
classifications (\amssubj), and an 'author's footnote' as
footnotes to the title or first page of a document. Works with
any class for which the \thanks macro works (e.g., article).

%package -n texlive-titlepic
Provides:       tex-titlepic = %{tl_version}
License:        Public Domain
Summary:        Add picture to title page of a document
Version:        svn43497
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(titlepic.sty) = %{tl_version}

%description -n texlive-titlepic
The package allows you to place a picture on the title page
(cover page) of a LaTeX document. Example of usage:
\usepackage[cc]{titlepic} \usepackage{graphicx}
\titlepic{\includegraphics[width=\textwidth]{picture.png}} The
package currently only works with the document classes article,
report and book.

%package -n texlive-titlepic-doc
Summary:        Documentation for titlepic
Version:        svn43497
Provides:       tex-titlepic-doc
AutoReqProv:    No

%description -n texlive-titlepic-doc
Documentation for titlepic

%package -n texlive-titlepages-doc
Summary:        Documentation for titlepages
Version:        svn19457.0

Provides:       tex-titlepages-doc
AutoReqProv:    No

%description -n texlive-titlepages-doc
Documentation for titlepages

%package -n texlive-tlc2-doc
Summary:        Documentation for tlc2
Version:        svn26096.0

Provides:       tex-tlc2-doc
AutoReqProv:    No

%description -n texlive-tlc2-doc
Documentation for tlc2

%package -n texlive-titleref
Provides:       tex-titleref = %{tl_version}
License:        Public Domain
Summary:        A "\titleref" command to cross-reference section titles
Version:        svn18729.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(titleref.sty) = %{tl_version}

%description -n texlive-titleref
Defines a command \titleref that allows you to cross-reference
section (and chapter, etc) titles and captions just like \ref
and \pageref. The package does not interwork with hyperref; if
you need hypertext capabilities, use nameref instead.

%package -n texlive-titleref-doc
Summary:        Documentation for titleref
Version:        svn18729.3.1

Provides:       tex-titleref-doc
AutoReqProv:    No

%description -n texlive-titleref-doc
Documentation for titleref

%package -n texlive-titlesec
Provides:       tex-titlesec = %{tl_version}
License:        LPPL
Summary:        Select alternative section titles
Version:        svn40129

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(titleps.sty) = %{tl_version}, tex(titlesec.sty) = %{tl_version}
Provides:       tex(titletoc.sty) = %{tl_version}, tex(ttlkeys.def) = %{tl_version}
Provides:       tex(ttlps.def) = %{tl_version}

%description -n texlive-titlesec
A package providing an interface to sectioning commands for
selection from various title styles. E.g., marginal titles and
to change the font of all headings with a single command, also
providing simple one-step page styles. Also includes a package
to change the page styles when there are floats in a page. You
may assign headers/footers to individual floats, too.

%package -n texlive-titlesec-doc
Summary:        Documentation for titlesec
Version:        svn40129

Provides:       tex-titlesec-doc
AutoReqProv:    No

%description -n texlive-titlesec-doc
Documentation for titlesec

%package -n texlive-titling
Provides:       tex-titling = %{tl_version}
License:        LPPL
Summary:        Control over the typesetting of the \maketitle command
Version:        svn15878.2.1d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(titling.sty) = %{tl_version}

%description -n texlive-titling
The titling package provides control over the typesetting of
the \maketitle command and \thanks commands, and makes the
\title, \author and \date information permanently available.
Multiple titles are allowed in a single document. New titling
elements can be added and a titlepage title can be centered on
a physical page.

%package -n texlive-titling-doc
Summary:        Documentation for titling
Version:        svn15878.2.1d

Provides:       tex-titling-doc
AutoReqProv:    No

%description -n texlive-titling-doc
Documentation for titling

%package -n texlive-tocbibind
Provides:       tex-tocbibind = %{tl_version}
License:        LPPL
Summary:        Add bibliography/index/contents to Table of Contents
Version:        svn20085.1.5k

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tocbibind.sty) = %{tl_version}

%description -n texlive-tocbibind
Automatically adds the bibliography and/or the index and/or the
contents, etc., to the Table of Contents listing.

%package -n texlive-tocbibind-doc
Summary:        Documentation for tocbibind
Version:        svn20085.1.5k

Provides:       tex-tocbibind-doc
AutoReqProv:    No

%description -n texlive-tocbibind-doc
Documentation for tocbibind

%package -n texlive-tocloft
Provides:       tex-tocloft = %{tl_version}
License:        LPPL 1.3
Summary:        Control table of contents, figures, etc
Version:        svn45188
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(tocloft.sty) = %{tl_version}

%description -n texlive-tocloft
Provides control over the typography of the Table of Contents,
List of Figures and List of Tables, and the ability to create
new 'List of ...'. The ToC \parskip may be changed.

%package -n texlive-tocloft-doc
Summary:        Documentation for tocloft
Version:        svn45188
Provides:       tex-tocloft-doc
AutoReqProv:    No

%description -n texlive-tocloft-doc
Documentation for tocloft

%package -n texlive-tocvsec2
Provides:       tex-tocvsec2 = %{tl_version}
License:        LPPL 1.3
Summary:        Section numbering and table of contents control
Version:        svn33146.1.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(tocvsec2.sty) = %{tl_version}

%description -n texlive-tocvsec2
Provides control over section numbering (without recourse to
starred sectional commands) and/or the entries in the Table of
Contents on a section by section basis.

%package -n texlive-tocvsec2-doc
Summary:        Documentation for tocvsec2
Version:        svn33146.1.3a

Provides:       tex-tocvsec2-doc
AutoReqProv:    No

%description -n texlive-tocvsec2-doc
Documentation for tocvsec2

%package -n texlive-todo
Provides:       tex-todo = %{tl_version}
License:        LPPL
Summary:        Make a to-do list for a document
Version:        svn17746.2.142

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty)
Provides:       tex(todo.sty) = %{tl_version}

%description -n texlive-todo
The package allows you to insert "to do" marks in your
document, to make lists of such items, and to cross-reference
to them.

%package -n texlive-todo-doc
Summary:        Documentation for todo
Version:        svn17746.2.142

Provides:       tex-todo-doc
AutoReqProv:    No

%description -n texlive-todo-doc
Documentation for todo

%package -n texlive-todonotes
Provides:       tex-todonotes = %{tl_version}
License:        LPPL 1.2
Summary:        Marking things to do in a LaTeX document
Version:        svn48208
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(xkeyval.sty), tex(xcolor.sty), tex(tikz.sty)
Requires:       tex(calc.sty)
Provides:       tex(todonotes.sty) = %{tl_version}

%description -n texlive-todonotes
The package lets the user mark things to do later, in a simple
and visually appealing way. The package takes several options
to enable customization/finetuning of the visual appearance.

%package -n texlive-todonotes-doc
Summary:        Documentation for todonotes
Version:        svn48208
Provides:       tex-todonotes-doc
AutoReqProv:    No

%description -n texlive-todonotes-doc
Documentation for todonotes

%package -n texlive-tokenizer
Provides:       tex-tokenizer = %{tl_version}
License:        LPPL
Summary:        A tokenizer
Version:        svn15878.1.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(tokenizer.sty) = %{tl_version}

%description -n texlive-tokenizer
A tokenizer for LaTeX. \GetTokens{Target1}{Target2}{Source}
splits source into two tokens at the first encounter of a
comma. The first token is saved in a newly created command with
the name passed as <Target1> and the second token likewise. A
package option 'trim' causes leading and trailing space to be
removed from each token; with this option, the \TrimSpaces
command is defined, which removes leading and trailing spaces
from its argument.

%package -n texlive-tokenizer-doc
Summary:        Documentation for tokenizer
Version:        svn15878.1.1.0

Provides:       tex-tokenizer-doc
AutoReqProv:    No

%description -n texlive-tokenizer-doc
Documentation for tokenizer

%package -n texlive-toolbox
Provides:       tex-toolbox = %{tl_version}
License:        LPPL
Summary:        Tool macros
Version:        svn32260.5.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(toolbox.sty) = %{tl_version}

%description -n texlive-toolbox
A package for (La)TeX which provides some macros which are
convenient for writing indexes, glossaries, or other macros. It
contains macros which support: implicit macros; fancy optional
arguments; loops over tokenlists and itemlists; searching and
splitting; controlled expansion; redefinition of macros; and
concatenated macro names; macros for text replacement.

%package -n texlive-toolbox-doc
Summary:        Documentation for toolbox
Version:        svn32260.5.1

Provides:       tex-toolbox-doc
AutoReqProv:    No

%description -n texlive-toolbox-doc
Documentation for toolbox

%package -n texlive-topfloat
Provides:       tex-topfloat = %{tl_version}
License:        GPL+
Summary:        Move floats to the top of the page
Version:        svn19084.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(topfloat.sty) = %{tl_version}

%description -n texlive-topfloat
topfloat package

%package -n texlive-topfloat-doc
Summary:        Documentation for topfloat
Version:        svn19084.0

Provides:       tex-topfloat-doc
AutoReqProv:    No

%description -n texlive-topfloat-doc
Documentation for topfloat

%package -n texlive-totcount
Provides:       tex-totcount = %{tl_version}
License:        LPPL
Summary:        Find the last value of a counter
Version:        svn21178.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(totcount.sty) = %{tl_version}

%description -n texlive-totcount
The package records the value that was last set, for any
counter of interest; since most such counters are simply
incremented when they are changed, the recorded value will
usually be the maximum value.

%package -n texlive-totcount-doc
Summary:        Documentation for totcount
Version:        svn21178.1.2

Provides:       tex-totcount-doc
AutoReqProv:    No

%description -n texlive-totcount-doc
Documentation for totcount

%package -n texlive-totpages
Provides:       tex-totpages = %{tl_version}
License:        LPPL
Summary:        Count pages in a document, and report last page number
Version:        svn15878.2.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(everyshi.sty), tex(keyval.sty)
Provides:       tex(totpages.sty) = %{tl_version}

%description -n texlive-totpages
The package counts the actual pages in the document (as opposed
to reporting the number of the last page, as does lastpage).
The counter itself may be shipped out to the DVI file. The
package uses the everyshi package for its task.

%package -n texlive-totpages-doc
Summary:        Documentation for totpages
Version:        svn15878.2.00

Provides:       tex-totpages-doc
AutoReqProv:    No

%description -n texlive-totpages-doc
Documentation for totpages

%package -n texlive-translator
Summary:        Easy translation of strings in LaTeX
Version:        svn46231
License:        LPPL or GPL+
Requires:       texlive-base texlive-kpathsea, tex(keyval.sty)
Provides:       tex(translator.sty) = %{tl_version}

%description -n texlive-translator
This LaTeX package provides a flexible mechanism for
translating individual words into different languages. For
example, it can be used to translate a word like "figure" into,
say, the German word "Abbildung". Such a translation mechanism
is useful when the author of some package would like to
localize the package such that texts are correctly translated
into the language preferred by the user. This package is not
intended to be used to automatically translate more than a few
words.

%package -n texlive-tikz-page
Summary:        Small macro to help building nice and complex layout materials
Version:        svn42039
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikz-page.sty) = %{tl_version}

%description -n texlive-tikz-page
The package provides a small macro to help building nice and
complex layout materials.

%package -n texlive-translation-array-fr-doc
Summary:        Documentation for translation-array-fr
Version:        svn24344.0

Provides:       tex-translation-array-fr-doc
AutoReqProv:    No

%description -n texlive-translation-array-fr-doc
Documentation for translation-array-fr

%package -n texlive-translation-dcolumn-fr-doc
Summary:        Documentation for translation-dcolumn-fr
Version:        svn24345.0

Provides:       tex-translation-dcolumn-fr-doc
AutoReqProv:    No

%description -n texlive-translation-dcolumn-fr-doc
Documentation for translation-dcolumn-fr

%package -n texlive-translation-natbib-fr-doc
Summary:        Documentation for translation-natbib-fr
Version:        svn25105.0

Provides:       tex-translation-natbib-fr-doc
AutoReqProv:    No

%description -n texlive-translation-natbib-fr-doc
Documentation for translation-natbib-fr

%package -n texlive-translation-tabbing-fr-doc
Summary:        Documentation for translation-tabbing-fr
Version:        svn24228.0

Provides:       tex-translation-tabbing-fr-doc
AutoReqProv:    No

%description -n texlive-translation-tabbing-fr-doc
Documentation for translation-tabbing-fr

%package -n texlive-translations
Provides:       tex-translations = %{tl_version}
License:        LPPL 1.3
Summary:        Internationalisation of LaTeX2e packages
Version:        svn45189
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(cnltx-base.sty), tex(scrlfile.sty)
Provides:       tex(translations.sty) = %{tl_version}

%description -n texlive-translations
This package (once part of the exsheets package), provides a
framework for providing multilingual features to a LaTeX
package. The package has its own basic dictionaries for
English, French, German and Spanish; it aims to use translation
material for English, French, German, Italian, Spanish,
Catalan, Turkish, Croatian, Hungarian, Danish and Portuguese
from babel or polyglossia if either is in use in the document.
(Additional languages from the multilingual packages may be
possible: ask the author.)

%package -n texlive-translations-doc
Summary:        Documentation for translations
Version:        svn45189
Provides:       tex-translations-doc
AutoReqProv:    No

%description -n texlive-translations-doc
Documentation for translations

%package -n texlive-trfsigns
Provides:       tex-trfsigns = %{tl_version}
License:        GPL+
Summary:        Typeset transform signs
Version:        svn15878.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(trfsigns.sty) = %{tl_version}

%description -n texlive-trfsigns
A package for typesetting various transformation signs for
Laplace transforms, Fourier transforms and others.

%package -n texlive-trfsigns-doc
Summary:        Documentation for trfsigns
Version:        svn15878.1.01

Provides:       tex-trfsigns-doc
AutoReqProv:    No

%description -n texlive-trfsigns-doc
Documentation for trfsigns

%package -n texlive-trigonometry
Summary:        Demonstration code for cos and sin in TeX macros
Version:        svn43006
License:        Knuth
Requires:       texlive-base texlive-kpathsea
Provides:       tex(trigonometry.tex) = %{tl_version}

%description -n texlive-trigonometry
A document that both provides macros that are usable elsewhere,
and demonstrates the macros. The code uses the "classical"
analytical expansion of sin and cos (the more recent trig uses
a "numerical analyst's" expansion).

%package -n texlive-trimspaces
Provides:       tex-trimspaces = %{tl_version}
License:        LPPL
Summary:        Trim spaces around an argument or within a macro
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(trimspaces.sty) = %{tl_version}

%description -n texlive-trimspaces
A very short package that allows you to expandably remove
spaces around a token list (commands are provided to remove
spaces before, spaces after, or both); or to remove surrounding
spaces within a macro definition, or to define space-stripped
macros.

%package -n texlive-trimspaces-doc
Summary:        Documentation for trimspaces
Version:        svn15878.1.1

Provides:       tex-trimspaces-doc
AutoReqProv:    No

%description -n texlive-trimspaces-doc
Documentation for trimspaces

%package -n texlive-trivfloat
Provides:       tex-trivfloat = %{tl_version}
License:        LPPL
Summary:        Quick float definitions in LaTeX
Version:        svn15878.1.3b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(floatrow.sty), tex(float.sty)
Provides:       tex(trivfloat.sty) = %{tl_version}

%description -n texlive-trivfloat
The trivfloat package provides a quick method for defining new
float types in LaTeX. A single command sets up a new float in
the same style as the LaTeX kernel figure and table float
types. The package works with memoir as well as the standard
classes.

%package -n texlive-trivfloat-doc
Summary:        Documentation for trivfloat
Version:        svn15878.1.3b

Provides:       tex-trivfloat-doc
AutoReqProv:    No

%description -n texlive-trivfloat-doc
Documentation for trivfloat

%package -n texlive-trsym
Provides:       tex-trsym = %{tl_version}
License:        LPPL 1.2
Summary:        Symbols for transformations
Version:        svn18732.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(trsy10.tfm) = %{tl_version}, tex(trsy12.tfm) = %{tl_version}
Provides:       tex(trsym.sty) = %{tl_version}, tex(utrsy.fd) = %{tl_version}

%description -n texlive-trsym
The bundle provides Metafont source for a small font used for
(e.g.) Laplace transformations, together with a LaTeX .fd file
and a package providing commands for the symbols' use in
mathematics.

%package -n texlive-trsym-doc
Summary:        Documentation for trsym
Version:        svn18732.1.0

Provides:       tex-trsym-doc
AutoReqProv:    No

%description -n texlive-trsym-doc
Documentation for trsym

%package -n texlive-truncate
Provides:       tex-truncate = %{tl_version}
License:        Public Domain
Summary:        Truncate text to a specified width
Version:        svn18921.3.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(truncate.sty) = %{tl_version}

%description -n texlive-truncate
The package will by default break at word boundaries, but
package options are offered to permit breaks within words.

%package -n texlive-truncate-doc
Summary:        Documentation for truncate
Version:        svn18921.3.6

Provides:       tex-truncate-doc
AutoReqProv:    No

%description -n texlive-truncate-doc
Documentation for truncate

%package -n texlive-tucv
Provides:       tex-tucv = %{tl_version}
License:        CC-BY-SA
Summary:        Support for typesetting a CV or resumee
Version:        svn20680.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(color.sty), tex(calc.sty), tex(fancyhdr.sty)
Requires:       tex(xparse.sty)
Provides:       tex(tucv.sty) = %{tl_version}

%description -n texlive-tucv
The package provides commands for typesetting a CV or resume.
It provides commands for general-purpose headings, entries, and
item/description pairs, as well as more specific commands for
formatting sections, with explicit inclusion of school, degree,
employer, job, conference, and publications entries. It tends
to produce a somewhat long and quite detailed document but may
also be suitable to support a shorter resume. The package
relies on a 'sufficiently recent' copy of the l3kernel and
l3packages bundles.

%package -n texlive-tucv-doc
Summary:        Documentation for tucv
Version:        svn20680.1.0

Provides:       tex-tucv-doc
AutoReqProv:    No

%description -n texlive-tucv-doc
Documentation for tucv

%package -n texlive-turkmen
Provides:       tex-turkmen = %{tl_version}
License:        LPPL
Summary:        Babel support for Turkmen
Version:        svn17748.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(turkmen.ldf) = %{tl_version}

%description -n texlive-turkmen
The package provides support for Turkmen in babel, but
integration with babel is not available.

%package -n texlive-turkmen-doc
Summary:        Documentation for turkmen
Version:        svn17748.0.2

Provides:       tex-turkmen-doc
AutoReqProv:    No

%description -n texlive-turkmen-doc
Documentation for turkmen

%package -n texlive-turnthepage
Provides:       tex-turnthepage = %{tl_version}
License:        LPPL
Summary:        Provide "turn page" instructions
Version:        svn29803.1.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(atbegshi.sty), tex(picture.sty), tex(zref-abspage.sty), tex(zref-lastpage.sty)
Requires:       tex(alphalph.sty), tex(pageslts.sty)
Provides:       tex(turnpageetex.sty) = %{tl_version}, tex(turnpagewoetex.sty) = %{tl_version}
Provides:       tex(turnthepage.sty) = %{tl_version}

%description -n texlive-turnthepage
The package prints a 'turn' instruction at the bottom of odd-
numbered pages (except the last). This is a common convention
for examination papers and the like.

%package -n texlive-turnthepage-doc
Summary:        Documentation for turnthepage
Version:        svn29803.1.3a

Provides:       tex-turnthepage-doc
AutoReqProv:    No

%description -n texlive-turnthepage-doc
Documentation for turnthepage

%package -n texlive-twoinone
Provides:       tex-twoinone = %{tl_version}
License:        Public Domain
Summary:        Print two pages on a single page
Version:        svn17024.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(2in1.sty) = %{tl_version}

%description -n texlive-twoinone
The package is for printing two pages on a single (landscape)
A4 page. Page numbers appear on the included pages, and not on
the landscape 'container' page.

%package -n texlive-twoinone-doc
Summary:        Documentation for twoinone
Version:        svn17024.0

Provides:       tex-twoinone-doc
AutoReqProv:    No

%description -n texlive-twoinone-doc
Documentation for twoinone

%package -n texlive-twoup
Provides:       tex-twoup = %{tl_version}
License:        LPPL
Summary:        Print two virtual pages on each physical page
Version:        svn15878.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(twoup.sty) = %{tl_version}

%description -n texlive-twoup
MiKTeX and many other TeX implementations include tools for
massaging PostScript into booklet and two-up printing -- that
is, printing two logical pages side by side on one side of one
sheet of paper. However, some LaTeX preliminaries are necessary
to use those tools. The twoup package provides such
preliminaries and gives advice on how to use the PostScript
tools.

%package -n texlive-twoup-doc
Summary:        Documentation for twoup
Version:        svn15878.1.3

Provides:       tex-twoup-doc
AutoReqProv:    No

%description -n texlive-twoup-doc
Documentation for twoup

%package -n texlive-txgreeks
Provides:       tex-txgreeks = %{tl_version}
License:        LPPL 1.3
Summary:        Shape selection for TX fonts Greek letters
Version:        svn21839.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(txfonts.sty)
Provides:       tex(txgreeks.sty) = %{tl_version}

%description -n texlive-txgreeks
The package allows LaTeX users who use the TX fonts to select
the shapes (italic or upright) for the Greek lowercase and
uppercase letters. Once the shapes for lowercase and uppercase
have been selected via a package option, the \other prefix
(e.g., \otheralpha) allows using the alternate glyph (as in the
fourier package). The txgreeks package does not constrain the
text font that may be used in the document.

%package -n texlive-txgreeks-doc
Summary:        Documentation for txgreeks
Version:        svn21839.1.0

Provides:       tex-txgreeks-doc
AutoReqProv:    No

%description -n texlive-txgreeks-doc
Documentation for txgreeks

%package -n texlive-type1cm
Provides:       tex-type1cm = %{tl_version}
License:        LPPL
Summary:        Arbitrary size font selection in LaTeX
Version:        svn21820.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(type1cm.sty) = %{tl_version}

%description -n texlive-type1cm
LaTeX, by default, restricts the sizes at which you can use its
default computer modern fonts, to a fixed set of discrete sizes
(effectively, a set specified by Knuth). The type1cm package
removes this restriction; this is particularly useful when
using scalable versions of the cm fonts (Bakoma, or the
versions from BSR/Y&Y, or True Type versions from Kinch, PCTeX,
etc.). In fact, since modern distributions will automatically
generate any bitmap font you might need, type1cm has wider
application than just those using scaleable versions of the
fonts. Note that the LaTeX distribution now contains a package
fix-cm, which performs the task of type1cm, as well as doing
the same job for T1- and TS1-encoded ec fonts.

%package -n texlive-type1cm-doc
Summary:        Documentation for type1cm
Version:        svn21820.0

Provides:       tex-type1cm-doc
AutoReqProv:    No

%description -n texlive-type1cm-doc
Documentation for type1cm

%package -n texlive-typeface
Provides:       tex-typeface = %{tl_version}
License:        LPPL 1.3
Summary:        Select a balanced set of fonts
Version:        svn27046.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifetex.sty), tex(etexcmds.sty), tex(etoolbox.sty), tex(ifthenx.sty)
Requires:       tex(iftex.sty), tex(ifpdf.sty), tex(xkeyval.sty), tex(fix-cm.sty)
Requires:       tex(nfssext-cfr.sty), tex(scalefnt.sty), tex(xcolor.sty)
Provides:       tex(typeface.cfg) = %{tl_version}, tex(typeface.sty) = %{tl_version}

%description -n texlive-typeface
The package provides the means of establishing a consistent set
of fonts for use in a LaTeX document. It allows mixing and
matching the Type 1 font sets available on the archive (and it
may be extended, via its configuration file, to support other
fonts). Font-set definition takes the form of a set of options
that are read when the package is loaded: for each typographic
category (main body font, sans-serif font, monospace font,
mathematics fonts, text figures, and so on), a font or a
transformation is given in those options. The approach enables
the user to remember their own configurations (as a single
command) and to borrow configurations that other users have
developed. The present release is designated "for review".

%package -n texlive-typeface-doc
Summary:        Documentation for typeface
Version:        svn27046.0.1

Provides:       tex-typeface-doc
AutoReqProv:    No

%description -n texlive-typeface-doc
Documentation for typeface

%package -n texlive-typogrid
Provides:       tex-typogrid = %{tl_version}
License:        LPPL
Summary:        Print a typographic grid
Version:        svn24994.0.21

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(keyval.sty), tex(eso-pic.sty)
Provides:       tex(typogrid.sty) = %{tl_version}

%description -n texlive-typogrid
Draws a grid on every page of the document; the grid divides
the page into columns, and may be used for fixing measurements
of layout.

%package -n texlive-typogrid-doc
Summary:        Documentation for typogrid
Version:        svn24994.0.21

Provides:       tex-typogrid-doc
AutoReqProv:    No

%description -n texlive-typogrid-doc
Documentation for typogrid

%package -n texlive-thesis-ekf
Provides:       tex-thesis-ekf = %{tl_version}
License:        LPPL 1.2
Summary:        Thesis class for Eszterhazy Karoly College
Version:        svn46534
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(geometry.sty), tex(hyperref.sty)
Provides:       tex(thesis-ekf.cls) = %{tl_version}

%description -n texlive-thesis-ekf
The distribution contains the files to generate the thesis
class as well as three templates.

%package -n texlive-thesis-ekf-doc
Summary:        Documentation for thesis-ekf
Version:        svn46534
Provides:       tex-thesis-ekf-doc
AutoReqProv:    No

%description -n texlive-thesis-ekf-doc
Documentation for thesis-ekf

%package -n texlive-thesis-titlepage-fhac
Provides:       tex-thesis-titlepage-fhac = %{tl_version}
License:        LPPL
Summary:        Little style to create a standard titlepage for diploma thesis
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(figbib.sty), tex(gloss.sty)
Provides:       tex(fhACtitlepage.cfg) = %{tl_version}, tex(fhACtitlepage.sty) = %{tl_version}
Provides:       tex(figbib_add.sty) = %{tl_version}, tex(gloss_add.sty) = %{tl_version}

%description -n texlive-thesis-titlepage-fhac
Yet another thesis titlepage style: support of Fachhochschule
Aachen (Standort Juelich)

%package -n texlive-thesis-titlepage-fhac-doc
Summary:        Documentation for thesis-titlepage-fhac
Version:        svn15878.0.1

Provides:       tex-thesis-titlepage-fhac-doc
AutoReqProv:    No

%description -n texlive-thesis-titlepage-fhac-doc
Documentation for thesis-titlepage-fhac

%package -n texlive-thuthesis
Provides:       tex-thuthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis template for Tsinghua University
Version:        svn47740
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(ifthen.sty), tex(calc.sty), tex(amsmath.sty)
Requires:       tex(txfonts.sty), tex(graphicx.sty), tex(subcaption.sty), tex(paralist.sty)
Requires:       tex(footmisc.sty), tex(CJKfntef.sty), tex(CJKspace.sty), tex(ntheorem.sty)
Requires:       tex(array.sty), tex(longtable.sty), tex(booktabs.sty), tex(natbib.sty)
Requires:       tex(hyperref.sty), tex(multirow.sty), tex(tabularx.sty), tex(diagbox.sty)
Requires:       tex(float.sty)
Provides:       tex(thufonts.def) = %{tl_version}, tex(thuthesis.cfg) = %{tl_version}
Provides:       tex(thuthesis.cls) = %{tl_version}, tex(thutils.sty) = %{tl_version}

%description -n texlive-thuthesis
ThuThesis is a LaTeX thesis template package for Tsinghua
University in order to make it easy to write theses for either
bachelor's, master's or doctor's degree.

%package -n texlive-thuthesis-doc
Summary:        Documentation for thuthesis
Version:        svn47740
Provides:       tex-thuthesis-doc
AutoReqProv:    No

%description -n texlive-thuthesis-doc
Documentation for thuthesis

%package -n texlive-toptesi
Provides:       tex-toptesi = %{tl_version}
License:        LPPL 1.3
Summary:        Bundle for typesetting multilanguage theses
Version:        svn47699
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty), tex(textcomp.sty), tex(etoolbox.sty), tex(fontspec.sty)
Requires:       tex(polyglossia.sty), tex(babel.sty), tex(graphicx.sty), tex(pdfx.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(topcoman.sty) = %{tl_version}, tex(topfront.sty) = %{tl_version}
Provides:       tex(toptesi.cfg) = %{tl_version}, tex(toptesi.cls) = %{tl_version}
Provides:       tex(toptesi.sty) = %{tl_version}

%description -n texlive-toptesi
This bundle contains everything is needed for typesetting a
bachelor, master or PhD thesis in Italian (or in any other
language supported by LaTeX: the bundle is constructed to
support multilingual use). The infix strings may be selected
and specified at will by means of a configuration file, so as
to customize the layout of the front page to the requirements
of a specific university. Thanks to its language management,
the bundle is suited for multilanguage theses that are becoming
more and more frequent thanks to the double degree programs of
the European Community Socrates programs. Toptesi is designed
to save the PDF version of a thesis in PDF/A-1b compliant mode
and with all the necessary metadata.

%package -n texlive-toptesi-doc
Summary:        Documentation for toptesi
Version:        svn47699
Provides:       tex-toptesi-doc
AutoReqProv:    No

%description -n texlive-toptesi-doc
Documentation for toptesi

%package -n texlive-tudscr
Provides:       tex-tudscr = %{tl_version}
License:        LPPL 1.3
Summary:        The Corporate Design of TU Dresden
Version:        svn44480
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontspec.sty), tex(textcase.sty), tex(environ.sty), tex(graphicx.sty)
Requires:       tex(trimspaces.sty), tex(scrlayer-scrpage.sty)
Requires:       tex(geometry.sty), tex(scrbase.sty), tex(kvsetkeys.sty), tex(etoolbox.sty)
Requires:       tex(xcolor.sty), tex(dox.sty), tex(csquotes.sty), tex(mweights.sty)
Requires:       tex(lmodern.sty), tex(xspace.sty), tex(scrhack.sty), tex(scrextend.sty)
Requires:       tex(xparse.sty), tex(textcomp.sty), tex(setspace.sty), tex(babel.sty)
Requires:       tex(microtype.sty), tex(quoting.sty), tex(isodate.sty), tex(hologo.sty)
Requires:       tex(marginnote.sty), tex(listings.sty), tex(silence.sty), tex(filemod.sty)
Requires:       tex(ifpdf.sty), tex(todonotes.sty), tex(ifplatform.sty), tex(hyperref.sty)
Requires:       tex(bookmark.sty), tex(imakeidx.sty), tex(enumitem.sty), tex(ellipsis.sty)
Requires:       tex(tabularx.sty), tex(ragged2e.sty), tex(chngcntr.sty), tex(booktabs.sty)
Requires:       tex(varioref.sty), tex(tikz.sty), tex(pdfpages.sty), tex(units.sty)
Requires:       tex(auto-pst-pdf.sty), tex(scrwfile.sty)
Requires:       tex(filecontents.sty), tex(hyphsubst.sty)
Provides:       tex(mathswap.sty) = %{tl_version}, tex(tudscrartcl.cls) = %{tl_version}
Provides:       tex(tudscrbase.sty) = %{tl_version}, tex(tudscrbook.cls) = %{tl_version}
Provides:       tex(tudscrcolor.sty) = %{tl_version}, tex(tudscrcomp.sty) = %{tl_version}
Provides:       tex(tudscrdoc.cls) = %{tl_version}, tex(tudscrfonts.sty) = %{tl_version}
Provides:       tex(tudscrman.cls) = %{tl_version}, tex(tudscrman.sty) = %{tl_version}
Provides:       tex(tudscrreprt.cls) = %{tl_version}, tex(tudscrsupervisor.sty) = %{tl_version}
Provides:       tex(twocolfix.sty) = %{tl_version}

%description -n texlive-tudscr
The TUD-KOMA-Script bundle provides both classes and packages
in order to create LaTeX documents in the corporate design of
the Technische Universitat Dresden. It bases on the KOMA-Script
bundle, which must necessarily be present. In addition, the
PostScript font families Univers and DIN-Bold should be
installed. Otherwise, the document classes can admittedly be
used, but in this case, the created documents do not correspond
to the originally thought style. Employees and students of the
Technische Universitat Dresden can request these fonts via
https://tu-dresden.de/service/publizieren/cd/4_latex from the
university marketing university marketing with regard to the
use of LaTeX. To install the PostScript fonts, please refer to
the corresponding release under https://github.com/tud-
cd/tudscr/releases/tag/fonts and the LaTeX forum of the
Technische Universitat Dresden: http://latex.wcms-file3.tu-
dresden.de/phpBB3/index.php The bundle offers: the three
document classes tudscrartcl, tudscrreprt and tudscrbook which
serve as wrapper classes for scrartcl, scrreprt and scrbook.
the package tudscrsupervisor providing environments and macros
to create tasks, evaluations and notices for scientific theses,
the package tudscrfonts, which makes the corporate design fonts
of the Technische Universitat Dresden available for LaTeX
standard classes and KOMA-Script classes, the package mathswap
for swapping math delimiters within numbers (similar to
ionumbers), and the package twocolfix for fixing the
positioning bug of headings in two column layout, a
comprehensive user documentation as well as several tutorials.

%package -n texlive-tudscr-doc
Summary:        Documentation for tudscr
Version:        svn44480
Provides:       tex-tudscr-doc
AutoReqProv:    No

%description -n texlive-tudscr-doc
Documentation for tudscr

%package -n texlive-tugboat
Provides:       tex-tugboat = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX macros for TUGboat articles
Version:        svn45713
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(mflogo.sty)
Provides:       tex(ltugboat.cls) = %{tl_version}, tex(ltugboat.sty) = %{tl_version}
Provides:       tex(ltugcomn.sty) = %{tl_version}, tex(ltugproc.cls) = %{tl_version}
Provides:       tex(ltugproc.sty) = %{tl_version}

%description -n texlive-tugboat
Provides ltugboat.cls for both regular and proceedings issues
of the TUGboat journal. The distribution also includes a BibTeX
style appropriate for use with the classes' "harvard" option.

%package -n texlive-tugboat-doc
Summary:        Documentation for tugboat
Version:        svn45713
Provides:       tex-tugboat-doc
AutoReqProv:    No

%description -n texlive-tugboat-doc
Documentation for tugboat

%package -n texlive-tugboat-plain
Provides:       tex-tugboat-plain = %{tl_version}
License:        Bibtex
Summary:        Plain TeX macros for TUGboat
Version:        svn43560
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(tugboat.sty) = %{tl_version}, tex(tugproc.sty) = %{tl_version}

%description -n texlive-tugboat-plain
The macros defined in this directory (in files tugboat.sty and
tugboat.cmn) are used in papers written in Plain TeX for
publication in TUGboat.

%package -n texlive-tugboat-plain-doc
Summary:        Documentation for tugboat-plain
Version:        svn43560
Provides:       tex-tugboat-plain-doc
AutoReqProv:    No

%description -n texlive-tugboat-plain-doc
Documentation for tugboat-plain

%package -n texlive-turabian
Provides:       tex-turabian = %{tl_version}
License:        LPPL
Summary:        Create Turabian-formatted material using LaTeX
Version:        svn36298.0.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(turabian.cls) = %{tl_version}

%description -n texlive-turabian
The bundle provides a class file and a template for creating
Turabian-formatted projects. The class file supports citation
formatting conforming to the Turabian 8th Edition style guide.

%package -n texlive-turabian-doc
Summary:        Documentation for turabian
Version:        svn36298.0.1.0

Provides:       tex-turabian-doc
AutoReqProv:    No

%description -n texlive-turabian-doc
Documentation for turabian

%package -n texlive-tui
Provides:       tex-tui = %{tl_version}
License:        LPPL
Summary:        Thesis style for the University of the Andes, Colombia
Version:        svn27253.1.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(inputenc.sty), tex(makeidx.sty), tex(babel.sty)
Requires:       tex(microtype.sty), tex(kpfonts.sty), tex(mathptmx.sty), tex(hyperref.sty)
Requires:       tex(amsmath.sty), tex(amsthm.sty), tex(amssymb.sty), tex(xcolor.sty)
Requires:       tex(graphicx.sty), tex(courier.sty), tex(csquotes.sty), tex(breakurl.sty)
Requires:       tex(MnSymbol.sty)
Provides:       tex(tui.cls) = %{tl_version}

%description -n texlive-tui
Doctoral Dissertations from the Faculty of Engineering at the
Universidad de los Andes, Bogota, Colombia. The class is
implemented as an extension of the memoir class. Clase de Tesis
doctorales para ingenieria, Universidad de los Andes, Bogota.

%package -n texlive-tui-doc
Summary:        Documentation for tui
Version:        svn27253.1.9

Provides:       tex-tui-doc
AutoReqProv:    No

%description -n texlive-tui-doc
Documentation for tui

%package -n texlive-t-angles
Provides:       tex-t-angles = %{tl_version}
License:        GPL+
Summary:        Draw tangles, trees, Hopf algebra operations and other pictures
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty)
Provides:       tex(t-angles.sty) = %{tl_version}

%description -n texlive-t-angles
A LaTeX2e package for drawing tangles, trees, Hopf algebra
operations and other pictures. It is based on emTeX or TPIC
\specials. Therefore, it can be used with the most popular
drivers, including emTeX drivers, dviwin, xdvi and dvips, and
(using some code from ConTeXt) it may also be used with
PDFLaTeX.

%package -n texlive-t-angles-doc
Summary:        Documentation for t-angles
Version:        svn15878.0

Provides:       tex-t-angles-doc
AutoReqProv:    No

%description -n texlive-t-angles-doc
Documentation for t-angles

%package -n texlive-tipa-de-doc
Summary:        Documentation for tipa-de
Version:        svn22005.1.3

Provides:       tex-tipa-de-doc
AutoReqProv:    No

%description -n texlive-tipa-de-doc
Documentation for tipa-de

%package -n texlive-translation-arsclassica-de-doc
Summary:        Documentation for translation-arsclassica-de
Version:        svn23803.0

Provides:       tex-translation-arsclassica-de-doc
AutoReqProv:    No

%description -n texlive-translation-arsclassica-de-doc
Documentation for translation-arsclassica-de

%package -n texlive-translation-biblatex-de-doc
Summary:        Documentation for translation-biblatex-de
Version:        svn42198
Provides:       tex-translation-biblatex-de-doc
AutoReqProv:    No

%description -n texlive-translation-biblatex-de-doc
Documentation for translation-biblatex-de

%package -n texlive-translation-chemsym-de-doc
Summary:        Documentation for translation-chemsym-de
Version:        svn23804.0

Provides:       tex-translation-chemsym-de-doc
AutoReqProv:    No

%description -n texlive-translation-chemsym-de-doc
Documentation for translation-chemsym-de

%package -n texlive-translation-ecv-de-doc
Summary:        Documentation for translation-ecv-de
Version:        svn24754.0

Provides:       tex-translation-ecv-de-doc
AutoReqProv:    No

%description -n texlive-translation-ecv-de-doc
Documentation for translation-ecv-de

%package -n texlive-translation-enumitem-de-doc
Summary:        Documentation for translation-enumitem-de
Version:        svn24196.0

Provides:       tex-translation-enumitem-de-doc
AutoReqProv:    No

%description -n texlive-translation-enumitem-de-doc
Documentation for translation-enumitem-de

%package -n texlive-translation-europecv-de-doc
Summary:        Documentation for translation-europecv-de
Version:        svn23840.0

Provides:       tex-translation-europecv-de-doc
AutoReqProv:    No

%description -n texlive-translation-europecv-de-doc
Documentation for translation-europecv-de

%package -n texlive-translation-filecontents-de-doc
Summary:        Documentation for translation-filecontents-de
Version:        svn24010.0

Provides:       tex-translation-filecontents-de-doc
AutoReqProv:    No

%description -n texlive-translation-filecontents-de-doc
Documentation for translation-filecontents-de

%package -n texlive-translation-moreverb-de-doc
Summary:        Documentation for translation-moreverb-de
Version:        svn23957.0

Provides:       tex-translation-moreverb-de-doc
AutoReqProv:    No

%description -n texlive-translation-moreverb-de-doc
Documentation for translation-moreverb-de

%package -n texlive-tikz-feynman-doc
Provides:       tex-tikz-feynman-doc = %{tl_version}
License:        GPLv3+
Summary:        doc files of tikz-feynman
Version:        svn39582

AutoReqProv:    No

%description -n texlive-tikz-feynman-doc
Documentation for tikz-feynman

%package -n texlive-tikz-feynman
Provides:       tex-tikz-feynman = %{tl_version}
License:        LPPL
Summary:        Feynman diagrams with TikZ
Version:        svn39582

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tikz-feynman.sty) = %{tl_version}, tex(tikzfeynman.keys.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryfeynman.code.tex) = %{tl_version}

%description -n texlive-tikz-feynman
This is a is a LaTeX package allowing Feynman diagrams to be
easily generated within LaTeX with minimal user instructions
and without the need of external programs. It builds upon the
TikZ package and leverages the graph placement algorithms from
TikZ in order to automate the placement of many vertices. tikz-
feynman still allows fine-tuned placement of vertices so that
even complex diagrams can still be generated with ease.

%package -n texlive-tikzinclude
Provides:       tex-tikzinclude = %{tl_version}
License:        LPPL 1.3
Summary:        Import TikZ images from colletions
Version:        svn28715.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty), tex(etoolbox.sty)
Provides:       tex(tikzinclude.sty) = %{tl_version}

%description -n texlive-tikzinclude
The package addresses the problem of importing only one TikZ-
image from a file holding multiple images.

%package -n texlive-tikzinclude-doc
Summary:        Documentation for tikzinclude
Version:        svn28715.1.0

Provides:       tex-tikzinclude-doc
AutoReqProv:    No

%description -n texlive-tikzinclude-doc
Documentation for tikzinclude

%package -n texlive-tikzmark
Provides:       tex-tikzmark = %{tl_version}
License:        LPPL 1.3
Summary:        Use TikZ's method of remembering a position on a page
Version:        svn44475
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(tikzlibrarytikzmark.code.tex) = %{tl_version}
Provides:       tex(tikzmarklibrarylistings.code.tex) = %{tl_version}

%description -n texlive-tikzmark
The tikzmark package defines a command to "remember" a position
on a page for later (or earlier) use, primarily (but not
exclusively) with TikZ.

%package -n texlive-tikzmark-doc
Summary:        Documentation for tikzmark
Version:        svn44475
Provides:       tex-tikzmark-doc
AutoReqProv:    No

%description -n texlive-tikzmark-doc
Documentation for tikzmark

%package -n texlive-tikzorbital
Provides:       tex-tikzorbital = %{tl_version}
License:        LPPL
Summary:        Atomic and molecular orbitals using TiKZ
Version:        svn36439.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty)
Provides:       tex(tikzorbital.sty) = %{tl_version}

%description -n texlive-tikzorbital
Atomic s, p and d orbitals may be drawn, as well as molecular
orbital diagrams.

%package -n texlive-tikzorbital-doc
Summary:        Documentation for tikzorbital
Version:        svn36439.0

Provides:       tex-tikzorbital-doc
AutoReqProv:    No

%description -n texlive-tikzorbital-doc
Documentation for tikzorbital

%package -n texlive-tikzpagenodes
Provides:       tex-tikzpagenodes = %{tl_version}
License:        LPPL
Summary:        A single TikZ node for the whole page
Version:        svn27723.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifoddpage.sty)
Provides:       tex(tikzpagenodes.sty) = %{tl_version}

%description -n texlive-tikzpagenodes
The package provides special PGF/TikZ nodes for the text,
marginpar, footer and header area of the current page. They are
inspired by the 'current page' node defined by PGF/TikZ itself.

%package -n texlive-tikzpagenodes-doc
Summary:        Documentation for tikzpagenodes
Version:        svn27723.1.1

Provides:       tex-tikzpagenodes-doc
AutoReqProv:    No

%description -n texlive-tikzpagenodes-doc
Documentation for tikzpagenodes

%package -n texlive-tikzpfeile
Provides:       tex-tikzpfeile = %{tl_version}
License:        LPPL
Summary:        Draw arrows using PGF/TikZ
Version:        svn25777.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(kvoptions.sty)
Provides:       tex(tikzpfeile.sty) = %{tl_version}

%description -n texlive-tikzpfeile
In a document with a lot of diagrams created with PGF/TikZ,
there is a possibility of the reader being distracted by
different sorts of arrowheads in the diagrams and in the text
(as, e.g., in \rightarrow). The package defines macros to
create all arrows using PGF/TikZ, so as to avoid the problem.

%package -n texlive-tikzpfeile-doc
Summary:        Documentation for tikzpfeile
Version:        svn25777.1.0

Provides:       tex-tikzpfeile-doc
AutoReqProv:    No

%description -n texlive-tikzpfeile-doc
Documentation for tikzpfeile

%package -n texlive-tikzposter
Provides:       tex-tikzposter = %{tl_version}
License:        LPPL 1.2
Summary:        Create scientific posters using TikZ
Version:        svn32732.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty)
Provides:       tex(tikzposter.cls) = %{tl_version}, tex(tikzposterBackgroundstyles.tex) = %{tl_version}
Provides:       tex(tikzposterBlockstyles.tex) = %{tl_version}
Provides:       tex(tikzposterColorpalettes.tex) = %{tl_version}
Provides:       tex(tikzposterColorstyles.tex) = %{tl_version}
Provides:       tex(tikzposterInnerblockstyles.tex) = %{tl_version}
Provides:       tex(tikzposterLayoutthemes.tex) = %{tl_version}
Provides:       tex(tikzposterNotestyles.tex) = %{tl_version}
Provides:       tex(tikzposterTitlestyles.tex) = %{tl_version}

%description -n texlive-tikzposter
A document class provides a simple way of using TikZ for
generating posters. Several formatting options are available,
and spacing and layout of the poster is to a large extent
automated.

%package -n texlive-tikzposter-doc
Summary:        Documentation for tikzposter
Version:        svn32732.2.0

Provides:       tex-tikzposter-doc
AutoReqProv:    No

%description -n texlive-tikzposter-doc
Documentation for tikzposter

%package -n texlive-tikzscale
Provides:       tex-tikzscale = %{tl_version}
License:        LPPL 1.3
Summary:        Resize pictures while respecting text size
Version:        svn30637.0.2.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(etoolbox.sty), tex(pgfkeys.sty), tex(xparse.sty)
Requires:       tex(letltxmacro.sty), tex(xstring.sty)
Provides:       tex(tikzscale.sty) = %{tl_version}

%description -n texlive-tikzscale
The package extends the \includegraphics command to support
tikzpictures. It allows scaling of TikZ images and PGFPlots to
a given width or height without changing the text size.

%package -n texlive-tikzscale-doc
Summary:        Documentation for tikzscale
Version:        svn30637.0.2.6

Provides:       tex-tikzscale-doc
AutoReqProv:    No

%description -n texlive-tikzscale-doc
Documentation for tikzscale

%package -n texlive-tikzsymbols
Provides:       tex-tikzsymbols = %{tl_version}
License:        LPPL 1.3
Summary:        Some symbols created using TikZ
Version:        svn47730
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(xargs.sty), tex(xcolor.sty), tex(xkeyval.sty)
Requires:       tex(xspace.sty), tex(calc.sty)
Provides:       tex(tikzsymbols.sty) = %{tl_version}

%description -n texlive-tikzsymbols
The package provides various emoticons, cooking symbols and
trees.

%package -n texlive-tikzsymbols-doc
Summary:        Documentation for tikzsymbols
Version:        svn47730
Provides:       tex-tikzsymbols-doc
AutoReqProv:    No

%description -n texlive-tikzsymbols-doc
Documentation for tikzsymbols

%package -n texlive-timing-diagrams
Provides:       tex-timing-diagrams = %{tl_version}
License:        LPPL 1.3
Summary:        Draw timing diagrams
Version:        svn31491.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty)
Provides:       tex(timing-diagrams.sty) = %{tl_version}

%description -n texlive-timing-diagrams
The package provides commands to draw and annotate various
kinds of timing diagrams, using Tikz. Documentation is sparse,
but the source and the examples file should be of some use.

%package -n texlive-timing-diagrams-doc
Summary:        Documentation for timing-diagrams
Version:        svn31491.0

Provides:       tex-timing-diagrams-doc
AutoReqProv:    No

%description -n texlive-timing-diagrams-doc
Documentation for timing-diagrams

%package -n texlive-timetable
Provides:       tex-timetable = %{tl_version}
License:        LPPL
Summary:        Generate timetables
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(timetable.tex) = %{tl_version}

%description -n texlive-timetable
A highly-configurable package, with nice output and simple
input. The macros use a radix sort mechanism so that the order
of input is not critical.

%package -n texlive-treetex
Provides:       tex-treetex = %{tl_version}
License:        Public Domain
Summary:        Draw trees
Version:        svn28176.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(classes.tex) = %{tl_version}, tex(l_pic.tex) = %{tl_version}
Provides:       tex(treetex.tex) = %{tl_version}

%description -n texlive-treetex
Macros to draw trees, within TeX (or LaTeX). The algorithm used
is discussed in an accompanying paper (written using LaTeX
2.09).

%package -n texlive-treetex-doc
Summary:        Documentation for treetex
Version:        svn28176.0

Provides:       tex-treetex-doc
AutoReqProv:    No

%description -n texlive-treetex-doc
Documentation for treetex

%package -n texlive-thaienum
Summary:        Thai labels in enumerate environments
Version:        svn44140
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(thaienum.sty) = %{tl_version}

%description -n texlive-thaienum
This LaTeX package provides a command to use Thai numerals or
characters as labels in enumerate environments. Once the
package is loaded with \usepackage{thaienum} you can use labels
such as \thainum* or \thaimultialph* in conjunction with the
package enumitem. Concrete examples are given in the
documentation.

%package -n texlive-tikzcodeblocks
Summary:        Helps to draw codeblocks like scratch, NEPO and PXT in TikZ
Version:        svn47265
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzcodeblocks.sty) = %{tl_version}

%description -n texlive-tikzcodeblocks
tikzcodeblocks is a LaTeX package for typesetting blockwise
graphic programming languages like scratch, nepo or pxt.

%package -n texlive-tikzducks
Summary:        A little fun package for using rubber ducks in TikZ
Version:        svn48176
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzducks.sty) = %{tl_version}

%description -n texlive-tikzducks
The package is a LaTeX package for ducks to be used in TikZ
pictures. This project is a continuation of an answer at
StackExchange How we can draw a duck?

%package -n texlive-tikz-kalender
Summary:        A LaTeX based calendar using TikZ
Version:        svn46224
License:        CC-BY-SA
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikz-kalender-translation.clo) = %{tl_version}
Provides:       tex(tikz-kalender.cls) = %{tl_version}

%description -n texlive-tikz-kalender
For usage see the example files tikz-kalender-example1.tex,
tikz-kalender-example2.tex, and *.events. The Code is inspired
by this document and has the >>Creative Commons attribution
license (CC-BY-SA)<<. The class tikz-kalender requires the
package TikZ and the TikZ libraries calc and calendar.

%package -n texlive-tikz-optics
Summary:        A library for drawing optical setups with TikZ
Version:        svn43466
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzlibraryoptics.code.tex) = %{tl_version}

%description -n texlive-tikz-optics
This package provides a new TikZ library designed to easily
draw optical setups with TikZ. It provides shapes for lens,
mirror, etc. The geometrically (in)correct computation of light
rays through the setup is left to the user.

%package -n texlive-tikzpeople
Summary:        Draw people-shaped nodes in TikZ
Version:        svn43978
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzpeople.shape.alice.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.bob.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.bride.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.builder.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.businessman.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.charlie.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.chef.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.conductor.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.cowboy.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.criminal.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.dave.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.devil.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.duck.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.graduate.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.groom.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.guard.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.jester.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.judge.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.maninblack.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.mexican.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.nun.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.nurse.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.physician.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.pilot.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.police.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.priest.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.sailor.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.santa.sty) = %{tl_version}
Provides:       tex(tikzpeople.shape.surgeon.sty) = %{tl_version}
Provides:       tex(tikzpeople.sty) = %{tl_version}

%description -n texlive-tikzpeople
This package provides people-shaped nodes in the style of
Microsoft Visio clip art, to be used with TikZ. The available,
highly customizable, node shapes are: alice, bob, bride,
builder, businessman, charlie, chef, conductor, cowboy,
criminal, dave, devil, duck, graduate, groom, guard, jester,
judge, maininblack, mexican, nun, nurse, physician, pilot,
police, priest, sailor, santa, surgeon.

%package -n texlive-tocdata
Summary:        Adds names to chapters, sections, figures in the TOC and LOF.
Version:        svn42623
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tocdata.sty) = %{tl_version}

%description -n texlive-tocdata
The package may be used to add a small amount of data to an
entry in the table of contents or list of figures, between the
section name and the page number. The typical use would be to
add the name of an author or artist of a chapter or section,
such as in an anthology or a collection of papers.
Additionally, user-level macros are provided which add the
author's name to a chapter or section, along with an optional
prefix and/or suffix, and add to a figure the artist's name,
prefix, and suffix, plus optional additional text. Author and
artist names are also added to the index. Additional user-level
macros control formatting.

%package -n texlive-txuprcal
Summary:        Upright calligraphic font based on TX calligraphic
Version:        svn43327
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(TXUprCal.map) = %{tl_version}, tex(txUprCal-Bold.tfm) = %{tl_version}
Provides:       tex(txUprCal-Regular.tfm) = %{tl_version}
Provides:       tex(txuprcal-bold.pfb) = %{tl_version}, tex(txuprcal-reg.pfb) = %{tl_version}
Provides:       tex(txuprcal.sty) = %{tl_version}, tex(utxuprcal.fd) = %{tl_version}

%description -n texlive-txuprcal
This small package provides a means of loading as \mathcal an
uprighted version of the calligraphic fonts from the TX font
package. A scaled option to provided to allow arbitrary
scaling.

%package -n texlive-typoaid
Summary:        Macros for font diagnostics
Version:        svn44238
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(typoaid.sty) = %{tl_version}

%description -n texlive-typoaid
This package provides macros for measuring alphabet lengths
(i.e. the length occupied by the characters "abcd...xyz"), em-
widths and ex-heights, which may help in making typesetting
decisions. The package is compatible with pdfLaTeX, LuaLaTeX,
and XeLaTeX, and will accept font family switches defined via
the fontspec package. The plan is that future versions shall be
able to provide even more diagnostic tools, and some LuaTeX-
specific special commands, too. The package relies on the
following other LaTeX packages: expl3, array, booktabs, and
siunitx.

%package -n texlive-tqft
Provides:       tex-tqft = %{tl_version}
License:        LPPL 1.3
Summary:        Drawing TQFT diagrams with TikZ/PGF
Version:        svn44455
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pgfkeys.sty), tex(pgf.sty)
Provides:       tex(tikzlibrarytqft.code.tex) = %{tl_version}
Provides:       tex(tqft.sty) = %{tl_version}

%description -n texlive-tqft
The package defines some node shapes useful for drawing TQFT
diagrams with TikZ/PGF. That is, it defines highly customisable
shapes that look like cobordisms between circles, such as those
used in TQFT and other mathematical diagrams.

%package -n texlive-tqft-doc
Summary:        Documentation for tqft
Version:        svn44455
Provides:       tex-tqft-doc
AutoReqProv:    No

%description -n texlive-tqft-doc
Documentation for tqft

%package -n texlive-tkz-base
Provides:       tex-tkz-base = %{tl_version}
License:        LPPL
Summary:        Tools for drawing with a cartesian coordinate system
Version:        svn22961.1.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(tikz.sty), tex(numprint.sty), tex(fp.sty)
Provides:       tex(tkz-base.cfg) = %{tl_version}, tex(tkz-base.sty) = %{tl_version}
Provides:       tex(tkz-obj-marks.tex) = %{tl_version}, tex(tkz-obj-points.tex) = %{tl_version}
Provides:       tex(tkz-obj-segments.tex) = %{tl_version}
Provides:       tex(tkz-tools-arith.tex) = %{tl_version}
Provides:       tex(tkz-tools-base.tex) = %{tl_version}, tex(tkz-tools-math.tex) = %{tl_version}
Provides:       tex(tkz-tools-misc.tex) = %{tl_version}, tex(tkz-tools-obsolete.tex) = %{tl_version}
Provides:       tex(tkz-tools-utilities.tex) = %{tl_version}

%description -n texlive-tkz-base
The bundle is a set of packages, designed to give mathematics
teachers (and students) easy access to programming of drawings
with TikZ.

%package -n texlive-tkz-base-doc
Summary:        Documentation for tkz-base
Version:        svn22961.1.16

Provides:       tex-tkz-base-doc
AutoReqProv:    No

%description -n texlive-tkz-base-doc
Documentation for tkz-base

%package -n texlive-tkz-berge
Provides:       tex-tkz-berge = %{tl_version}
License:        LPPL
Summary:        Macros for drawing graphs of graph theory
Version:        svn22891.1.00c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tkz-tools-arith.tex), tex(tkz-graph.sty)
Provides:       tex(tkz-arith.sty) = %{tl_version}, tex(tkz-berge.sty) = %{tl_version}

%description -n texlive-tkz-berge
The package provides a collection of useful macros for drawing
classic graphs of graph theory, or to make other graphs.

%package -n texlive-tkz-berge-doc
Summary:        Documentation for tkz-berge
Version:        svn22891.1.00c

Provides:       tex-tkz-berge-doc
AutoReqProv:    No

%description -n texlive-tkz-berge-doc
Documentation for tkz-berge

%package -n texlive-tkz-doc
Provides:       tex-tkz-doc = %{tl_version}
License:        LPPL
Summary:        Documentation macros for the TKZ series of packages
Version:        svn22959.1.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(inputenc.sty), tex(xkeyval.sty), tex(framed.sty)
Requires:       tex(eso-pic.sty), tex(amsmath.sty), tex(amssymb.sty), tex(textcomp.sty)
Requires:       tex(fourier.sty), tex(berasans.sty), tex(beramono.sty), tex(footmisc.sty)
Requires:       tex(scrpage2.sty), tex(makeidx.sty), tex(calc.sty), tex(tikz.sty)
Requires:       tex(multido.sty), tex(lscape.sty), tex(graphicx.sty), tex(array.sty)
Requires:       tex(multicol.sty), tex(multirow.sty), tex(tabularx.sty), tex(ragged2e.sty)
Requires:       tex(booktabs.sty), tex(fixltx2e.sty)
Provides:       tex(tkz-doc.cls) = %{tl_version}, tex(tkzexample.sty) = %{tl_version}

%description -n texlive-tkz-doc
This bundle offers a documentation class (tkz-doc) and a
package (tkzexample). These files are used in the documentation
of the author's packages tkz-tab and tkz-linknodes.

%package -n texlive-tkz-doc-doc
Summary:        Documentation for tkz-doc
Version:        svn22959.1.1c

Provides:       tex-tkz-doc-doc
AutoReqProv:    No

%description -n texlive-tkz-doc-doc
Documentation for tkz-doc

%package -n texlive-tkz-euclide
Provides:       tex-tkz-euclide = %{tl_version}
License:        LPPL
Summary:        Tools for drawing Euclidean geometry
Version:        svn22830.1.16c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tkz-base.sty)
Provides:       tex(tkz-euclide.sty) = %{tl_version}, tex(tkz-lib-symbols.tex) = %{tl_version}
Provides:       tex(tkz-obj-addpoints.tex) = %{tl_version}
Provides:       tex(tkz-obj-angles.tex) = %{tl_version}, tex(tkz-obj-arcs.tex) = %{tl_version}
Provides:       tex(tkz-obj-circles.tex) = %{tl_version}
Provides:       tex(tkz-obj-lines.tex) = %{tl_version}, tex(tkz-obj-polygons.tex) = %{tl_version}
Provides:       tex(tkz-obj-protractor.tex) = %{tl_version}
Provides:       tex(tkz-obj-sectors.tex) = %{tl_version}
Provides:       tex(tkz-obj-vectors.tex) = %{tl_version}
Provides:       tex(tkz-tools-intersections.tex) = %{tl_version}
Provides:       tex(tkz-tools-transformations.tex) = %{tl_version}

%description -n texlive-tkz-euclide
The tkz-euclide package is a set of files, designed to give
math teachers and students) easy access at the programming of
Euclidean geometry with TikZ.

%package -n texlive-tkz-euclide-doc
Summary:        Documentation for tkz-euclide
Version:        svn22830.1.16c

Provides:       tex-tkz-euclide-doc
AutoReqProv:    No

%description -n texlive-tkz-euclide-doc
Documentation for tkz-euclide

%package -n texlive-tkz-fct
Provides:       tex-tkz-fct = %{tl_version}
License:        LPPL
Summary:        Tools for drawing graphs of functions
Version:        svn22831.1.16c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tkz-base.sty)
Provides:       tex(tkz-fct.sty) = %{tl_version}

%description -n texlive-tkz-fct
The tkz-fct package is designed to give math teachers (and
students) easy access to programming graphs of functions with
TikZ and gnuplot.

%package -n texlive-tkz-fct-doc
Summary:        Documentation for tkz-fct
Version:        svn22831.1.16c

Provides:       tex-tkz-fct-doc
AutoReqProv:    No

%description -n texlive-tkz-fct-doc
Documentation for tkz-fct

%package -n texlive-tkz-graph
Provides:       tex-tkz-graph = %{tl_version}
License:        LPPL
Summary:        Draw graph-theory graphs
Version:        svn22832.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(ifthen.sty), tex(xkeyval.sty), tex(tikz.sty)
Provides:       tex(tkz-graph.sty) = %{tl_version}

%description -n texlive-tkz-graph
The package is designed to create graph diagrams as simply as
possible, using TikZ

%package -n texlive-tkz-graph-doc
Summary:        Documentation for tkz-graph
Version:        svn22832.1.00

Provides:       tex-tkz-graph-doc
AutoReqProv:    No

%description -n texlive-tkz-graph-doc
Documentation for tkz-graph

%package -n texlive-tkz-kiviat
Provides:       tex-tkz-kiviat = %{tl_version}
License:        LPPL
Summary:        Draw Kiviat graphs
Version:        svn22857.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(tikz.sty)
Provides:       tex(tkz-kiviat.sty) = %{tl_version}

%description -n texlive-tkz-kiviat
The package allows the user to draw Kiviat Graphs directly, or
with data from an external file. The drawing is done with the
help of pgfplots.

%package -n texlive-tkz-kiviat-doc
Summary:        Documentation for tkz-kiviat
Version:        svn22857.0.1

Provides:       tex-tkz-kiviat-doc
AutoReqProv:    No

%description -n texlive-tkz-kiviat-doc
Documentation for tkz-kiviat

%package -n texlive-tkz-linknodes
Provides:       tex-tkz-linknodes = %{tl_version}
License:        LPPL
Summary:        Link nodes in mathematical environments
Version:        svn22833.1.0c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(ifthen.sty), tex(xkeyval.sty), tex(tikz.sty)
Requires:       tex(amsmath.sty)
Provides:       tex(tkz-linknodes.sty) = %{tl_version}

%description -n texlive-tkz-linknodes
The package arose from a requirement to link the elements of an
amsmath align or aligned environment. The package makes use of
PGF/TikZ. The package documentation relies on the facilities of
the tkz-doc bundle

%package -n texlive-tkz-linknodes-doc
Summary:        Documentation for tkz-linknodes
Version:        svn22833.1.0c

Provides:       tex-tkz-linknodes-doc
AutoReqProv:    No

%description -n texlive-tkz-linknodes-doc
Documentation for tkz-linknodes

%package -n texlive-tkz-orm
Provides:       tex-tkz-orm = %{tl_version}
License:        GPL+
Summary:        Create Object-Role Model (ORM) diagrams,
Version:        svn39408

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(tkz-orm.sty) = %{tl_version}

%description -n texlive-tkz-orm
The package provides styles for drawing Object-Role Model (ORM)
diagrams in TeX based on the pgf and TikZ picture environment.

%package -n texlive-tkz-orm-doc
Summary:        Documentation for tkz-orm
Version:        svn39408

Provides:       tex-tkz-orm-doc
AutoReqProv:    No

%description -n texlive-tkz-orm-doc
Documentation for tkz-orm

%package -n texlive-tkz-tab
Provides:       tex-tkz-tab = %{tl_version}
License:        LPPL
Summary:        Tables of signs and variations using PGF/TikZ
Version:        svn22834.1.3c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(ifthen.sty), tex(xkeyval.sty), tex(tikz.sty)
Provides:       tex(tkz-tab.sty) = %{tl_version}

%description -n texlive-tkz-tab
The package provides comprehensive facilities for preparing
lists of signs and variations, using PGF. The package
documentation requires the tkz-doc bundle.

%package -n texlive-tkz-tab-doc
Summary:        Documentation for tkz-tab
Version:        svn22834.1.3c

Provides:       tex-tkz-tab-doc
AutoReqProv:    No

%description -n texlive-tkz-tab-doc
Documentation for tkz-tab

%package -n texlive-tsemlines
Provides:       tex-tsemlines = %{tl_version}
License:        Public Domain
Summary:        Support for the ancient \emline macro
Version:        svn23440.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tsemlines.sty) = %{tl_version}

%description -n texlive-tsemlines
Occasional Documents appear, that use graphics generated by
texcad from the emtex distribution. These documents often use
the \emline macro, which produced lines at an arbitrary
orientation. The present package emulates the macro, using
TikZ.

%package -n texlive-tufte-latex
Provides:       tex-tufte-latex = %{tl_version}
License:        ASL 2.0
Summary:        Document classes inspired by the work of Edward Tufte
Version:        svn37649.3.5.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-xifthen, tex-ifmtarg, tex-changepage, tex-paralist
Requires:       tex-sauerj, tex-placeins
Provides:       tex(tufte-book.cls) = %{tl_version}, tex(tufte-common.def) = %{tl_version}
Provides:       tex(tufte-handout.cls) = %{tl_version}

%description -n texlive-tufte-latex
Provided are two classes inspired, respectively, by handouts
and books created by Edward Tufte.

%package -n texlive-tufte-latex-doc
Summary:        Documentation for tufte-latex
Version:        svn37649.3.5.2

Provides:       tex-tufte-latex-doc
AutoReqProv:    No
Requires:       tex-xifthen-doc, tex-ifmtarg-doc, tex-changepage-doc, tex-paralist-doc

Provides:       tex-tufte-latex-doc
AutoReqProv:    No
Requires:       tex-xifthen-doc, tex-ifmtarg-doc, tex-changepage-doc, tex-paralist-doc
Requires:       tex-sauerj-doc, tex-placeins-doc

%description -n texlive-tufte-latex-doc
Documentation for tufte-latex

%package -n texlive-tipfr
Provides:       tex-tipfr = %{tl_version}
License:        LPPL
Summary:        Produces calculator's keys with the help of TikZ
Version:        svn38646

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tipfr.sty) = %{tl_version}

%description -n texlive-tipfr
The package provides commands to draw calculator keys with the
help of TikZ. It also provides commands to draw the content of
screens and of menu items.

%package -n texlive-typed-checklist-doc
Provides:       tex-typed-checklist-doc = %{tl_version}
License:        LPPL
Summary:        doc files of typed-checklist
Version:        svn40389

AutoReqProv:    No

%description -n texlive-typed-checklist-doc
Documentation for typed-checklist

%package -n texlive-typed-checklist
Provides:       tex-typed-checklist = %{tl_version}
License:        LPPL
Summary:        Typesetting tasks, goals, milestones, artifacts, and more in LaTeX
Version:        svn40389

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(typed-checklist.sty) = %{tl_version}

%description -n texlive-typed-checklist
The main goal of this package is to provide means for
typesetting checklists in a way that stipulates users to
explicitly distinguish checklists for goals, for tasks, for
artifacts, and for milestones -- i.e., the type of checklist
entries. The intention behind this is that a user of the
package is coerced to think about what kind of entries he/she
adds to the checklist. This shall yield a clearer result and,
in the long run, help with training to distinguish entries of
different types.

%package -n texlive-typehtml
Provides:       tex-typehtml = %{tl_version}
License:        LPPL
Summary:        Typeset HTML directly from LaTeX
Version:        svn17134.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(exscale.sty)
Provides:       tex(typehtml.sty) = %{tl_version}

%description -n texlive-typehtml
Can handle almost all of HTML2, and most of the math fragment
of the draft HTML3.

%package -n texlive-typehtml-doc
Summary:        Documentation for typehtml
Version:        svn17134.0

Provides:       tex-typehtml-doc
AutoReqProv:    No

%description -n texlive-typehtml-doc
Documentation for typehtml

%package -n texlive-tagpdf
Summary:        Tools for experimenting with tagging using pdfLaTeX and LuaLaTeX
Version:        svn48366
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tagpdf-checks-code.sty) = %{tl_version}
Provides:       tex(tagpdf-luatex.def) = %{tl_version}, tex(tagpdf-mc-code-generic.sty) = %{tl_version}
Provides:       tex(tagpdf-mc-code-lua.sty) = %{tl_version}
Provides:       tex(tagpdf-mc-code-shared.sty) = %{tl_version}
Provides:       tex(tagpdf-pdftex.def) = %{tl_version}, tex(tagpdf-roles-code.sty) = %{tl_version}
Provides:       tex(tagpdf-struct-code.sty) = %{tl_version}
Provides:       tex(tagpdf-tree-code.sty) = %{tl_version}
Provides:       tex(tagpdf-user.sty) = %{tl_version}, tex(tagpdf.lua) = %{tl_version}
Provides:       tex(tagpdf.sty) = %{tl_version}

%description -n texlive-tagpdf
The package offers tools to experiment with tagging and
accessibility using pdfLaTeX and LuaTeX. It isn't meant for
production but allows the user to try out how difficult it is
to tag some structures; to try out how much tagging is really
needed; to test what else is needed so that a pdf works e.g.
with a screen reader. Its goal is to get a feeling for what has
to be done, which kernel changes are needed, how packages
should be adapted.

%package -n texlive-thalie
Provides:       tex-thalie = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset drama plays
Version:        svn44048
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(etoolbox.sty), tex(suffix.sty), tex(longtable.sty)
Requires:       tex(xspace.sty), tex(pgfopts.sty)
Provides:       tex(thalie.sty) = %{tl_version}

%description -n texlive-thalie
The package provides tools to typeset drama plays. It defines
commands to introduce characters' lines, to render stage
directions, to divide a play into acts and scenes and to build
the dramatis personae automatically.

%package -n texlive-thalie-doc
Summary:        Documentation for thalie
Version:        svn44048
Provides:       tex-thalie-doc
AutoReqProv:    No

%description -n texlive-thalie-doc
Documentation for thalie

%package -n texlive-tree-dvips
Provides:       tex-tree-dvips = %{tl_version}
License:        LPPL
Summary:        Trees and other linguists' macros
Version:        svn21751.91

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lingmacros.sty) = %{tl_version}, tex(tree-dvips.sty) = %{tl_version}

%description -n texlive-tree-dvips
The package defines a mechanism for specifying connected trees
that uses a tabular environment to generate node positions. The
package uses PostScript code, loaded by dvips, so output can
only be generated by use of dvips. The package lingmacros.sty
defines a few macros for linguists: \enumsentence for
enumerating sentence examples, simple tabular-based non-
connected tree macros, and gloss macros.

%package -n texlive-tree-dvips-doc
Summary:        Documentation for tree-dvips
Version:        svn21751.91

Provides:       tex-tree-dvips-doc
AutoReqProv:    No

%description -n texlive-tree-dvips-doc
Documentation for tree-dvips

%package -n texlive-thaispec
Summary:        Thai Language Typesetting in XeLaTeX
Version:        svn46923
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(fontspec.sty)
Requires:       tex(ucharclasses.sty), tex(polyglossia.sty)
Requires:       tex(setspace.sty), tex(datetime2.sty), tex(kvoptions.sty), tex(fp.sty)
Requires:       tex(afterpackage.sty), tex(xstring.sty), tex(xpatch.sty)
Provides:       tex(thaispec.sty) = %{tl_version}

%description -n texlive-thaispec
This package allows the user to input Thai characters directly
to a .tex file and choose any Thai fonts to be used in the
document. Required packages are fontspec, ucharclasses,
polyglossia, setspace, datetime2, kvoptions, fp, afterpackage,
xstring, and xpatch.

%package -n texlive-thesis-gwu
Summary:        Thesis class for George Washington University School of Engineering and Applied Science
Version:        svn48324
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(thesis-gwu.cls) = %{tl_version}

%description -n texlive-thesis-gwu
This class is an attempt to create a standard format for GWU
SEAS dissertations/theses. It automatically handles many of the
complicated formatting requirements and includes many useful
packages. An example thesis is provided serving as a user guide
and a demonstration of the thesis.

%package -n texlive-thucoursework
Summary:        Coursework template for Tsinghua University
Version:        svn47781
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(iidef.sty) = %{tl_version}

%description -n texlive-thucoursework
A LaTeX package for students of Tsinghua University to write
coursework more efficiently. It can also be used by students
from other universities. Note that the package itself does not
import the ctex package; to use it with Chinese writing, see
example file ithw.tex for details.

%package -n texlive-tikz-karnaugh
Summary:        Typeset Karnaugh maps using TikZ
Version:        svn47026
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzlibrarykarnaugh.code.tex) = %{tl_version}

%description -n texlive-tikz-karnaugh
The tikz-karnaugh package is a LaTeX package used to draw
Karnaugh maps. It uses TikZ to produce high quality graph up to
12 variables, but this limit depends on the TeX memory usage
and can be different for you. It is very good for presentation
since TikZ allows for a better control over the final
appearance of the map. You can control colour, styles and
distances. It can be considered as an upgrade of Andreas W.
Wieland's karnaugh package towards TikZ supporting. Also,
complex maps with solution (prime implicants) pointed out can
be generated with external java software. It supports both
America and traditional styles, though American style requires
a little extra effort.

%package -n texlive-tikz-ladder
Summary:        Draw ladder diagrams using TikZ
Version:        svn46555
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzlibrarycircuits.plc.ladder.code.tex) = %{tl_version}

%description -n texlive-tikz-ladder
The tikz-ladder package contains a collection of symbols for
typesetting ladder diagrams (PLC program) in agreement with the
international standard IEC-61131-3/2013. It includes blocks
(for representing functions and function blocks) besides
contacts and coils. It extends the circuit library of TikZ and
allows you to draw a ladder diagram in the same way as you
would draw any other circuit.

%package -n texlive-tikz-layers
Summary:        TikZ provides graphical layers on TikZ: "behind", "above" and "glass"
Version:        svn46660
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikz-layers.sty) = %{tl_version}

%description -n texlive-tikz-layers
TikZ-layers is a tiny package that provides, along side
"background", typical graphical layers on TikZ: "behind",
"above" and "glass". The layers may be selected with one of the
styles "on behind layer", "on above layer", "on glass layer" as
an option to a {scope} environment.

%package -n texlive-tikzmarmots
Summary:        Drawing little marmots in TikZ
Version:        svn48177
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzmarmots.sty) = %{tl_version}, tex(tikzlibrarymarmots.code.tex) = %{tl_version}

%description -n texlive-tikzmarmots
This is a LaTeX package for marmots to be used in TikZ
pictures. These little figures are constructed in such a way
that they may even "borrow" some garments and other attributes
from the TikZducks.

%package -n texlive-tikz-nef
Summary:        Create diagrams for neural networks constructed with the methods of the Neural Engineering Framework (NEF)
Version:        svn48240
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzlibrarynef.code.tex) = %{tl_version}

%description -n texlive-tikz-nef
The nef TikZ library provides predefined styles and shapes to
create diagrams for neural networks constructed with the
methods of the Neural Engineering Framework (NEF). The
following styles are supported: ea: ensemble array ens:
ensemble ext: external input or output inhibt: inhibitory
connection net: network pnode: pass-through node rect:
rectification ensemble recurrent: recurrent connection.

%package -n texlive-tikz-network
Summary:        Draw networks with TikZ
Version:        svn48314
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikz-network.sty) = %{tl_version}

%description -n texlive-tikz-network
This package allows the creation of images of complex networks
that are seamlessly integrated into the underlying LaTeX files.

%package -n texlive-tikz-relay
Summary:        TikZ library for typesetting electrical diagrams
Version:        svn48024
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%description -n texlive-tikz-relay
This package contains a collection of symbols for typesetting
electrical wiring diagrams for relay control systems. The
symbols are meant to be in agreement with the international
standard IEC-60617 which has been adopted worldwide, with
perhaps the exception of the USA. It extends and modifies, when
needed, the TikZ-libray circuits.ee.IEC. A few non-standard
symbols are also included mainly to be used in presentations,
particularly with the beamer package.

%package -n texlive-tikz-sfc
Summary:        Symbols collection for typesetting Sequential Function Chart (SFC) diagrams (PLC programs)
Version:        svn46332
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tikzlibrarycircuits.plc.sfc.code.tex) = %{tl_version}

%description -n texlive-tikz-sfc
This package contains a collection of symbols for typesetting
Sequential Function Chart (SFC) diagrams in agreement with the
international standard IEC-61131-3/2013. It includes steps
(normal and initial), transitions, actions and actions
qualifiers (with and without time duration). It extends the
circuit library of TikZ and allows you to draw an SFC diagram
in same way you would draw any other circuit.

%package -n texlive-timbreicmc
Summary:        Typeset documents with ICMC/USP watermarks
Version:        svn46070
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(timbreicmc.sty) = %{tl_version}

%description -n texlive-timbreicmc
With this package you can typeset documents with ICMC/USP Sao
Carlos watermarks. ICMC is acronym for "Instituto de Ciencias
Matematicas e de Computacao" of the "Universidade de Sao Paulo"
(USP), in the city of Sao Carlos-SP, Brazil.

%package -n texlive-tinos
Summary:        Tinos fonts with LaTeX support
Version:        svn42882
License:        ASL 2.0
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tns_27astb.enc) = %{tl_version}, tex(tns_s6t4vy.enc) = %{tl_version}
Provides:       tex(tns_xze2cy.enc) = %{tl_version}, tex(tns_y6kixo.enc) = %{tl_version}
Provides:       tex(tinos.map) = %{tl_version}, tex(Tinos-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Tinos-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tinos-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Tinos-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Tinos-tlf-ly1.tfm) = %{tl_version}, tex(Tinos-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Tinos-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-tlf-t1.tfm) = %{tl_version}, tex(Tinos-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Tinos-tlf-ts1.tfm) = %{tl_version}, tex(Tinos-Bold.ttf) = %{tl_version}
Provides:       tex(Tinos-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Tinos-Italic.ttf) = %{tl_version}, tex(Tinos-Regular.ttf) = %{tl_version}
Provides:       tex(Tinos-Bold.pfb) = %{tl_version}, tex(Tinos-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Tinos-Italic.pfb) = %{tl_version}, tex(Tinos.pfb) = %{tl_version}
Provides:       tex(Tinos-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Tinos-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Tinos-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Tinos-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Tinos-tlf-t1.vf) = %{tl_version}, tex(Tinos-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Tinos-TLF.fd) = %{tl_version}, tex(OT1Tinos-TLF.fd) = %{tl_version}
Provides:       tex(T1Tinos-TLF.fd) = %{tl_version}, tex(TS1Tinos-TLF.fd) = %{tl_version}
Provides:       tex(tinos.sty) = %{tl_version}

%description -n texlive-tinos
Tinos, designed by Steve Matteson, is an innovative, refreshing
serif design that is metrically compatible with Times New
Roman.

%package -n texlive-tlc-article
Summary:        A LaTeX document class for formal documents
Version:        svn47891
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tlc-article.cls) = %{tl_version}

%description -n texlive-tlc-article
The package provides a LaTeX document class that orchestrates a
logical arrangement for document header, footer, author,
abstract, table of contents, and margins. It standardizes a
document layout intended for formal documents. The tlc_article
GitHub repository uses a SCRUM framework adapted to standard
GitHub tooling. tlc_article is integrated with Travis-ci.org
for continuous integration and AllanConsulting.slack.com for
centralized notification.

%package -n texlive-topletter
Summary:        Letter class for the Politecnico di Torino
Version:        svn48182
License:        ASL 2.0
Requires:       texlive-base texlive-kpathsea
Provides:       tex(TOPletter.cls) = %{tl_version}

%description -n texlive-topletter
This package provides a LaTeX class for typesetting letters
conforming to the official Corporate Image guidelines for the
Politecnico di Torino. The class can be used for letters
written in Italian and in English.

%package -n texlive-typewriter
Summary:        Typeset with a randomly variable monospace font
Version:        svn46641
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(typewriter.sty) = %{tl_version}

%description -n texlive-typewriter
The typewriter package uses the OpenType Computer Modern
Unicode Typewriter font, together with a LuaTeX virtual font
setup that introduces random variability in grey level and
angle of each character. It was originally an answer to a
question on stackexchange.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names=""
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-tools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tools/

%files -n texlive-tools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tools/

%files -n texlive-tpslifonts
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/tpslifonts/

%files -n texlive-tpslifonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/tpslifonts/

%files -n texlive-trajan
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/trajan/
%{_texdir}/texmf-dist/fonts/map/dvips/trajan/
%{_texdir}/texmf-dist/fonts/tfm/public/trajan/
%{_texdir}/texmf-dist/fonts/type1/public/trajan/
%{_texdir}/texmf-dist/tex/latex/trajan/

%files -n texlive-trajan-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/trajan/

%files -n texlive-txfontsb
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/txfontsb/
%{_texdir}/texmf-dist/fonts/enc/dvips/txfontsb/
%{_texdir}/texmf-dist/fonts/map/dvips/txfontsb/
%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb/
%{_texdir}/texmf-dist/fonts/type1/public/txfontsb/
%{_texdir}/texmf-dist/fonts/vf/public/txfontsb/
%{_texdir}/texmf-dist/tex/latex/txfontsb/

%files -n texlive-txfontsb-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/txfontsb/

%files -n texlive-typicons
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/truetype/public/typicons/
%{_texdir}/texmf-dist/tex/latex/typicons/

%files -n texlive-typicons-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/typicons/

%files -n texlive-times
%license gpl.txt
%{_texdir}/texmf-dist/dvips/times/
%{_texdir}/texmf-dist/fonts/afm/adobe/times/
%{_texdir}/texmf-dist/fonts/afm/urw/times/
%{_texdir}/texmf-dist/fonts/map/dvips/times/
%{_texdir}/texmf-dist/fonts/tfm/adobe/times/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/times/
%{_texdir}/texmf-dist/fonts/type1/urw/times/
%{_texdir}/texmf-dist/fonts/vf/adobe/times/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/times/
%{_texdir}/texmf-dist/tex/latex/times/

%files -n texlive-tipa
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/tipa/
%{_texdir}/texmf-dist/fonts/source/public/tipa/
%{_texdir}/texmf-dist/fonts/tfm/public/tipa/
%{_texdir}/texmf-dist/fonts/type1/public/tipa/
%{_texdir}/texmf-dist/tex/latex/tipa/

%files -n texlive-tipa-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/tipa/

%files -n texlive-txfonts
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/
%{_texdir}/texmf-dist/fonts/enc/dvips/txfonts/
%{_texdir}/texmf-dist/fonts/map/dvips/txfonts/
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/
%{_texdir}/texmf-dist/tex/latex/txfonts/

%files -n texlive-txfonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/txfonts/

%files -n texlive-tracklang
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/tracklang/
%{_texdir}/texmf-dist/tex/latex/tracklang/

%files -n texlive-tracklang-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/tracklang/

%files -n texlive-thalie
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/thalie/

%files -n texlive-thalie-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/thalie/

%files -n texlive-tree-dvips
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/tree-dvips/
%{_texdir}/texmf-dist/tex/latex/tree-dvips/

%files -n texlive-tree-dvips-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tree-dvips/

%files -n texlive-tram
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/tram/
%{_texdir}/texmf-dist/tex/latex/tram/

%files -n texlive-tram-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tram/

%files -n texlive-titlepages-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/titlepages/

%files -n texlive-tlc2-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tlc2/

%files -n texlive-turkmen
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/turkmen/

%files -n texlive-turkmen-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/turkmen/

%files -n texlive-translation-array-fr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-array-fr/

%files -n texlive-translation-dcolumn-fr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-dcolumn-fr/

%files -n texlive-translation-natbib-fr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-natbib-fr/

%files -n texlive-translation-tabbing-fr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-tabbing-fr/

%files -n texlive-tipa-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tipa-de/

%files -n texlive-translation-arsclassica-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-arsclassica-de/

%files -n texlive-translation-biblatex-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-biblatex-de/

%files -n texlive-translation-chemsym-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-chemsym-de/

%files -n texlive-translation-ecv-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-ecv-de/

%files -n texlive-translation-enumitem-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-enumitem-de/

%files -n texlive-translation-europecv-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-europecv-de/

%files -n texlive-translation-filecontents-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-filecontents-de/

%files -n texlive-translation-moreverb-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/translation-moreverb-de/

%files -n texlive-typehtml
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/typehtml/

%files -n texlive-typehtml-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/typehtml/

%files -n texlive-ticollege
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ticollege/

%files -n texlive-ticollege-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ticollege/

%files -n texlive-tipfr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tipfr/

%files -n texlive-tikz-3dplot
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikz-3dplot/

%files -n texlive-tikz-3dplot-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikz-3dplot/

%files -n texlive-tikz-bayesnet
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikz-bayesnet/

%files -n texlive-tikz-bayesnet-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikz-bayesnet/

%files -n texlive-tikz-cd
%license gpl3.txt
%{_texdir}/texmf-dist/tex/generic/tikz-cd/
%{_texdir}/texmf-dist/tex/latex/tikz-cd/

%files -n texlive-tikz-cd-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/tikz-cd/

%files -n texlive-tikz-dependency
%{_texdir}/texmf-dist/tex/latex/tikz-dependency/

%files -n texlive-tikz-dependency-doc
%{_texdir}/texmf-dist/doc/latex/tikz-dependency/

%files -n texlive-tikz-dimline
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/tikz-dimline/

%files -n texlive-tikz-dimline-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/tikz-dimline/

%files -n texlive-tikz-inet
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tikz-inet/

%files -n texlive-tikz-inet-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tikz-inet/

%files -n texlive-tikz-opm
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikz-opm/

%files -n texlive-tikz-opm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikz-opm/

%files -n texlive-tikz-palattice
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikz-palattice/

%files -n texlive-tikz-palattice-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikz-palattice/

%files -n texlive-tikz-qtree
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/tikz-qtree/

%files -n texlive-tikz-qtree-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/tikz-qtree/

%files -n texlive-tikz-timing
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tikz-timing/

%files -n texlive-tikz-timing-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tikz-timing/

%files -n texlive-tikzinclude
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikzinclude/

%files -n texlive-tikzinclude-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikzinclude/

%files -n texlive-tikzmark
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikzmark/

%files -n texlive-tikzmark-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikzmark/

%files -n texlive-tikzorbital
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tikzorbital/

%files -n texlive-tikzorbital-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tikzorbital/

%files -n texlive-tikzpagenodes
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tikzpagenodes/

%files -n texlive-tikzpagenodes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tikzpagenodes/

%files -n texlive-tikzpfeile
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tikzpfeile/

%files -n texlive-tikzpfeile-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tikzpfeile/

%files -n texlive-tikzposter
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/tikzposter/

%files -n texlive-tikzposter-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/tikzposter/

%files -n texlive-tikzscale
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikzscale/

%files -n texlive-tikzscale-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikzscale/

%files -n texlive-tikzsymbols
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikzsymbols/

%files -n texlive-tikzsymbols-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikzsymbols/

%files -n texlive-timing-diagrams
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/timing-diagrams/

%files -n texlive-timing-diagrams-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/timing-diagrams/

%files -n texlive-tqft
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tqft/

%files -n texlive-tqft-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tqft/

%files -n texlive-tkz-base
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-base/

%files -n texlive-tkz-base-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-base/

%files -n texlive-tkz-berge
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-berge/

%files -n texlive-tkz-berge-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-berge/

%files -n texlive-tkz-doc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-doc/

%files -n texlive-tkz-doc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-doc/

%files -n texlive-tkz-euclide
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-euclide/

%files -n texlive-tkz-euclide-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-euclide/

%files -n texlive-tkz-fct
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-fct/

%files -n texlive-tkz-fct-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-fct/

%files -n texlive-tkz-graph
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-graph/

%files -n texlive-tkz-graph-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-graph/

%files -n texlive-tkz-kiviat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-kiviat/

%files -n texlive-tkz-kiviat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-kiviat/

%files -n texlive-tkz-linknodes
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-linknodes/

%files -n texlive-tkz-linknodes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-linknodes/

%files -n texlive-tkz-orm
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/tkz-orm/

%files -n texlive-tkz-orm-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/tkz-orm/

%files -n texlive-tkz-tab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tkz-tab/

%files -n texlive-tkz-tab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tkz-tab/

%files -n texlive-tsemlines
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/tsemlines/

%files -n texlive-tufte-latex
%license apache2.txt
%{_texdir}/texmf-dist/bibtex/bst/tufte-latex/
%{_texdir}/texmf-dist/tex/latex/tufte-latex/

%files -n texlive-tufte-latex-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/latex/tufte-latex/

%files -n texlive-theoremref
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/theoremref/

%files -n texlive-theoremref-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/theoremref/

%files -n texlive-thinsp
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/thinsp/

%files -n texlive-thinsp-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/thinsp/

%files -n texlive-thmtools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/thmtools/

%files -n texlive-thmtools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/thmtools/

%files -n texlive-threadcol
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/threadcol/

%files -n texlive-threadcol-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/threadcol/

%files -n texlive-threeparttable
%{_texdir}/texmf-dist/tex/latex/threeparttable/

%files -n texlive-threeparttable-doc
%{_texdir}/texmf-dist/doc/latex/threeparttable/

%files -n texlive-threeparttablex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/threeparttablex/

%files -n texlive-threeparttablex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/threeparttablex/

%files -n texlive-thumb
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/thumb/

%files -n texlive-thumb-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/thumb/

%files -n texlive-thumbs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/thumbs/

%files -n texlive-thumbs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/thumbs/

%files -n texlive-thumby
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/thumby/

%files -n texlive-thumby-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/thumby/

%files -n texlive-ticket
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ticket/

%files -n texlive-ticket-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ticket/

%files -n texlive-titlecaps
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/titlecaps/

%files -n texlive-titlecaps-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/titlecaps/

%files -n texlive-titlefoot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/titlefoot/

%files -n texlive-titlepic
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/titlepic/

%files -n texlive-titlepic-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/titlepic/

%files -n texlive-titleref
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/titleref/

%files -n texlive-titleref-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/titleref/

%files -n texlive-titlesec
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/titlesec/

%files -n texlive-titlesec-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/titlesec/

%files -n texlive-titling
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/titling/

%files -n texlive-titling-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/titling/

%files -n texlive-tocbibind
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tocbibind/

%files -n texlive-tocbibind-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tocbibind/

%files -n texlive-tocloft
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tocloft/

%files -n texlive-tocloft-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tocloft/

%files -n texlive-tocvsec2
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tocvsec2/

%files -n texlive-tocvsec2-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tocvsec2/

%files -n texlive-todo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/todo/

%files -n texlive-todo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/todo/

%files -n texlive-todonotes
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/todonotes/

%files -n texlive-todonotes-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/todonotes/

%files -n texlive-tokenizer
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tokenizer/

%files -n texlive-tokenizer-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tokenizer/

%files -n texlive-toolbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/toolbox/

%files -n texlive-toolbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/toolbox/

%files -n texlive-topfloat
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/topfloat/

%files -n texlive-topfloat-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/topfloat/

%files -n texlive-totcount
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/totcount/

%files -n texlive-totcount-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/totcount/

%files -n texlive-totpages
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/totpages/

%files -n texlive-totpages-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/totpages/

%files -n texlive-translations
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/translations/

%files -n texlive-translations-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/translations/

%files -n texlive-trfsigns
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/trfsigns/

%files -n texlive-trfsigns-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/trfsigns/

%files -n texlive-trimspaces
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/trimspaces/

%files -n texlive-trimspaces-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/trimspaces/

%files -n texlive-trivfloat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/trivfloat/

%files -n texlive-trivfloat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/trivfloat/

%files -n texlive-trsym
%license lppl1.2.txt
%{_texdir}/texmf-dist/fonts/source/public/trsym/
%{_texdir}/texmf-dist/fonts/tfm/public/trsym/
%{_texdir}/texmf-dist/tex/latex/trsym/

%files -n texlive-trsym-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/trsym/

%files -n texlive-truncate
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/truncate/

%files -n texlive-truncate-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/truncate/

%files -n texlive-tucv
%{_texdir}/texmf-dist/tex/latex/tucv/

%files -n texlive-tucv-doc
%{_texdir}/texmf-dist/doc/latex/tucv/

%files -n texlive-turnthepage
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/turnthepage/

%files -n texlive-turnthepage-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/turnthepage/

%files -n texlive-twoinone
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/twoinone/

%files -n texlive-twoinone-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/twoinone/

%files -n texlive-twoup
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/twoup/

%files -n texlive-twoup-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/twoup/

%files -n texlive-txgreeks
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/txgreeks/

%files -n texlive-txgreeks-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/txgreeks/

%files -n texlive-type1cm
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/type1cm/

%files -n texlive-type1cm-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/type1cm/

%files -n texlive-typeface
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/typeface/

%files -n texlive-typeface-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/typeface/

%files -n texlive-typogrid
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/typogrid/

%files -n texlive-typogrid-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/typogrid/

%files -n texlive-thmbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/thmbox/

%files -n texlive-thmbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/thmbox/

%files -n texlive-turnstile
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/turnstile/

%files -n texlive-turnstile-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/turnstile/

%files -n texlive-threeddice
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/threeddice/

%files -n texlive-threeddice-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/threeddice/

%files -n texlive-timetable
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/timetable/

%files -n texlive-treetex
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/treetex/

%files -n texlive-treetex-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/treetex/

%files -n texlive-thesis-ekf
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/thesis-ekf/

%files -n texlive-thesis-ekf-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/thesis-ekf/

%files -n texlive-thesis-titlepage-fhac
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/thesis-titlepage-fhac/

%files -n texlive-thesis-titlepage-fhac-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/thesis-titlepage-fhac/

%files -n texlive-thuthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/thuthesis/
%{_texdir}/texmf-dist/tex/latex/thuthesis/

%files -n texlive-thuthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/thuthesis/

%files -n texlive-toptesi
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/toptesi/

%files -n texlive-toptesi-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/toptesi/

%files -n texlive-tudscr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tudscr/

%files -n texlive-tudscr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tudscr/

%files -n texlive-tugboat
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/tugboat/
%{_texdir}/texmf-dist/tex/latex/tugboat/

%files -n texlive-tugboat-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tugboat/

%files -n texlive-tugboat-plain
%{_texdir}/texmf-dist/tex/plain/tugboat-plain/

%files -n texlive-tugboat-plain-doc
%{_texdir}/texmf-dist/doc/plain/tugboat-plain/

%files -n texlive-turabian
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/turabian/

%files -n texlive-turabian-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/turabian/

%files -n texlive-turabian-formatting
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/turabian-formatting/

%files -n texlive-turabian-formatting-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/turabian-formatting/

%files -n texlive-tui
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/tui/

%files -n texlive-tui-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/tui/

%files -n texlive-t-angles
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/t-angles/

%files -n texlive-t-angles-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/t-angles/

%files -n texlive-tikz-feynman-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/tikz-feynman/

%files -n texlive-tikz-feynman
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/tikz-feynman/

%files -n texlive-tipfr
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/tipfr/

%files -n texlive-typed-checklist-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/typed-checklist/

%files -n texlive-typed-checklist
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/typed-checklist/

%files -n texlive-thaienum
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/thaienum/
%{_texdir}/texmf-dist/tex/latex/thaienum/

%files -n texlive-tikzcodeblocks
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/tikzcodeblocks/
%{_texdir}/texmf-dist/tex/latex/tikzcodeblocks/

%files -n texlive-tikzducks
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/tikzducks/
%{_texdir}/texmf-dist/tex/latex/tikzducks/

%files -n texlive-tikz-kalender
%doc %{_texdir}/texmf-dist/doc/latex/tikz-kalender/
%{_texdir}/texmf-dist/tex/latex/tikz-kalender/

%files -n texlive-tikz-optics
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/tikz-optics/
%{_texdir}/texmf-dist/tex/latex/tikz-optics/

%files -n texlive-tikzpeople
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/tikzpeople/
%{_texdir}/texmf-dist/tex/latex/tikzpeople/

%files -n texlive-tocdata
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/tocdata/
%{_texdir}/texmf-dist/tex/latex/tocdata/

%files -n texlive-txuprcal
%license gpl3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/txuprcal/
%{_texdir}/texmf-dist/fonts/map/dvips/txuprcal/
%{_texdir}/texmf-dist/fonts/tfm/public/txuprcal/
%{_texdir}/texmf-dist/fonts/type1/public/txuprcal/
%{_texdir}/texmf-dist/tex/latex/txuprcal/

%files -n texlive-typoaid
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/typoaid/
%{_texdir}/texmf-dist/tex/latex/typoaid/

%files -n texlive-translator
%license lppl1.3.txt 
%license gpl.txt
%doc %{_texdir}/texmf-dist/doc/latex/translator/
%{_texdir}/texmf-dist/tex/latex/translator/

%files -n texlive-tikz-page
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/tikz-page/
%{_texdir}/texmf-dist/tex/latex/tikz-page/

%files -n texlive-trigonometry
%license knuth.txt
%doc %{_texdir}/texmf-dist/doc/generic/trigonometry/
%{_texdir}/texmf-dist/tex/generic/trigonometry/

%files -n texlive-thaispec
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/thaispec/
%doc %{_texdir}/texmf-dist/doc/latex/thaispec/

%files -n texlive-thesis-gwu
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/thesis-gwu/
%doc %{_texdir}/texmf-dist/doc/latex/thesis-gwu/

%files -n texlive-thucoursework
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/thucoursework/
%doc %{_texdir}/texmf-dist/doc/latex/thucoursework/

%files -n texlive-tikz-karnaugh
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/tikz-karnaugh/
%doc %{_texdir}/texmf-dist/doc/latex/tikz-karnaugh/

%files -n texlive-tikz-ladder
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/tikz-ladder/
%doc %{_texdir}/texmf-dist/doc/latex/tikz-ladder/

%files -n texlive-tikz-layers
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/tikz-layers/
%doc %{_texdir}/texmf-dist/doc/latex/tikz-layers/

%files -n texlive-tikzmarmots
%license lppl.txt 
%{_texdir}/texmf-dist/tex/latex/tikzmarmots/
%doc %{_texdir}/texmf-dist/doc/latex/tikzmarmots/

%files -n texlive-tikz-nef
%{_texdir}/texmf-dist/tex/latex/tikz-nef/
%doc %{_texdir}/texmf-dist/doc/latex/tikz-nef/

%files -n texlive-tikz-network
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/tikz-network/
%doc %{_texdir}/texmf-dist/doc/latex/tikz-network/

%files -n texlive-tikz-relay
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/tikz-relay/

%files -n texlive-tikz-sfc
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/tikz-sfc/
%doc %{_texdir}/texmf-dist/doc/latex/tikz-sfc/

%files -n texlive-timbreicmc
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/timbreicmc/
%doc %{_texdir}/texmf-dist/doc/latex/timbreicmc/

%files -n texlive-tinos
%license apache2.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/tinos/
%{_texdir}/texmf-dist/fonts/map/dvips/tinos/
%{_texdir}/texmf-dist/fonts/tfm/google/tinos/
%{_texdir}/texmf-dist/fonts/truetype/google/tinos/
%{_texdir}/texmf-dist/fonts/type1/google/tinos/
%{_texdir}/texmf-dist/fonts/vf/google/tinos/
%{_texdir}/texmf-dist/tex/latex/tinos/
%doc %{_texdir}/texmf-dist/doc/fonts/tinos/

%files -n texlive-tlc-article
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/tlc-article/
%doc %{_texdir}/texmf-dist/doc/latex/tlc-article/

%files -n texlive-topletter
%license apache2.txt
%{_texdir}/texmf-dist/tex/latex/topletter/
%doc %{_texdir}/texmf-dist/doc/latex/topletter/

%files -n texlive-typewriter
%license lppl.txt
%{_texdir}/texmf-dist/tex/lualatex/typewriter/
%doc %{_texdir}/texmf-dist/doc/lualatex/typewriter/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
