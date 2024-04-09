import React from 'react';
import { View, StyleSheet, TouchableOpacity } from 'react-native';
import { FontAwesome5 } from '@expo/vector-icons';

const Nav = () => {
  return (
    <View style={[styles.nav, styles.shadowProp]}>
      <TouchableOpacity
        accessible={true}
        accessibilityLabel='Home button was pressed!'
        onPress={() => console.log('Home button pressed')}
      >
        <FontAwesome5 name='home' style={styles.icon} />
      </TouchableOpacity>
      <TouchableOpacity
        accessible={true}
        accessibilityLabel='Ingredients button was pressed!'
        onPress={() => console.log('Ingredient button pressed')}
      >
        <FontAwesome5 name='apple-alt' style={styles.icon} />
      </TouchableOpacity>
      <TouchableOpacity
        accessible={true}
        accessibilityLabel='Shopping bag button was pressed!'
        onPress={() => console.log('Shopping bag button pressed')}
      >
        <FontAwesome5 name='shopping-bag' style={styles.icon} />
      </TouchableOpacity>
      <TouchableOpacity
        accessible={true}
        accessibilityLabel='Account button was pressed!'
        onPress={() => console.log('Account button pressed')}
      >
        <FontAwesome5 name='user-circle' style={styles.icon} />
      </TouchableOpacity>
      <TouchableOpacity
        accessible={true}
        accessibilityLabel='Search button was pressed!'
        onPress={() => console.log('Search button pressed')}
      >
        <FontAwesome5 name='search' style={styles.icon} />
      </TouchableOpacity>
    </View>
  );
};
//Test

const styles = StyleSheet.create({
  nav: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    backgroundColor: 'white',
    height: 60,
  },
  icon: {
    color: 'black',
    fontSize: 24,
    padding: 10,
  },
  shadowProp: {
    shadowColor: '#171717',
    shadowOffset: { width: 0, height: -2 },
    shadowOpacity: 0.2,
    shadowRadius: 3,
  },
});

export default Nav;