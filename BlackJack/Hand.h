//
//  Hand.h
//  
//
//  Created by Shane Kelley on 1/17/17.
//
//
#include <vector>
#include "Card.h"
using namespace std;
#ifndef Hand_h
#define Hand_h

class Hand{                     //create a class named hand
private:
    vector<Card> vecHand;       //vector to hold cards
    
public:
    Hand();                     //constructor
    void clearHand();           //remove all items in hand vector
    void addCard(Card card);    //add new card to hand vector
    int getTotal() const;       //get sum of card values in hand vecto
    int getCardsRemaining() const;  //return number of cards in hand vector
    Card getSecondCard() const;
    void outputCards() const;
    
};


#endif /* Hand_h */
