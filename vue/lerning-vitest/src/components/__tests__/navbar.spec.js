import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";
import Navbar from '../Navbar.vue';

describe('navbar', () => {
  it('when showLogin is false showLoginButton is true', () => {
    const wrapper = mount(Navbar, {
      props: {
        showLogin:false 
      }
    })

    expect(wrapper.vm.showLoginButton).toBe(true);
  });

  it('when showLogin is true showLoginButton is false', () => {
    const wrapper = mount(Navbar, {
      props: {
        showLogin: true 
      }
    })

    expect(wrapper.vm.showLoginButton).toBe(false);
  });

  it('onClick emit updateShowLogin', async () => {
    const wrapper = mount(Navbar, {
      props: {
        showLogin: false 
      }
    })

    await wrapper.find('button').trigger('click');

    expect(wrapper.emitted()).toHaveProperty('updateShowLogin');
  })
})

