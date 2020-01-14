//
//  Dealer.h
//  BlackJack
//
//  Created by Shane Kelley on 1/23/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//
#include "Player.h"
#include "Deck.h"
#include <vector>
using namespace std;
#ifndef Dealer_h
#define Dealer_h
class Dealer: public Player{    //create dealer class
private:
    string dealerName;      //keep track of deaalers name
    vector<Card> dealerHand;    //dealers hand of cards
    bool isBusted;          //keep track if dealer has busted
    bool turnDone;          //keep track if turnis done
    
public:
    Dealer();           //default constructor
    Dealer(string dealName);    //copy constructor
    int dealerHit(Deck d);  //dealer hits for an extra card
    bool getTurnDone() const;
    
};


#endif /* Dealer_h */
