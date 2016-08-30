% Syntax
% Cadel Watson
% 1/8/2016

# Alignment

Ngujari has three alignment cases: ergative, nominative, and accusative. The use
of these cases and their corresponding suffixes allows for a more free word
order. Rather than the placement of words determining the role of nouns in a
sentence, the cases take on the role.

In a typical sentence, a noun can take on one of three roles:

- The **agent** of a transitive verb, which is a noun performing an action on
  another noun. In the sentence "The dog saw the cat", the dog is the agent.
- The **object** of a transitive verb, or the noun that an action is being
  performed on. The cat is the object of the above sentence.
- The **subject** of an intransitive verb, which is a verb that only requires
  one verb. For example, in the sentence "The dog barks", the dog is the
  subject.

The case assigned to each of these roles depends on the **morphosyntactic
alignment**, which is a set of rules for determining each case. Ngujari is a
**split ergative** language, meaning that the alignment changes depending on the
nouns in use.

For clauses whose agent and object (or subject) are animate pronouns, the
alignment is **nominative-accusative**. In this alignment, the agent and subject
are assigned the nominative case and the object takes the accusative case. The following example shows what this looks like in practice.

(@) j-i wa-j nna-l miij-awu-ø,
    love.aux-pres 1s-nom 3s-acc love-an-1st,
    I love her.

All other clauses have an **ergative-nominative** alignment, which means that
the object and subject are marked as nominative and the agent is marked as
ergative. The sentence above can be rewritten without using the third-person
pronoun, and will therefore be placed in the ergative-nominative alignment.

(@) j-i wa-ø majuu-j miij-awu-ø,
    love.aux-pres 1s-erg kangaroo-nom love-an-2nd,
    I love the kangaroo.

# Clauses

A clause is simply the most basic unit of a sentence. The only requirements are
the presence of a verb.

## Verb Phrases

(*)Verb Phrase: vp = aux [neg] np(s) [adv(s)] [val] v

A **verb phrase** is the primary structure of the clause. The most basic clause
possible is an avalent^[An avalent verb is one that takes no nouns or
arguments.] verb. This is demonstrated in the following example:

(@) nn-uu rrunn-aa,
    rain.aux-pres rain-inan-1st,
    It's raining.

In practice, most verb phrases will involve nouns. While word order is flexible,
as can be seen in the pragmatics chapter, there are three rules which generally
apply:

