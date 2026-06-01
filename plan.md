## Project Plan
Labubu And Minion War Battle
### Gameplay Plan
[Canva Flowchart Link](https://canva.link/hocyaqg51uah9pm)
### Requirements List
**Basic Game**  
* Character class
  * alive (bool)
  * health (int)
  * max health (int)
  * moves (list of Move objects?)
* Move class
  * dmg range (list of 2 ints)
  * use move method
* Labubu child class of Character
  * Attack method
* Minion child class of Character
  * Choose move method
* Battle function
* 1 battle
* Minimum 2 different moves for each character
* Brief intro and outro for story

**Game Game**
* Option for multiple battles
* Add currency attribute to Character class
* Add inventory to Character class
* Currency system
  * Defeating Labubu drops currency
* Item class
  * price (int)
  * effect type (str, ex. "heal", "dmg boost")
  * effect quantity (int or float?)
* Shop child class of Inventory
* 1 shop item: healing potion
  * Used in between battles
* Additional character moves
* Incorporate additional story elements (ex. revise intro/outro for more story, additional mid-game narratives)

**Advanced Game**
* Additional shop items that provide boosts (ex. dmg boost)
* Bossfight unlockable after defeating a certain amount of Labubus