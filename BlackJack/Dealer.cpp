//
//  Dealer.cpp
//  BlackJack
//
//  Created by Shane Kelley on 1/23/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//

#include "Dealer.h"
#include "Deck.h"
#include <iostream>
#include <vector>
using namespace std;

Dealer::Dealer(){           //default constructor
    dealerName = "Dealer";
    isBusted = false;
};
Dealer::Dealer(string name){    //copy constructor
    dealerName = name;
    isBusted = false;
    turnDone = false;
};

int Dealer::dealerHit(Deck d){  //dealer hit
    int total;
    if (this->getTotal() < 17) {    // if the dealers total is less than 17 then hit
        this->hit(d);
    }
    else if (this->getTotal() >= 17 and this->getTotal() <= 21) //if dealer between 17 and 21 stay
         total = this->stay();
    else{               //if dealer over 21 busted
        total = 0;
        isBusted = true;
        turnDone = true;
    }
    return total;
};

bool Dealer::getTurnDone() const {
    return turnDone;
};
