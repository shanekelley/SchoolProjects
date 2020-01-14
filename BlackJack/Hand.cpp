//
//  Hand.cpp
//  BlackJack
//
//  Created by Shane Kelley on 1/17/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//

#include "Hand.h"
#include <iostream>
#include <vector>
using namespace std;


Hand::Hand(){           //default constructor
};

void Hand::clearHand(){
    while (vecHand.empty() == false)    //while there are still items in the hand delete the last one until no more left
        vecHand.pop_back();
};
void Hand::addCard(Card c){         //add card to hand vector
    vecHand.push_back(c);
};
int Hand::getTotal() const{
    int j = vecHand.size();
    int i = 0;
    int total = 0;
    int hasAce = 0;
    while (i < j){                              //check if any cards in hand are aces
        if (vecHand[i].checkAce() == true){
            hasAce++;
        };
    };
    i = 0;                  //reset i to 0 to iterate through vector again
    while (i < j){          //while i is less than the number of elements in hand then get the value of ith card and add it to total
        total += vecHand[i].getValue();
        i++;
    };
    
    while (total > 21 and hasAce > 0) {     //if total is over 21 and there is at least one ace in the hand go ace low and check again
        total -= 10;
        hasAce--;
        };
    return total;
};

int Hand::getCardsRemaining() const{
    return vecHand.size();      //return how many cards are in hand vector
};

Card Hand::getSecondCard() const{
    return vecHand[1];
};

void Hand::outputCards() const {
    for (int i = 0; i < vecHand.size(); i++) {
        cout << i;
    }
}


