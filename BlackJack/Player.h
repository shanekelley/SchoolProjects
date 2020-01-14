//
//  Player.h
//  BlackJack
//
//  Created by Shane Kelley on 1/23/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//
#include "Hand.h"
#include "Deck.h"
#include <vector>
using namespace std;
#ifndef Player_h
#define Player_h
class Player: public Hand{          //create class player
private:
    vector<Card> playerHand;        //vector for cardin players hand
    bool isBusted;                  //keep track if player is busted
    bool turnDone;                  //keep track of if the player finished their turn
    
public:
    Player();                       //default constructor
    int stay();                     //method to keep the current hand
    void hit(Deck d);               //method to hit and get new card
    bool getIsBusted() const;       //gets value of isBusted
    
};



#endif /* Player_h */
