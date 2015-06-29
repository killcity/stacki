# @SI_Copyright@
# @SI_Copyright@

import stack.commands.set.network

class Command(stack.commands.set.network.command):
	"""
	Sets the network mask for one or more networks.

        <arg type='string' name='network' optional='1' repeat='1'>
        The names of zero of more networks. If no network is specified
        the mask is set for all existing networks.
	</arg>
	
	<param type='string' name='mask' optional='0'>
        Mask that the named network should have.
	</param>
	
	<example cmd='set network mask ipmi mask=255.255.255.0'>
        Sets the "ipmi" network mask to 255.255.255.0.
	</example>
	"""
                
        def run(self, params, args):

                (networks, mask) = self.fillSetNetworkParams(args, 'mask')
			        	
        	for network in networks:
			self.db.execute("""
                        	update subnets set mask='%s' where
				subnets.name='%s'
                                """ % (mask, network))