1.  The verb's auxiliary appears at the beginning.
2.  The verb itself appears at the end.
3.  [Valence modifiers](morphology.html#valence-modification) appear immediately
    before the verb.

Nouns are free to take most positions in the clause. The following examples illustrate basic verb phrases.

(@) wann-uma maaju-maaju-j ka jinn-u-m,
    see.aux-pst kangaroo-pl-nom 2.val.1 eat-an-3rd,
    The kangaroos ate/were eating.

(@) k-i wa-j kurru-l ji wurr-u-ø,
    strike.aux-pres 1s-nom 2s-acc 0.val.2 electrically.storm-an-1st,
    I strike you.

To demonstrate the flexibility of word order, which is helped by the use of case
markings, the previous example can be rewritten in two other ways.

(@) kurru-l wa-j k-i ji wurr-u-ø,
    2s-acc 1s-nom strike.aux-pres 0.val.2 electrically.storm-an-1st,
    I strike you.

(@) wa-j kurru-l k-i ji wurr-u-ø,
    1s-nom 2s-acc  strike.aux-pres 0.val.2 electrically.storm-an-1st,
    I strike you.

For the most part, nouns will be placed between the verb and its auxiliary. This
order makes it easier to create more complex sentences.

## Noun Phrases

(*)Noun Phrase: np = [adj(s)-attr] n

A verb phrase is able to take more than bare nouns. A **noun phrase** acts like
a noun, but is modified by any number of adjectives and relative clauses.
Relative clauses always come at the end of the noun phrase, but adjectives come
both before and after the noun, depending on the [adjective
order](#modifier-positioning) rules, as seen below.

(@) birru-ø birruku miinna,
    sea-erg blue big,
    vast blue sea

(@) kanaama yirlirna-j gu,
    woven basket-nom small,
    small woven basket

## Relative Clauses

(*)Relative Clause: rc = [aux] [neg] v [val] [adv(s)] np(s)

A relative clause is a clause which modifies a noun (the **head noun**). Ngujari
uses **adjoined** relative clauses, which means that the relative clause is
simply appended to the end of the verb. However, it must first be placed into a
slightly different form than a standard clause.

There are two cases for a relative clause:

- **object clauses**, in which the head noun is the object of the relative
  clause.
- **agent clause**, where the head noun is the relative clause's agent or
  subject.

In both types of relative clause, the verb is moved from the end of the clause to a position immediately following the verb's auxiliary.

In an object clause, the valency of the verb is reduced by one. In effect, the
head noun becomes a noun in the clause.

(@) wiingu-ø k-a pirr-u-ø ka wa-j,
    man-erg aux-pst see-an-1st 2.val.1 1s-nom,
    the man that I saw

In an agent clause, the valency is not modified. Instead, a pronoun that matches
the person, plurality, and animacy of the head noun is added to the relative
clause.

(@) j-a Wuurna-ø nn-uuki-ti yann-u-mi nna-j jurlu-l wa-j ka naj-u-m,
    say.aux-pst Wuurna-erg aux-fut-dub catch-an-3rd 3s-nom turtle-acc 1s-nom 3.val.2 say-an-3rd,
    Wuurna, who might catch a turtle, spoke to me.

# Modifier Positioning

## Adjectives

TODO

## Adverbs

Adverbs can be split into two categories:

- Temporal adverbs specify the time a verb takes place
- Manner adverbs detail the manner in which the verb was conducted

Temporal adverbs usually follow the base verb.

(@) k-a jana-ø jari-rn wiirr-uu-ø yuurli-rna ma,
    go.aux-pst 1s.ch-erg beach-loc go-ch-1st day-rev one,
    Yesterday, I [a child] went to the beach.

Manner adverbs usually precede the base verb.

(@) nn-uuki-yii waya-ø pirwa-pirwa-j garrna gann-u-ø,
    pickup.aux-fut-wimp 1pl-erg clothing-pl-nom quickly pickup-an-1st,
    We should pick up the clothes quickly.

However, both can occupy different positions inside the verb phrase if the
speaker desires it.

# Predicates

A **predicate** is a sentence which modifies a noun. There are three types:

- **Adjectival**, in which a noun is modified by an adjective, such as "The
  grass is green".
- **Nominal**, where the noun is modified by another noun. This is commonly used
  for professions, as in "She is a teacher".
- **Locational**, which assigns a location to a noun, such as "The campsite is
  in the valley".

The Ngujari language distinguishes between these types and forms each in a different way.

## Adjectival

(*)Adjectival Predicate: apred = n [adj(s)-pred/n-com]

An adjectival predicate is formed without the use of a verb, and simply requires
a noun and at least one adjective. The noun is first given the same case as if
it were a subject^[The subject is the only argument to an intransitive verb.].
Any adjectives are changed to their predicate form (see
[morphology](morphology.html#adjectives-and-adverbs)). The adjectives then
simply follow the noun.

(@) puurna-j birruku-ku,
    sky-nom blue-an,
    The sky is blue.

There is another form of adjectival predicate, in which a noun is used in place
of an adjective. While this may seem counter-intuitive, the noun in effect
becomes an adjective. This form is used when describing a changeable state. The
described noun is treated as above, but the modifying noun is given the
comitative case.

(@) murta-j gurlu-yi,
    berry-nom freshness-com,
    The berry is fresh.

## Nominal

(*)Nominal Predicate: npred = be.aux n-subj n-obj be

A nominal predicate is formed using `ngurr`, the verb for "to be". By default,
`ngurr` has a valence of two, taking an agent and an object. The described noun
is the agent and the modifying noun is the object.

(@) ngarr-i wa-ø gajangu-j ngurr-u-ø,
    be.aux-pres 1s-erg teacher be-an-1st,
    I am a teacher.

## Locational

(*)Locational Predicate: lpred = be.aux n-subj n-loc be

A locational predicate is formed in almost the same way as a nominal predicate.
The only difference is that the modifying location is given the locative case,
rather than the comitative.

(@) k-i wurlki-ø kirujunga-ø ngurr-a-m,
    be.aux-pres village-erg somewhere-loc be-inan-3rd,
    The village is somewhere.

# Possession

## Alienable

To indicate alienable possession (possession that is not permanent or subject to
change), the locative case is used in conjunction with the verb `ngurr`. The
possessed noun appears in the locative case as the subject of the transitive
form of `ngurr`, with the possessor appearing as the object in the usual case.

(@) ngarr-i mulu-mulu-ka-rn mungu-j ngurr-a-m,
    be.aux-pres deadfish-pl-dual-loc woman-nom be-inan-3rd,
    The woman has two dead fish.

## Inalienable

Inalienable possession (possession that is unequivocal) is indicated simply
through the use of the verb `gurr`.

(@) garr-aa-nga ngungu-j jarta-l ka gurr-u-ø,
    have.aux-fut-gno mob-nom homeland-acc 3.val.2 have-an-1st,
    Our mob will always have a homeland.

## Pronominal

A noun phrase can be indicated as possessed through the use of a possessive
pronoun as an adjective.

(@) nn-uma nnaa-ø waju-j yurni nna-lu giinn-u-m,
    admire.aux-pst 3pl.an-erg face-nom beautiful 3s.an-pos admire-an-3rd,
    They admired his beautiful face.

In Ngujari culture, an object can be owned by a mob as a whole. Only inanimate
objects may be possessed by a mob (with the exception of areas of land).
Possession is indicated by the particle `tuu`, which appears before the noun. To
specify the possessing mob, the mob's name is placed immediately after the
particle. The regular name is used by members of the possessing mob, but the
honorific name is used for possessions of others. For example, the particle for
something owned by the Wujanga mob would be *tuu-Wujanga* for a member or
*tuu-Wujarra* for an outsider.

(@) nn-i-ju waya-ø tuu-Gurnu jaku nnalu-j muu-ma naa tinn-u-ø,
    protect.aux-strimp 1pl-erg pos-gurnu precious land-nom spirit-inst 2.val.3 protect-an-1st,
    We must protect our [the Gurnu mob's] precious land with vigour.

# Interrogative

## Polar Questions

Polar questions are syntactically the same as a factual statement,
except they are expressed with a rising tone at the beginning of the
question.

(@) nn-uuki kupa-kupa-ø gaypa-gaypa-rn narnn-u-m?,
    fly.aux-fut bird-pl-erg mountain-pl-loc fly-an-3rd,
    Will the birds fly to the mountains?

## Non-Polar Questions

One way of forming a non-polar question is using an interrogative
pronoun as a verb's argument, with no syntactic change taking place.

(@) kiru ngarr-i wumpa-j j-i palyaj-a-m nnu-ø wurlki-j ngurr-a-m,
    where be.aux-prs path-nom leadto.aux-prs leadto-inan-3rd 3s.inan-erg village-nom be-inan-3rd,
    Where is the path that leads to the village?

To question a certain word in a statement, the particle `yuu` can be
placed before the word.

(@) k-aa yuu-nnara-ø nurtwu-j panwa-rnu mirr-uu-m,
    bring.aux-fut int-3dual.an-erg food-nom fire-ori bring-ch-3rd,
    Will those two children bring the food to the fire?

(@) nn-i wa-ø yuu-gurlurni parnti-j jinn-u-mi,
    eat.aux-pres 3s-erg int-fresh kangaroomeat-nom eat-an-3rd,
    Is he eating fresh kangaroo meat?

# Comparative

Ngujari contains locational-type comparatives. This means that the *standard*
noun, or the noun to be judged against, is marked in the revertive case.
Comparatives do not use a verb, and are always positive (i.e. more adjective
than the standard). The adjective is in the predicative inflection.

(@) nna-j wa-rna yam-u,
    3s-nom 1s-rev tall-an,
    He is taller than me.

For comparatives in relative clauses, the adjective is fronted and is followed
by the arguments.

(@) k-a nnalji-ø junn-u nna-ø wiinguurki-rna yuki-j ka giirr-u-m,
    win.aux-pst dingo-erg fast-an 3s-erg boy-rev race-nom 2.val.1 win-an-3rd,
    The dingo, who is faster than the boy, won the race.

# Conditional

There are two types of conditionals: implicative and predictive. The protasis
(condition) and apodosis (outcome) are modified in different ways.

implicative

:   The conditional is a universal truth. Whenever the condition is
    true, the outcome is also true.

predictive

:   The conditional is a prediction. If the condition occurs, the
    outcome will occur.

To form both conditionals, the condition verb phrase appears first, followed
immediately by the outcome verb phrase. There is no morpheme with equivalent
meaning to "if". However, the outcome is always placed in the subjunctive mood
and the present tense.

In an implicative conditional, the condition is given the gnomic mood. The
statement must therefore follow the usual rules of the gnomic, in that it must
state an undisputable truth. The condition is always in the present tense.

(@) k-i-nga kunii-ø mu-rn naa yarr-uu-n j-i-tirlu kunii-j ka mulj-awuu-n,
    fall.aux-prs-gno 2dual.ch-erg water-loc 1.val.2 fall-ch-2nd wet.aux-prs-sbjv 2dual-ch-nom 2.val.1 wet-ch-2nd,
    If you two fall in the water, you will both get wet.

In a predictive conditional, the condition is usually not given a mood. However,
if the phrase is counterfactual, in that the condition is not seen as likely,
the condition occurs in the dubitative mood. Usually, the condition will be in
the future tense.

(@) nn-uuki palwuuwa-j ka girnn-aa-mi k-i yannu-ø nna-j ji wurr-a-rn,
    break.aux-fut branch-nom 2.val.1 break-inan-3rd strike.aux-pres dem.sg.inan-erg 3s-an-nom 0.val.2 strike-inan-3rd,
    If that branch breaks, it will strike him.

(@) k-aa-tila nna-ø maaju-j yirn parr-u-m ngarr-tiru nurtwa-nurtwa-rn yuni waya-j ngurr-a-m,
    hunt.aux-fut-dub 3s.an-erg kangaroo-nom completedly hunt-an-3rd be.aux-subj food-pl-loc lots 1pl-nom be-inan-3rd,
    If he were to successfully hunt the kangaroo [unlikely], we would have lots of food.

# Negative

There are two types of negation: clausal, where the entire clause is negated,
and constituent, where one noun is negated.

The formation of the clausal negative requires the negative particle that
corresponds to the class of the clause's verb. In a standard negative clause,
the particle follows the verb's auxiliary. However, in imperative clauses it
precedes the auxiliary. Qualifiers such as "never" are used following the
sentence, as stand-alone utterances.

(@) k-a tu nna-ø naarla wiirr-u-m,
    go.aux-pst neg 3s.an-erg there go-an-3rd,
    He didn't go there.

(@) ti j-i-yuu ku-j waa yanj-awu-n. wulnni,
    neg steal.aux-strimp 2s-nom 3.val.1 steal-an-2nd never,
    You must never steal.

The consituent negative is applicable to clauses using `gurr`. It is formed
using the special argument *tunna* in the comitative slot of the verb.

(@) rr-i gunnari-ø guwa-guwa-j tunna gurr-a-m,
    have.aux-prs tree-erg leaf-pl-nom none have-inan-3rd,
    The tree doesn't have any leaves.

# Reflexive/Reciprocal

In reflexive clauses, the personal pronoun of the subject simply occupies the
object position in the usual case. However, the valence of the verb must be
decreased by one.

(@) k-i Paya-ø nna-j ka tiirr-u-m,
    carefor.aux-prs paya-erg 3s.an-nom 2.val.1 carefor-an-3rd,
    Paya cares for himself.

If the clause is reciprocal, which applies only to plural subjects, the personal
pronoun is still used except it takes the comitative case. The valence is also
still decreased by one.

(@) k-arlu kuu-j kuu-yi ka pirr-u-n,
    see.aux-rem 2pl-nom 2pl-com 2.val.1 see-an-2nd,
    You [plural] used to see each other.

# Gerunds

The gerund of a verb serves two purposes. It can act in a way similar to the
English gerund, where the verb is used as a noun, or in a way similar to an
infinitive, meaning roughly "in order to".

The gerund is formed through nominalising the verb. The last vowel of the verb
is simply appended as a suffix.

When used in the nominal form, the gerund takes the appropriate noun case.

(@) k-arlu wa-j junnu yuurr-u-ø,
    like.aux-rem 1s-nom swim.ger like-an-1st,
    I used to like swimming.

In the infinitive form, the gerund is placed before the verb's auxiliary.

(@) parra k-a nni-j naarla wiirr-u-m,
    hunt.ger go.aux-pst 3s.an-nom there go-an-3rd,
    He went there to hunt.

# Causatives

There are two forms of the causative. The first occurs when a single noun is
responsible for causing a verb phrase to occur. In this case, the comitative
causative is used. However, if an entire verb phrase is responsible, the
subjunctive purposive is used.

## Comitative Causative

In the comitative causative, an extra argument is added to the verb phrase
without modifying the valence. The argument is the causer, and takes the former
subject's form (be it nominative or ergative). The causee, or the argument which
was formerly the subject, then takes the comitative case instead. The verb
remains in agreement with the former subject.

(@) j-a turrayi-j mu nnij-a-m,
    capsize.aux-pst canoe-nom capsize-inan-3rd,
    The canoe capsized.

(@) j-a turrayi-yi nna-j mu nnij-a-m,
    capsize.aux-pst canoe-com 3s.an-nom capsize-inan-3rd,
    He caused the canoe to capsize.

(@) k-a wa-ø wuta-j walu gukarr-u-ø,
    drop.aux-pst 1s-erg axe-nom my drop-an-1st,
    I dropped my axe.

(@) k-a wa-yi wuta-j walu gaju-ø gukarr-u-ø,
    drop.aux-pst 1s-com axe-nom my wind-erg drop-an-1st,
    The wind caused me to drop my axe.

## Subjunctive Purposive

The subjunctive purposive is formed through the use of the verb `nnurr`. The
auxiliary, *nnarr* takes the present tense, and begins the sentence. The verb
itself is not required, but it still takes two verb phrases as arguments. The
verb phrase causing the other assumes its usual tense and mood, but the caused
action becomes present and subjunctive.

(@) nnarr-i k-a nna-ø naarla wiirr-u-m j-i-tirlu wa-j nna-l nnurr-u-ø,
    effect.aux-prs go.aux-pst 3s.an-erg there go-an-3rd follow.aux-prs-sbjv 1s-nom 3s-an-acc follow-an-1st,
    He went there, so I followed him.

# Subjunctive

## Desires

To express desires, a "wanting" verb is used, such as `mann`, along with a verb
phrase in the subjunctive expressing the desired action. The action can be in
any tense.

(@) nn-i wa-j j-a-tirlu ti nna-j ngarj-awu-m mann-u-ø,
    wish.aux-prs 1s-nom hurt.aux-pst-sbjv neg 3s.an-nom hurt-an-3rd wish-an-1st,
    I wish that he hadn't hurt himself.

## Speculation

If the speaker is speaking hypothetically about a situation, the subjunctive can
be used. In this case, the verb `ngurr` would be used with a predicate adjective
rather than the verbless construction.

(@) ngarr-aa-tilu parra-ø kurlu-j tuwilwa-wa ka ngurr-a-m,
    be.aux-fut-sbjv hunt-erg thing-NOM dangerous-in 2.val.1 be-inan-3rd,
    The [prospective] hunt would be very dangerous.