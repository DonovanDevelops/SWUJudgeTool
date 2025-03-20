# Star Wars Unlimited Resources

## Table of Contents
* [Rules clarifications from Ryan Serrano, SWU Rules Admiral](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#rules-clarifications-from-ryan-serrano-swu-rules-admiral)
* [Rules clarifications from the dev team collected from social media](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#rules-clarifications-from-the-dev-team-collected-from-social-media)
  * [Set 4](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#set-4---jump-to-lightspeed)
  * [Set 3](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#set-3---twilight-of-the-republic)  
  * [Set 2](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#set-2---shadows-of-the-galaxy)
  * [Set 1](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#set-1---spark-of-rebellion)  
* [Rules clarifications from FFG via Jonah](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#rules-clarifications-from-ffg-via-jonah-nexus-manager)
* [Official Card Text Errata](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#official-card-text-errata)
* [Official Card Specific Rulings Compiled List from starwarsunlimited.com](https://nexus.cascadegames.com/resources/card_specific_rulings/)
* [Unofficial rules explainers](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#unofficial-rules-explainers)
* [Links to official resources](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#official-resources)
* [Commonly asked questions](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#commonly-asked-questions)
* [Fan made resources, communities, and tools](https://gist.github.com/macfergusson/256a534a98fc1d45f2595503f7d54953#other-useful-resourcescommunity-tools)

## Rules clarifications from Ryan Serrano, SWU Rules Admiral:

This section covers questions asked via the Nexus judge program with answers directly quoted from Ryan Serrano.

-------------------------------------------------

**Question:**

**What is the eligibility criteria of a Pilot attached as an upgrade determined by?**

*7.5.17A “Piloting” is a keyword whose effect is the same as the constant ability: “You may play this unit as an upgrade on a friendly VEHICLE unit without a PILOT upgrade on it by paying cost Y instead of its printed cost,” where Y is the cost in brackets following “Piloting.” Paying this cost follows all normal rules for paying costs, including accounting for any aspect penalties that modify this cost.*

*2.12.3 Units with the PILOT trait can be in play either as a unit or as an upgrade.*

We have two clarifications of intent:
- Survivors Gauntlet can not move a Pilot to a non-Vehicle.
- Survivors Gauntlet can move a Pilot to a Vehicle that already has a Pilot.

Both the attachment to a Vehicle unit, and the limit of no pre-existing Pilot, come from the same text in the Piloting keyword that only references playing the upgrade, not what it's ongoing attachment eligibility should be.

We also have leaders with the Pilot trait and no Piloting keyword (Boba Fett, for example), as well as units like Sidon Ithano with the Pilot trait and no Piloting keyword, so their eligibility criteria for valid attachment can't be based on the keyword text.

It seems that the limit of 1 Pilot attachment was meant to be able to be bypassed in certain cases, while the limit of Vehicle attachment was not, so should it be baked in to the definition of the Pilot trait? 

In other words, should 2.12.3 have been written as:
*2.12.3 Units with the PILOT trait can be in play either as a unit or as an upgrade **attached to a Vehicle unit.***


**Answer:**

CR5 will contain a small rework of upgrades to create a more robust picture of "attachment restrictions", rather than the current somewhat unwieldy "play restrictions" version.

Changes in CR5:

* All upgrades have implicit attachment restrictions. When playing an upgrade or attaching it to an "eligible" unit, you have to consider those restrictions.
* If an upgrade has no printed attachment restriction, the implicit restriction is "Attach to a unit."
* If an upgrade has a printed attachment restriction, use that.
* If a non-upgrade card is attached as an upgrade by an ability, the attachment restriction is created by the ability that turns that card into an upgrade. It persists while the card remains an upgrade in play.

Since this is too large of a change for CR4, the plan is to hotfix the issue by adding the following entry to a CR4 update:

CR4 Update (3.6.3B):

* **When an ability attaches a unit or leader to another unit as an upgrade (for example, the PILOTING keyword), any restriction from that ability continues to apply to that card until it leaves play. For a unit to be considered “eligible” for that upgrade, the upgrade must have been able to attach to that unit via the original ability.**

3.6.3B will be posted on websites and social media while the CR is updated behind the scenes, hopefully by next week. Judges should apply this rule when judging immediately.

* "One Pilot per vehicle" is a restriction.
* Phantom II's attachment to The Ghost is also a restriction.
* Both apply if you attempt to move the upgrade to a new unit.

`(Answer shared on 2025-03-06)`

`Editorial note: this supercedes previous clarifications related to Survivors' Gauntlet interacting with Phantom II and Pilots. They have been removed from this page.`

-------------------------------------------------  

**Question:**

**With the changes to smuggle explicitly stating that it is always a modified action, how does this impact nested triggers and especially Hondo Leader?**

**Answer:**

Nested Trigger Scenarios with Hondo

Scenario #1

Board state: Hondo leader
* I take a modified Play a Card action to Smuggle Weequay Pirate Gang from my resource row (Hondo and Ambush trigger).
 * I resolve Hondo/Ambush in either order.

Scenario #2

Board state: Hondo leader
* I take a modified Play a Card action to Smuggle Timely Intervention from my resource row (Hondo triggers).
 * TI tells me to take a modified Play a Card action. I play Lieutenant Childsen from hand (Ambush and Childsen's WP trigger).
 * I resolve the WP/Ambush in either order.
* I resolve Hondo.

Explanation:

In the first example, both WPG’s Ambush and Hondo’s ability are "abilities triggered during or as a result of" the modified action that is Smuggling WPG. They are resolved in the same window (once the steps of the action are finished).

In the second example, Hondo is triggered as a result of playing TI and resolves after you’re finished resolving TI’s event ability. That event ability is taking another action, though, and that modified action triggers other abilities that need to resolve before you can go back and resolve Hondo.

`(Answer shared on 2025-03-06)`

-------------------------------------------------

**Question:**

**Can A New Adventure on a pilot unit play the pilot as an upgrade?**

If A New Adventure is played on a pilot unit in play, it is returned to hand, and then can be played again for free. Can the pilot be played for free as an upgrade, or is the "play it for free" on ANA referring to the unit mode only?


**Answer:**

No, you can't pick up a pilot unit and play it as an upgrade. "Unit" applies to the entire ability, the same as "search for a unit and play it".

`(Answer shared on 2025-02-18)`

-------------------------------------------------

**Question:**

**Does Red Leader discount for any friendly upgrade or only friendly PILOT upgrades?**

Red Leader probably should be read as "each friendly PILOT (unit and upgrade)" however the language templating is very different on Padawan Starfighter.


**Answer:**

Red Leader discounts for each Pilot unit and Pilot upgrade.

`(Answer shared on 2025-02-18)`

-------------------------------------------------

**Question:**

**Does sentinel granted by a triggered ability and then removed also turn off the triggered ability?**


8.15.1 states that an ability giving the lost keyword is also lost for the duration of the lose effect. So if it is a conditional constant ability that is "on", it stops giving sentinel until the end of the phase, regardless of whether you turn it "off" then back "on". Such as with Gamorrean Guards vs SpecForce Soldier. Calculating Magnaguard can give sentinel more than once due to it having multiple trigger conditions for the triggered ability. If the sentinel granted by the When Played ability is removed by SpecForce Soldier, can the triggered ability still grant Sentinel again in that phase? Specific scenario: Player A controls a Battle Droid token and plays Calculating MagnaGuard, resolving its triggered ability to gain Sentinel. Player B plays SpecForce Soldier, resolving it's when played ability and removing Sentinel from Calculating MagnaGuard. Player A attacks the SpecForce Soldier with the Battle Droid, causing Calculating MagnaGuard to trigger to give itself Sentinel. As the new lasting effect originates from the same ability source, does the lose effect from SpecForce Soldier stop the Sentinel?


**Answer:**

We are changing how "lose" works in CR4 to simplify complex interactions like this. More info coming soon!

`(Answer shared on 2025-02-18)`

-------------------------------------------------

**Question:**

**What timing needs to be considered in 6.2.3.A Determine Costs?**

When calculating a card’s modified cost, start with the card’s printed cost, then apply any modifiers that increase the cost of the card (including the aspect penalty) before any modifiers that decrease the cost of the card, including abilities like Exploit. The result is the card’s modified cost. Example: Player A has a JTL Krennic unit in play. Player A plays a Battle Droid Legion, exploiting the Krennic unit. The Battle Droid Legion is the first unit played this round by player A. Does it cost 7 or 6, assuming no aspect penalty? Since Krennic is in play for determining costs, does his constant ability apply the discount, or does Exploit defeating Krennic mean his discount can't be applied?


**Answer:**

You can apply discounts in any order you want, so you can apply Krennic's -1 discount and then exploit him for an additional -2.

`(Answer shared on 2025-02-18)`

`Editorial note: this is expected to be clarified in CR5.`

-------------------------------------------------

**Question:**

**Does “Starting Hand” also mean “Opening Hand” or does it mean “First opening hand”?**

The CR references a player’s opening hand, but the base Colossus refers to Starting Hand.


**Answer:**

"Starting hand" is the same as "opening hand"; this is a templating inconsistency. If your base is Colossus, you draw one fewer card, even when you mulligan.

`(Answer shared on 2025-02-18)`

-------------------------------------------------

**Question:**

**How does Piloting and Last Known Information interact?**

Player A has Gar Saxon leader that is currently in play as a leader unit. A Pilot unit (let's say JTL Bossk, Hunt By Instinct) is played via piloting, and is attached to a TIE/LN Fighter. The TIE unit is defeated, sending the TIE and the attached upgrade that is Bossk to the discard. We now have a Pilot unit in the discard that was defeated in this phase, but it was an upgrade at the time of defeat. Is the pilot eligible to return to hand via Gar's leader ability? Is the pilot eligible to return to hand via The Emperor's Legion? Is the pilot eligible to be used by Spark of Hope to be converted in to a resource?


**Answer:**

Gar: Yes, Gar's ability only looks for whether a card was an upgrade attached to a unit, using last known information.

Emperor's Legion & Spark of Hope: Any card ability that cares about whether a certain card in your discard pile was defeated this phase cares about whether it was defeated as that type of card. (See the current Card Clarification for Spark of Hope that it does not work if a unit was defeated while a resource, e.g. by Han's leader ability.)

`(Answer shared on 2025-02-18)`

-------------------------------------------------

**Question:**

**Is it the potential for multiple actions or the actual existence of multiple actions that requires the sequential resolution and thus nesting of triggered abilities in 7.1.7?**

*7.1.7. If an ability instructs a player to take multiple actions (e.g. “Play three cards,” “Attack with two units”), that player performs each action sequentially. Any abilities triggered during or as a result of each action are considered nested abilities, and must be resolved before proceeding to the next action.*

If only a single unit is played by a U-Wing Reinforcements, are those When Played triggered abilities nested? 

Fleshing out the example: 

Say the single unit played by U-Wing Reinforcements is The Ghost, Specter Home Base, while the opponent has a Krayt Dragon in play. As a result, we will have 4 “When Played” pending abilities to resolve:

7 damage from Krayt, 6 damage from Krayt, Shielded from Ghost, and Shield another Spectre unit from Ghost. If we assume Active Player always resolves first, does this go

Shielded from Ghost and Shield another Spectre unit from Ghost in either order, and then 7 damage from Krayt and 6 damage from Krayt in either order.

OR

Shielded from Ghost and Shield another Spectre unit from Ghost in either order, and then 6 damage from Krayt, and then 7 damage from Krayt.

Another example:

If you have a Bossk, Deadly Stalker in play and play U-Wing Reinforcements, choosing to play only one unit from this ability, can Bossk's event trigger resolve prior to anything from the single unit played by U-Wing?


**Answer:**

This is a great thing to poke at, and we appreciate the attention to detail here and in your other questions! Having talked about some of the implications of the various answers to this question, we are going to move forward by separating the "nested" rule from the "sequential" rule in CR4. With some possible wording adjustments, CR4 will say: If an ability instructs a player to take a modified action, any abilities triggered during or as a result of that action are considered nested abilities. If an ability instructs a player to take multiple actions (e.g. “Play three cards,” “Attack with two units”), that player performs each action sequentially. Any nested abilities must be resolved before proceeding to the next action.

`Editorial note: as this is referencing an expected rules change upcoming in CR4, it is not immediately applied to all current rulings.`

`(Answer shared on 2025-01-20)`

-------------------------------------------------

**Question:**

**What is done with a card that becomes no longer valid to play, but was originally valid?**

This is a complicated chain of events, but it’s all legal:

Play U-wing Reinforcements and choose Fleet Lieutenant x2. Play the first Fleet LT, which allows you to attack with an Ezra. Ezra attacks and, on completing his attack, his ability allows you to play A New Adventure, forcing your opponent to return and then replay Regional Governor. The opponent does so, naming Fleet Lieutenant. You no longer can play your second Fleet Lieutenant, despite being able to when you were initially choosing the cards for U-Wing. 

Does the second Fleet Lieutenant return to the deck with the remainder of the searched cards, does it go to the discard, is it removed from the game, or does it somehow bypass the Regional Governor restriction?


**Answer:**

This was not covered adequately in CR3. Good catch! We have added wording in 8.27.8 to account for this situation.

`(Answer shared on 2025-01-20)`

-------------------------------------------------

**Question:**

**If Caught In The Crossfire is played in Twin Suns by Player A and they select a unit from Player B and a unit from Player C in the same arena, and Player C's unit has a bounty and is defeated, does Player A or Player B get to collect the bounty?**

And why? Does 1.18 apply to Bounty control? Following the current CR as written it seems that Player A, as the active player who played the event, would NOT collect the bounty, it would instead go to Player B, but this seems counter to other rulings such as how Lurking TIE Phantom functions. 


**Answer:**

According to 1.18.1A, the player whose unit deals lethal damage is considered before the player whose ability is played, so in your example, Player B collects the Bounty.

`(Answer shared on 2025-01-20)`

-------------------------------------------------

**Question:**

**Does Lurking TIE Phantom take damage from indirect damage?**

If not, is it a valid target to assign indirect damage to?

What we know so far:
*8.4.2. When “can’t” is used in a card ability, that ability adjusts or overrides a default rule of play. The player controlling a card with such an ability must follow that ability over the default rule of play. 8.4.3. Restrictive abilities override permissive abilities. If an ability with the word “may” or “can” directly contradicts an ability that uses the word “can’t”, then the ability that uses “can’t” takes precedence.*

LTP text: *This unit can't be captured, damaged, or defeated by enemy card abilities.*

*3.7.6. A Shield token is a type of token upgrade. A Shield token is an upgrade with the Armor trait that gives the unit it is attached to +0 power and +0 HP and has the text: “If damage would be dealt to attached unit, prevent that damage. If you do, defeat a Shield token on it.” When an ability instructs a player to give a Shield token to a unit, they take a Shield token that has been set aside and attach it to that unit.*

Clarifications so far: *Indirect damage can't be "wasted" by assigning it to a unit with less remaining HP*
LTP wouldn't be wasting it due to remaining HP. Damage can be assigned there, it isn't a "prevent damage" effect. It's a "can't" which takes precedence over the default rule of play.

How should this actually be ruled?


**Answer:**

Lurking TIE Phantom can be assigned damage from indirect damage. "Can't be damaged" is a prevent effect, as clarified in CR4. We are considering the additional step of errataing LTP to use "prevent" wording but aren’t 100% on that yet.

`(Answer shared on 2025-01-20)`

-------------------------------------------------

**Question:**

**Does Spare The Target on Unrefusable Offer work if the controller is not the owner?**

A follow up to an older question. A bounty is always resolved by the opponent of the controller of the unit which is USUALLY not the owner of said card. We know Spare The Target played on a unit with Unrefusable Offer attached results in not being able to play the unit when resolving the bounty because it's in your opponent's hand, which is a hidden zone. How does it change if Spare the Target returns the unit in question to your own hand, such as if it had previously been swapped control with Change of Heart? Are you then able to play it from your own hand since it is NOT in a zone hidden to the controller of the bounty when resolving?

Comparing similar effects, we know the effect of A New Adventure works from your hand, or your opponent’s hand, to play the unit for free. Does this mean STT+UR could actually play the unit if your opponent allowed you to, but normally it fails because there’s no reason for them not to “fail to find” the unit that the effect is looking for?


**Answer:**

No, Spare the Target can never play a card from hand. Unrefusable Offer was a templating error and will be corrected in the coming errata.

`(Answer shared on 2025-01-20)`

-------------------------------------------------

**Question:**

**What is the exact timing of deployed leader unit Bossk's triggered ability?**

Since it triggers on the collection of a bounty, it is always triggered by the resolution of a triggered ability. Does this mean the second bounty resolution is always nested inside the first bounty resolution, or since the trigger is the completion of the resolution of the first bounty does Bossk trigger at the end and it is sequential instead of nested?

Example 1:
Player 1: has deployed Bossk leader unit and Wampa in play, and a Snowtrooper Lieutenant in the top 5 of the deck.

Player 2: has Clone Trooper in play with Bounty Hunter's Quarry attached.

Player 1 attacks and defeats Clone Trooper with Bossk, resolves bounty by playing Snowtrooper Lieutenant. When Played ability from Snowtrooper is now nested within the first bounty resolution. Can Player 1 choose to resolve bounty again using Bossk's ability before resolving the Snowtrooper (granting an attack to Wampa) because it is also nested inside the first bounty, or is the second bounty only triggered after the first bounty is fully resolved, and thus is resolved at the top layer instead of in the nested layer?


**Answer:**

Bossk leader's triggered ability triggers when you collect a Bounty, which 7.5.13D defines as resolving a Bounty ability. 7.6.11 says that all abilities triggered while resolving a triggered ability A are nested, so Bossk's ability is always nested.

`(Answer shared on 2025-01-20)`

-------------------------------------------------


## Rules clarifications from the dev team collected from social media:

### Set 4 - Jump to Lightspeed
* [Pilot leaders deployed as upgrades are vulnerable to upgrade removal.](https://x.com/davflamerock/status/1864353688514396577)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X107.png)
* [Chewie and Han can pilot on to Falcon in either order.](https://x.com/davflamerock/status/1864356237212520768)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X108.png)
* [Pilot leader upgrades affected by Bamboozle are defeated, and pilots that are in play as units count as having the keyword for Daimyō Boba.](https://x.com/davflamerock/status/1864372691974697291)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X109.png)
* [Piloting and Smuggle are both alternate costs, and can't be played together. Choose one or the other!](https://bsky.app/profile/davflamerock.bsky.social/post/3lcj5ajy3r222)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X110.png)
* [Indirect damage ignores shields, and must be assigned to targets with sufficient remaining HP that it is not wasted.](https://bsky.app/profile/davflamerock.bsky.social/post/3lcj5rjx27s2u)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X111.png)
* [Unique Pilot can't be in play as a unit and as an upgrade simultaneously.](https://x.com/davflamerock/status/1864441597783351536)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X112.png)
* [A Piloting keyworded card can be played via U-Wing Reinforcement (must come out as a unit), OR via A Fine Addition (must come out as an upgrade).](https://bsky.app/profile/davflamerock.bsky.social/post/3lcl2inaa2s2a)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/Y34.png)
* [Pilot upgrades do not ready attached unit when deployed.](https://bsky.app/profile/davflamerock.bsky.social/post/3lcjhaeyzok2y)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X114.png)
* [Pilot upgrades are defeated like any other upgrade if something happens to the attached unit.](https://x.com/davflamerock/status/1864467346284278118)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X115.png)
* [When a Pilot leader deploys as an upgrade and grants leader status to a unit, it does not alter the aspects provided by your deck construction.](https://bsky.app/profile/davflamerock.bsky.social/post/3lcl63bvc4k2o)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X116.png)
* [Pilot upgrades do not grant traits to attached units unless explicitly stated.](https://x.com/davflamerock/status/1877894904598106253)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X118.png)
* [Pilots can be played as upgrades by cards that explicitly play only upgrades, but they can't be searched for or drawn by cards that search for or draw upgrades specifically, as they still count as units while in deck and discard.](https://x.com/davflamerock/status/1878259405105639438)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X119.png)  
* [Pilots that were defeated as upgrades can be returned to hand by Gar Saxon's deployed leader unit ability that grants a When Defeated to upgraded units, due to Last Known Information rules.](https://bsky.app/profile/davflamerock.bsky.social/post/3lgbyvy5quk2j)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/Y35.png)
* [Eligible Pilots can be played by Cobb Vanth ability as a unit or an upgrade.](https://bsky.app/profile/davflamerock.bsky.social/post/3lggq5zgctk2u)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X127.png)
* [Indirect damage can only be assigned to deployed Chirrut leader unit up to remaining HP.](https://x.com/davflamerock/status/1879321937748652342)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X120.png)
* [Red Leader cost discount benefits from friendly PILOT units and friendly PILOT upgrades. Source includes some language templating philosophy as well.](https://x.com/davflamerock/status/1879964533701398737)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X121.png)
* [JTL Thrawn does not work on bounties. Also, keywords don't actually count as the abilities that they shorthand represent.](https://bsky.app/profile/davflamerock.bsky.social/post/3lg6rycfxsk2b)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X122.png)
* [JTL Thrawn deployed as a leader unit needs to be in play when the ability resolves in order to trigger it again.](https://x.com/davflamerock/status/1881383305645613110)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X123.png)
* [JTL Thrawn does not double Gideon Hask's ability, it only works with abilities that explicitly say "When Defeated" and not other variations of that.](https://x.com/davflamerock/status/1881426616943100335)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X124.png)
* [Indirect damage caused by an ability from a unit does trigger TWI Jango leader ability.](https://x.com/davflamerock/status/1882442362418528612)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X126.png)
* [A "space unit" (when referring to units in play) is a unit in the space arena.](https://bsky.app/profile/davflamerock.bsky.social/post/3lhec62k5sk26)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X128.png)
* [Wingman Victor Three played via Piloting can't grant XP to the attached unit.](https://bsky.app/profile/davflamerock.bsky.social/post/3lhrrr5z3bc25)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X129.png)
* [JTL Poe can deploy as a unit even if he was previously in play due to a combo like playing him as an upgrade and then Eject. Since Poe does not make attached units in to leader units, those units can be successfuly stolen by change of control effects, and Poe remains attached. The player that owns Poe still controls Poe and thus can still activate his ability to move him to a friendly vehicle.](https://bsky.app/profile/davflamerock.bsky.social/post/3lhwet3vxss2c)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X130.png)
* [JTL Poe can not attach as a pilot where R2 is already piloting, R2 would have to be piloted on to vehicle after Poe.](https://bsky.app/profile/davflamerock.bsky.social/post/3lhwjohgqn22q)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X131.png)
* [JTL Luke leader as a pilot upgrade is defeated by Bamboozle despite the protection.](https://bsky.app/profile/davflamerock.bsky.social/post/3li3jimisw227)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X132.png)
* [JTL Admiral Trench leader deploying on an empty deck does not deal damage to your own base.](https://bsky.app/profile/davflamerock.bsky.social/post/3li3pm5fgic2w)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X134.png)
* [JTL Krennic can provide his discount while being Exploited for an additional discount. Cost discounts may be applied in any order, to be clarified in CR5 update.](https://bsky.app/profile/davflamerock.bsky.social/post/3li3ozosqoc2w)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X135.png)
* [JTL "No Glory, Only Results" event played on an opposing Snoke results in active player controlling the constant ability of -2/-2 for an instant long enough to defeat enemies with 2 HP remaining prior to Snoke being defeated by the next part of the event card text.](https://bsky.app/profile/davflamerock.bsky.social/post/3li3oxlmbak2w)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X136.png)
* [JTL Ghost propagates the entire text of a BOUNTY keyword to other spectre units.](https://bsky.app/profile/davflamerock.bsky.social/post/3li5nkstkd22l)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X138.png)
* [JTL Swarming Vulture limit of 15 copies applies in Twin Suns as well as in Premier.](https://bsky.app/profile/davflamerock.bsky.social/post/3li5gsmdblk2q)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X139.png)
* [JTL Kazuda Xiono leader ability does not retroactively nullify effects generated by already resolved triggered abilities.](https://bsky.app/profile/davflamerock.bsky.social/post/3lihzv6hfts2n)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X141.png)
* [JTL Swarming Vulture limit of 15 applies to deck building, removing it during game play has no impact.](https://bsky.app/profile/davflamerock.bsky.social/post/3lihonvkyek27)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X142.png)
* [JTL CR4 update will alter how "Lose" an ability functions in the rules. Once an ability is lost, it can not be regained from another source. This is a change in rules that is not active until JTL set releases.](https://www.youtube.com/watch?v=LxzljnKY7Hw&t=294s)
  * [Implications: JTL Kaz can remove downsides of Trench Run and Heroic Sacrifice as long as it isn't already triggered (pending triggers always resolve, Kaz doesn't remove effects). Kaz prevents acquisition of all new abilities.](https://bsky.app/profile/willmlliw31.bsky.social/post/3limg3vmvgk2a)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X143.png)
* [Upgrade eligibilty should be checked any time the upgrade is attached, but the upgrade won't fall off if it becomes invalid later on (such as "Attach to a Force unit" temporarily losing the Force trait).](https://bsky.app/profile/davflamerock.bsky.social/post/3lj65yfns7s2c)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X144.png)
* [Pilots already in play can't be moved to a non-vehicle unit.](https://bsky.app/profile/davflamerock.bsky.social/post/3ljjsyboyb22x)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X145.png)
* [If a captured unit is guarded by a pilot unit that gets picked up by Corvus, making the pilot an upgrade, the captured card stays guarded by the (now upgrade) pilot. If the pilot (upgrade) leaves play, the card will be rescued.](https://bsky.app/profile/davflamerock.bsky.social/post/3lk2tcbqv7s2h)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X146.png)


### Set 3 - Twilight of the Republic
* [If one of the defenders when Darth Maul attacks is upgraded with Electrostaff, the negative power modifier applies to the whole attack, including the other defender.](https://bsky.app/profile/davflamerock.bsky.social/post/3lct4xvzb5s27)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X117.png)
* [A unit with Coordinate always has that keyword regardless of unit counts.](https://x.com/davflamerock/status/1824086962552074461)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X64.png)
* [Darth Maul does one attack with two targets, dealing full damage to both and receives all the damage back.](https://x.com/davflamerock/status/1811218025653350831)
  * [Also, one shield absorbs combat damage from both defenders.](https://x.com/davflamerock/status/1811437680271540621)
    * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X52.png)
* [Han2 leader ability can combo with Exploit.](https://x.com/davflamerock/status/1829682524441743773)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X67.png)
* [Exploit unit is in play by the time When Defeated triggers resolve from "exploited" units.](https://x.com/davflamerock/status/1835807491357327579)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X71.png)
* [Jango Fett leader ability only triggers if unit actually takes damage (not replaced by shield, etc).](https://x.com/davflamerock/status/1836831008811012305)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X73.png)
* [Jango Leader + Overwhelming Barrage will exhaust one unit (front side) or all the units (deployed side), but the damage can't be dealt to Lurking TIE Phantom because it is still a card ability.](https://x.com/davflamerock/status/1836793952818594013)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X74.png)
* [Damage from an ability like Vambrace Flamethrower can't be dealt to Lurking TIE Phantom, but it is dealt from the attached unit, so Jango + Flamethrower will exhaust all damaged units. Also works with Bossk, Dengar, Emperor Palpatine (unit) abilities.](https://x.com/davflamerock/status/1836797062106485217)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X75.png)
* [Piett's passive ability goes away before the card is finished being played, so he wouldn't give Ambush if he's sacrificed to Exploit.](https://x.com/davflamerock/status/1839313379967775124)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X76.png)
* [Lando leader can be used as a soft pass but you must defeat a resource.](https://x.com/davflamerock/status/1841253357039579265)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X77.png)
* [Jar Jar Binks randomly picks from entire pool of bases and units of all players.](https://x.com/davflamerock/status/1841938532950278237)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X78.png)
* [Unlimited Power must be different units for each damage assignment.](https://x.com/davflamerock/status/1843867562079334541) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X81.png) 
* [Using Clone on a card with Exploit does not allow Clone to use Exploit.](https://x.com/davflamerock/status/1845891327659061621) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X82.png) 
* [When defeated, Clone reverts completely, so it is not eligible for any effects based on traits it had while it was a copy.](https://x.com/davflamerock/status/1845891268653556025) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X83.png) 
* [If Clone copies an enemy Krayt, that opponent deals 9 damage when resolving the trigger from Krayt.](https://x.com/davflamerock/status/1845958005478633599) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X85.png) 
* [Defense of Kamino only applies to units in play when the event is resolved.](https://x.com/davflamerock/status/1846774997496537597) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X86.png) 
* ["Chancellor Palpatine Playing Both Sides" is Heroism for deck building in Twin Suns.](https://discord.com/channels/1079526508688847078/1108048788762931250/1296854323246137416) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X87.png) 
* ["Chancellor Palpatine Playing Both Sides" will not flip without the defeated unit condition being met.](https://x.com/davflamerock/status/1847308603775934898) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X88.png)
* ["Chancellor Palpatine Playing Both Sides" stays exhausted when flipping.](https://x.com/davflamerock/status/1847313783707849198) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X89.png) 
* ["Chancellor Palpatine Playing Both Sides" only provides access to the currently face up aspects.](https://x.com/davflamerock/status/1847640433100542417)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X90.png)
* [Clone will trigger and resolve the When Played abilities gained from the original cloned card.](https://x.com/davflamerock/status/1847640608460177576)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X91.png)
* [Barriss Offee's constant ability is a passive that applies to any unit that's been healed this phase while she's in play. It's not permanent or stacking.](https://x.com/davflamerock/status/1848861947288285480)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X92.png)
* [Darth Maul defeating two units at once does trigger Ruthlessness twice.](https://x.com/davflamerock/status/1850596777319121238)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X93.png)
* [Token unit custom substitutions will be up to TO.](https://x.com/davflamerock/status/1850965089362325948)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X94.png)
* [Darth Maul + Corner the Prey will get a single power bonus equal to the sum of both defender's damage.](https://x.com/davflamerock/status/1851353813304639801)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X95.png)
* [Darth Maul vs Sentinel, if the opponent has multiple units and only one Sentinel, Maul can only attack the Sentinel.](https://x.com/davflamerock/status/1851353813304639801)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X95.png)
* [If Bright Hope When Played targets a token unit, the controller still gets to draw a card.](https://x.com/davflamerock/status/1852106519082418337)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X96.png)
* [Capture targeting a token with a bounty: it does count as captured when it is set aside, and the bounty is collectable.](https://x.com/davflamerock/status/1852106904434282899)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X98.png)
* [Resources may be shuffled in any way if an opponent wishes to interact with them, as long as the NUMBER of ready is maintained, but not in the middle of resolving that interaction.](https://x.com/davflamerock/status/1852131316537426404)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/Y1.png)
* [Count Dooku Exploiting for When Played ability can assign all damage to one unit all at once, or assign the individual damage amounts to separate units.](https://x.com/davflamerock/status/1853189737781006429)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X99.png)
* [Chancellor Palpatine Playing Both Sides: leader ability can be used as a soft pass, but to resolve any of the ability the initial "if" condition must be true.](https://x.com/davflamerock/status/1852563553816834183)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X100.png)
* [Cloning a token unit doesn't make Clone behave like a token unit when leaving play, but it does count as a token unit while in play.](https://x.com/davflamerock/status/1857184457456750843)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X102.png)
* [Empty deck damage is caused by the player to their own base.](https://x.com/davflamerock/status/1857149881116144007)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X104.png)
* [I Have The High Ground event applies the lasting effect to the chosen friendly unit, so enemy units played later will still be impacted.](https://x.com/davflamerock/status/1858943562777264370)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X105.png)
* [Exploited units are defeated simultaneously. FFG Video time stamped at 40 minute mark.](https://youtu.be/rmGkF2R_UU8?t=2399)
  * [Example from video: When playing Separatist Super Tank, exploit Nala Se deployed leader unit and Batch Brothers to heal base for 2.](https://raw.githubusercontent.com/macfergusson/SWU/main/X106.png)
* [Seventh Sister ability can trigger via Overwhelm.](https://x.com/davflamerock/status/1835550402848125366)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X70.png)
* [A Once Per Round ability limit is attached to the copy of the card, not based on controller. It can't be used again if control changes in the same phase after it's been used.](https://bsky.app/profile/davflamerock.bsky.social/post/3lihoqgkac227)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X140.png)


### Set 2 - Shadows of the Galaxy
* [Outflank must choose a different unit for the second attack.](https://x.com/davflamerock/status/1843713500058923218) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X79.png)
* [Spark of Hope does not work with units that were defeated as resources.](https://x.com/davflamerock/status/1800275651372408860)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X7.png)
* [Pre Visla stealing Entrenched while attacking a base does not stop the attack.](https://x.com/davflamerock/status/1799120916313481681)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X8.png)
* [Hero Boba Leader works with Conditional Keywords only when they are active.](https://x.com/davflamerock/status/1795608545112797520)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X9.png)
* [Force Lightning on friendly Kylo Ren can nullify the -1/0](https://x.com/davflamerock/status/1793036911675617543)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X15.png)
* [Bounties in multiplayer are collected by the player that defeats or captures the unit.](https://x.com/davflamerock/status/1775978346972684410)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X25.png)
* [Lasting effects fall off when changing zones.](https://x.com/davflamerock/status/1800674819769614362)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X27.png)
* [If the resolution of an ability you control defeats a unit, you have defeated that unit.](https://x.com/davflamerock/status/1811804055452197369)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X29.png)
* [Lurking TIE Phantom can be defeated by -X/-X.](https://x.com/davflamerock/status/1803083519872081928)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X28.png)
* [Lurking TIE Phantom can be chosen for Power of the Dark Side and will not be defeated.](https://x.com/davflamerock/status/1803083654538703155)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X30.png)
* [Lurking TIE Phantom can be defeated by Force Lightning.](https://x.com/davflamerock/status/1803472509183897671)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X31.png)
* [Lurking TIE Phantom can not be defeated by Overwhelming Barrage.](https://x.com/davflamerock/status/1811194315001245786)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/Y32.png)
* [Han2 leader unit playing Stolen Landspeeder defeats the unit before it would change control.](https://x.com/davflamerock/status/1803196374646948344)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X33.png)
* [Jabba leader ability works with Reputable Hunter on turn 1.](https://x.com/davflamerock/status/1803831022523470323)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X35.png)
* [Bounties stack and cost discounts stack.](https://x.com/davflamerock/status/1805679212197445980)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X37.png)
* ["Next unit" discounts are consumed by playing a unit for free.](https://x.com/davflamerock/status/1805700413985013808)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X38.png)
* [First Light cost can be paid by defeating a Shield token.](https://x.com/davflamerock/status/1805985459882889705)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X40.png)
* [Migs triggers on Spark of Rebellion.](https://x.com/davflamerock/status/1806694108305453377)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X41.png)
* [Unrefusable Offer fails to resolve if Spare the Target collects the bounty.](https://x.com/davflamerock/status/1808642970817564881)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X43.png)
* [Lando leader and Timely Intervention: defeat resource prior to resolving Ambush.](https://x.com/davflamerock/status/1809626326082449872)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X45.png)
* [Defeating DJ with unique rules does not allow you to keep the stolen resource permanently.](https://x.com/davflamerock/status/1810364597062307986)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X47.png)
* [Superlaser Technician and Unrefusable Offer are mutually exclusive.](https://x.com/davflamerock/status/1810561816805695791)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X48.png)
* [When Lando leader smuggles, replace the resource before destroying a resource.](https://x.com/davflamerock/status/1810561430271271234)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X49.png)
* [Omega does not ignore her own aspect penalty.](https://x.com/davflamerock/status/1811195783007596772)  
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X50.png)
* [Omega ability text is not active while playing her.](https://x.com/davflamerock/status/1824134630053761197)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X51.png)
* [Bravado is determined by who owns the ability that caused defeat, passive HP modifiers like Snoke still count.](https://x.com/davflamerock/status/1811545409707475391)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X53.png)
* [Calculated Lethality can target Lurking TIE Phantom, it will not be defeated, but you do gain experience per upgrade.](https://x.com/davflamerock/status/1811805407498616953)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X54.png)
* [Bossk leader does not double collect Bounty if simultaneously defeated in combat.](https://x.com/davflamerock/status/1811804215729160363)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X55.png)
* [Resolve Poe's chosen options in any order](https://x.com/davflamerock/status/1812904489281585571)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X57.png)
* [IG-11 damage effect replaces the capture effect, so it happens at that same timing point.](https://x.com/davflamerock/status/1813607378954461241)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X59.png)
* [Lurking TIE should be read as immune to "enemy" "card ability" not "enemy card" "ability", so it is immune to the bounty on a friendly Val.](https://x.com/davflamerock/status/1815966557694013696)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X60.png)
* [If you control a unit with an opponent's Heroic Resolve attached, you can use the ability, defeating the upgrade to pay the cost.](https://x.com/davflamerock/status/1818014745175392311)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X62.png)
* [You can not discard a card to smuggle Bamboozle for free.](https://x.com/davflamerock/status/1818052088687161561)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X63.png)
* [Krayt vs Force Lightning: Krayt triggers, then ability is blanked, then the ability resolves and controller of ability deals 1 damage.](https://x.com/davflamerock/status/1824107830246326670)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X65.png)
* [Cost modifier on Bravado can apply when smuggling.](https://x.com/davflamerock/status/1826080749323178214)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X66.png)
* [Player A controls a Clone Deserter and Player B controls a Snoke, then Player C plays a Snoke. Player C will resolve the bounty.](https://x.com/davflamerock/status/1834683333877301725)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X69.png)
* [Scanning Officer new resources are exhausted](https://x.com/davflamerock/status/1794451475285876911)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X12.png)
* [If conditional Overwhelm is lost before combat damage resolution, excess damage does not apply to base.](https://x.com/davflamerock/status/1829563590640283671)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X68.png)


### Set 1 - Spark of Rebellion
* [Regional Governor applies to multiple versions of units with the same name,but a partial name is insufficient to cover multiple names.](https://x.com/davflamerock/status/1724862181622112505)
    * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X1.png)
* [Regional Governor change of controller does not impact who is prevented from playing the named unit.](https://x.com/davflamerock/status/1843713855148687360) 
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X80.png) 
* [Overwhelm has no excess damage against Chirrut.](https://x.com/davflamerock/status/1748410572511592768)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X2.png)
* [Strafing Gunship opposing a space Sentinel can only attack Sentinels on Ground or Space arena.](https://x.com/davflamerock/status/1752360268795937096)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X3.png)
* [Ambush trigger must be resolved by the triggering player with a unit they control.](https://x.com/davflamerock/status/1796205663174922695)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X13.png)
* [Pick multiple option type abilities are resolved one at a time, and you can pick as you go.](https://x.com/davflamerock/status/1812910719815590221)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X58.png)
* [A player controls abilities on cards that they play and control, including events.](https://x.com/davflamerock/status/1811803903048241399)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X56.png)
* [For Palpatine leader sacrifice of a unit, When Defeated triggers resolve after card draw and 1 damage.](https://x.com/davflamerock/status/1810346572649033732)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X46.png)
* [You may fail to find hidden information even if the opponent knows it is present.](https://x.com/davflamerock/status/1792995929190007222)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X16.png)
* [SpecForce Soldier can choose any unit including itself to lose Sentinel.](https://x.com/davflamerock/status/1779968977122247105)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X21.png)
* [For A Cause I Believe In resolves as one single damage trigger for all revealed cards.](https://x.com/davflamerock/status/1778790979065004482)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X22.png)
* [All triggers caused by Vigilance choices wait to resolve until after event fully resolves.](https://x.com/davflamerock/status/1792353938160902455)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X17.png)
* [Chirrut does not die from -X/-X effects](https://x.com/davflamerock/status/1785035713974542630)
  * [Chirrut can only be defeated with abilities that explicitly say "defeat" or by removing his ability with Force Lightning.](https://x.com/davflamerock/status/1785055555070918858)
    * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X18.png)
* [Rukh's ability does not resolve until end of combat damage step even with Shoot First.](https://x.com/davflamerock/status/1782834959062843438)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X19.png)
* [Triggers on each card played by U-Wing are resolved before playing the next card.](https://x.com/davflamerock/status/1782108035789308029)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X20.png)
* [Limited format decks can change leaders and bases between games.](https://x.com/davflamerock/status/1805279225718464687)
  * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/X36.png)
  * [Follow up clarification.](https://x.com/davflamerock/status/1808645223444021595)
    * [Screenshot](https://raw.githubusercontent.com/macfergusson/SWU/main/Y33.png)


## Rules clarifications from FFG via Jonah (Nexus manager):
* [If Blizzard Assault AT-AT gains overwhelm, it will deal it's excess damage to the opponent's base, and there will be no damage for the triggered ability.](https://discord.com/channels/1265343874105081856/1285661685381599354/1290820595357061140)  
* [When collecting the Stolen Landspeeder Bounty vs Snoke, it will have the additional HP added before the constant effect is checked.](https://discord.com/channels/1265343874105081856/1288101185508737044/1290821263270481991)
* [Can I rearrange my resources after Scanning Officer has chosen ready ones to make the chosen resources exhausted instead, and then defeat those resources? No.](https://discord.com/channels/1265343874105081856/1273307936155762830/1301624251043811390)
* [Constant abilities are "on" immediately when a unit enters play, even if game state checks (such as uniqueness) are currently preventing effects from resolving such as a unit being defeated due to remaining HP.](https://discord.com/channels/1265343874105081856/1273307936155762830/1311072296248541335)
* [If multiple units are defeated for a single exploit, they are all defeated simultaneously.](https://discord.com/channels/1265343874105081856/1273307936155762830/1311072296248541335)
* [A Fine Addition may not be played as a soft pass if an eligible target upgrade exists in any player's discard.](https://discord.com/channels/1265343874105081856/1273307936155762830/1311072296248541335)


## Official Card Text Errata
* Blizzard Assault AT-AT (Spark of Rebellion, 88) - While attacking, this unit may deal its excess damage to an enemy ground unit."
* Bo-Katan Kryze (Shadows of the Galaxy, 12) - On Attack: You may deal 1 damage to a unit. Then, if you attacked with another Mandalorian unit this phase, you may deal 1 damage to a unit. (The same unit or a different unit.)
* Migs Mayfeld (Shadows of the Galaxy, 163) - When a player discards a card from a hand: You may deal 2 damage to a unit or base. Use this ability only once each round.
* Unrefusable Offer (Shadows of the Galaxy, 226) - Attach to a non-leader unit. Attached unit gains: “Bounty — Play this unit from its owner's discard pile or from capture for free (under your control). It enters play ready. At the start of the regroup phase, defeat it."
* I Have the High Ground (Twilight of the Republic, 72) - Choose a friendly unit. For this phase, while that unit is defending, the attacker gets –4/–0.
* Sly Moore (Twilight of the Republic, 211) - When Played: Take control of an enemy token unit and ready it. At the start of the regroup phase, that token unit's owner takes control of it.
* Wingman Victor Three (Jump to Lightspeed, 86) - When played as an upgrade: You may give an Experience token to a unit other than the attached unit.


## "Unofficial" Rules explainers:
* [All components of Reinforcement Walker ability are ignored on an empty deck.](https://discord.com/channels/1079526508688847078/1079527291283067020/1214252641174028348)
* [Defeated tokens do leave play.](https://discord.com/channels/1079526508688847078/1079527291283067020/1214252641174028348)
* [Moving Traitorous around with Survivors Gauntlet.](https://discord.com/channels/1079526508688847078/1173630114379079711/1240331386058051686)
* [For Moff Gideon, both the power and the Overwhelm are only while attacking a unit.](https://discord.com/channels/1079526508688847078/1079527291283067020/1225162007628484719)
* [Superlaser Technician and Unrefusable Offer do not play well together.](https://discord.com/channels/1079526508688847078/1079527291283067020/1252346793136754854)
* [When putting cards back after For A Cause I Believe In, the opponent DOES get to know the order of the cards since they are all revealed through the effect.](https://discord.com/channels/1079526508688847078/1079527291283067020/1186384076156977183)
* [Applying an effect to a token unit still counts for "if you do" effects. E.G. Bright Hope on a token unit, or capturing a token unit with a bounty.](https://discord.com/channels/1079526508688847078/1079527291283067020/1301646164634112121)


## Official Resources:
* [Comprehensive Rules](https://starwarsunlimited.com/how-to-play?chapter=rules)
* [Organized Play Documents: Tournament Regulations and Master Events Document](https://starwarsunlimited.com/organized-play#links)
* [Cascade Games Official SWU Judging Program](https://nexus.cascadegames.com/)


## Commonly asked questions
* Trigger timing is not the same as timing of resolution of that ability.
* Events only affect units that are in play when the event is played, unless explicitly stated otherwise.
* Overwhelm will still damage the base if the defending unit is defeated by an On Attack ability.
* Chirrut doesn't die to negative HP modifiers during action phase.
* Krayt Dragon always triggers.
* Bounties are not inherently upgrades, but upgrades can give bounties to attached unit.
* Tokens and leaders enter play but are not played (for the purposes of When Played triggers).
* Pay costs as normal for ambushing a unit when using Energy Conversion Lab Epic Action.
* Lurking TIE Phantom is immune explicitly to defeat, capture, and damage from enemy abilities, which means actual combat damage, HP modifiers, and return to hand are usually the best options for removing it.
* Fan made projects like Force Table and Karabast are not an official source of rules. If something seems off, double check with your friendly local judge and/or SWU discord rules chats, and let the maintainers know if you found something incorrect!


## Other useful resources/community tools:
* [SWUDB - Card database and collection tracking](https://www.swudb.com/)
* [GarbageRollers New player guide](https://garbagerollers.com/new-player-lessons-and-guides/)
* ["Who is the beatdown" tactical discussion](https://thefifthtrooper.com/whos-the-beatdown-star-wars-unlimited-edition/)
* [Karabast - An online tool for playtesting against other humans](https://karabast.net/SWUOnline/MainMenu.php)
* [ForceTable - An online tool for playtesting against a bot](https://www.forcetable.net/swu/quick-match)
* [SWU Community Discord](https://discord.gg/gKQnAWbdss)